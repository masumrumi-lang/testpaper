/**
 * DataLoader Service
 * ==================
 * Loads per-subject JSON data files using fetch().
 * Caches Promises (not resolved data) to prevent duplicate concurrent requests.
 * Reads manifest.json first so file paths are never hardcoded.
 *
 * Usage:
 *   DataLoader.loadChapter('fin1', '1').then(chapterData => { ... });
 */
const DataLoader = (() => {
  'use strict';

  // ── State ──────────────────────────────────────────────────────────────────
  /** @type {Promise|null}  Single shared Promise for manifest loading */
  let _manifestPromise = null;

  /** @type {Map<string, Promise>}  subjectId → Promise<subjectData> */
  const _cache = new Map();

  // ── Internal helpers ───────────────────────────────────────────────────────

  /**
   * Load and cache manifest.json.
   * Returns the same Promise on repeated calls (no duplicate requests).
   * @returns {Promise<Object>} manifest object
   */
  function _loadManifest() {
    if (_manifestPromise) return _manifestPromise;

    // Use absolute path from repository root for GitHub Pages compatibility
    const manifestPath = '/testpaper/static-data/manifest.json';
    
    _manifestPromise = fetch(manifestPath)
      .then(function (res) {
        if (!res.ok) {
          throw new Error(
            'DataLoader: failed to load manifest.json (HTTP ' + res.status + ')'
          );
        }
        return res.json();
      })
      .catch(function (err) {
        // Reset so a later call can retry
        _manifestPromise = null;
        throw err;
      });

    return _manifestPromise;
  }

  /**
   * Load and cache a subject JSON file.
   * Caches the Promise itself — if two callers request the same subject
   * before it resolves, only one network request is made.
   *
   * @param {string} subjectId
   * @returns {Promise<Object>} subject data keyed by chapter id
   */
  function loadSubject(subjectId) {
    if (_cache.has(subjectId)) {
      return _cache.get(subjectId);
    }

    const promise = _loadManifest().then(function (manifest) {
      const subjectInfo = manifest.subjects && manifest.subjects[subjectId];
      if (!subjectInfo) {
        throw new Error(
          'DataLoader: subject "' + subjectId + '" not found in manifest.json'
        );
      }

      return fetch(subjectInfo.file).then(function (res) {
        if (!res.ok) {
          throw new Error(
            'DataLoader: failed to load ' + subjectInfo.file +
            ' (HTTP ' + res.status + ')'
          );
        }
        return res.json();
      });
    });

    // Store the Promise immediately (before it resolves) so concurrent callers
    // share it rather than firing duplicate network requests.
    _cache.set(subjectId, promise);

    // On failure, remove the cached entry so a retry is possible
    promise.catch(function () {
      _cache.delete(subjectId);
    });

    return promise;
  }

  /**
   * Load data for a specific chapter.
   *
   * @param {string} subjectId
   * @param {string} chapterId
   * @returns {Promise<Object|null>} chapter data object, or null if not found
   */
  function loadChapter(subjectId, chapterId) {
    return loadSubject(subjectId).then(function (subjectData) {
      return subjectData[chapterId] || null;
    });
  }

  /**
   * Pre-warm: load the manifest in the background so it is ready
   * by the time the page needs data.
   */
  function preloadManifest() {
    _loadManifest();
  }

  // ── Public API ─────────────────────────────────────────────────────────────
  return {
    loadSubject:     loadSubject,
    loadChapter:     loadChapter,
    preloadManifest: preloadManifest,
  };
})();
