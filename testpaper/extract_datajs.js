#!/usr/bin/env node
/**
 * extract_datajs.js
 * =================
 * Reads data.js, evaluates it to obtain testDatabase,
 * then writes one JSON file per subject to static-data/.
 * Also writes static-data/manifest.json.
 *
 * Usage:  node extract_datajs.js
 * Output: static-data/<subject>.json  (one per subject)
 *         static-data/manifest.json
 */

'use strict';

const fs   = require('fs');
const path = require('path');

const DATA_JS    = path.resolve(__dirname, 'data.js');
const OUTPUT_DIR = path.resolve(__dirname, 'static-data');
const LOG_FILE   = path.resolve(__dirname, 'extract_datajs.log');

const logLines = [];
function log(msg) {
    console.log(msg);
    logLines.push(msg);
}

function writeLog() {
    fs.writeFileSync(LOG_FILE, logLines.join('\n') + '\n', 'utf8');
}

// ─── 1. Load data.js ─────────────────────────────────────────────────────────

log('='.repeat(65));
log('  EXTRACT data.js → per-subject JSON');
log('='.repeat(65));

if (!fs.existsSync(DATA_JS)) {
    log('[FATAL] data.js not found at: ' + DATA_JS);
    writeLog();
    process.exit(1);
}

log('\n[STEP 1] Reading data.js ...');
const rawContent = fs.readFileSync(DATA_JS, 'utf8');
log(`         Size: ${(rawContent.length / 1024 / 1024).toFixed(2)} MB`);

// ─── 2. Evaluate to extract testDatabase ─────────────────────────────────────

log('\n[STEP 2] Evaluating data.js ...');
let testDatabase;
try {
    // Use the same proven pattern from scratch/inspect_bus2_datajs.js
    testDatabase = (new Function(rawContent + '\nreturn testDatabase;'))();
} catch (err) {
    log('[FATAL] Failed to evaluate data.js: ' + err.message);
    writeLog();
    process.exit(1);
}

if (!testDatabase || typeof testDatabase !== 'object') {
    log('[FATAL] testDatabase is not a valid object after eval.');
    writeLog();
    process.exit(1);
}

const subjectIds = Object.keys(testDatabase);
log(`         Subjects found: ${subjectIds.join(', ')}`);
log(`         Total subjects: ${subjectIds.length}`);

// ─── 3. Create output directory ───────────────────────────────────────────────

log('\n[STEP 3] Creating static-data/ directory ...');
fs.mkdirSync(OUTPUT_DIR, { recursive: true });
log(`         Output dir: ${OUTPUT_DIR}`);

// ─── 4. Write per-subject JSON files ─────────────────────────────────────────

log('\n[STEP 4] Extracting subjects ...\n');

const manifest = { subjects: {} };
let totalChapters = 0;

for (const subjectId of subjectIds) {
    const subjectData = testDatabase[subjectId];
    const chapters    = Object.keys(subjectData).sort((a, b) => parseInt(a) - parseInt(b));

    // Get human-readable subject name from first chapter that has it
    let subjectName = subjectId;
    for (const ch of chapters) {
        if (subjectData[ch] && subjectData[ch].subjectName) {
            subjectName = subjectData[ch].subjectName;
            break;
        }
    }

    // Count MCQs, shortCQs, fullCQs across all chapters
    let mcqCount = 0, shortCount = 0, fullCount = 0;
    for (const ch of chapters) {
        const d = subjectData[ch];
        if (!d) continue;
        mcqCount   += (d.mcqData      || []).length;
        shortCount += (d.shortCQData  || []).length;
        fullCount  += (d.fullCQData   || []).length;
    }

    const outFile = path.join(OUTPUT_DIR, `${subjectId}.json`);
    const json    = JSON.stringify(subjectData, null, 2);
    fs.writeFileSync(outFile, json, 'utf8');

    const fileSizeKB = (fs.statSync(outFile).size / 1024).toFixed(0);
    const relPath    = `static-data/${subjectId}.json`;

    log(
        `  ✓ ${subjectId.padEnd(8)}` +
        `  ${chapters.length} ch` +
        `  MCQ:${mcqCount}  shortCQ:${shortCount}  fullCQ:${fullCount}` +
        `  → ${relPath} (${fileSizeKB} KB)`
    );

    manifest.subjects[subjectId] = {
        name:     subjectName,
        chapters: chapters,
        file:     relPath,
    };

    totalChapters += chapters.length;
}

// ─── 5. Write manifest.json ───────────────────────────────────────────────────

log('\n[STEP 5] Writing manifest.json ...');
const manifestPath = path.join(OUTPUT_DIR, 'manifest.json');
fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), 'utf8');
log(`         Subjects: ${subjectIds.length}`);
log(`         Chapters: ${totalChapters}`);
log(`         Path: ${manifestPath}`);

// ─── 6. Validation ────────────────────────────────────────────────────────────

log('\n[STEP 6] Validating outputs ...');
let errors = 0;
for (const subjectId of subjectIds) {
    const outFile = path.join(OUTPUT_DIR, `${subjectId}.json`);
    try {
        const parsed = JSON.parse(fs.readFileSync(outFile, 'utf8'));
        const chs = Object.keys(parsed);
        if (chs.length === 0) {
            log(`  ✗ ${subjectId}: empty object`);
            errors++;
        }
    } catch (e) {
        log(`  ✗ ${subjectId}: JSON parse error — ${e.message}`);
        errors++;
    }
}
if (errors === 0) {
    log(`  ✓ All ${subjectIds.length} subject files validated successfully`);
} else {
    log(`  ✗ ${errors} validation error(s) found`);
}

// ─── Done ─────────────────────────────────────────────────────────────────────

log('\n' + '='.repeat(65));
log(`  EXTRACTION COMPLETE`);
log(`  Subjects : ${subjectIds.length}`);
log(`  Chapters : ${totalChapters}`);
log(`  Files    : ${path.join(OUTPUT_DIR, '*.json')}`);
log(`  Original data.js is UNTOUCHED.`);
log('='.repeat(65));

writeLog();
process.exit(errors > 0 ? 1 : 0);
