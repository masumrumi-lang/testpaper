/**
 * OpenRouter AI Integration for Etestpaper / Antigravity
 * -------------------------------------------------------
 * Primary model  : minimax/minimax-m2.5:free
 * Fallback model : meta-llama/llama-3.1-8b-instruct:free
 *
 * Features:
 *   - Structured accounting output (Accounting Worksheet formatting)
 *   - Automatic fallback when primary model is unavailable / rate-limited
 *   - Fallback event logging for debugging
 *   - Dashboard-safe: never throws unhandled errors
 */

// ─── Configuration ───────────────────────────────────────────────────────────

const OPENROUTER_CONFIG = {
    apiUrl: 'https://openrouter.ai/api/v1/chat/completions',
    primaryModel: 'minimax/minimax-m2.5:free',
    fallbackModel: 'meta-llama/llama-3.1-8b-instruct:free',
    referer: 'https://github.com/masumrumi-lang/antigravity',
    siteName: 'Etestpaper Antigravity',
    maxRetries: 2,
    timeoutMs: 30000,
};

// ─── Fallback Log ────────────────────────────────────────────────────────────

const _fallbackLog = [];

function logFallbackEvent(reason, primaryModel, fallbackModel) {
    const entry = {
        timestamp: new Date().toISOString(),
        reason: reason,
        primaryModel: primaryModel,
        fallbackModel: fallbackModel,
    };
    _fallbackLog.push(entry);

    // Keep only the last 50 entries in memory
    if (_fallbackLog.length > 50) _fallbackLog.shift();

    // Persist to localStorage for post-mortem debugging
    try {
        localStorage.setItem(
            'openrouter_fallback_log',
            JSON.stringify(_fallbackLog)
        );
    } catch (_) {
        /* localStorage may be unavailable */
    }

    console.warn('[OpenRouter] Fallback activated:', entry);
}

/** Retrieve the fallback log (useful from the browser console). */
function getOpenRouterFallbackLog() {
    return JSON.parse(
        localStorage.getItem('openrouter_fallback_log') || '[]'
    );
}

// ─── API Key Management ──────────────────────────────────────────────────────

function getApiKey() {
    return (
        localStorage.getItem('openrouter_api_key') || ''
    );
}

function setApiKey(key) {
    localStorage.setItem('openrouter_api_key', key.trim());
}

// ─── System Prompt ───────────────────────────────────────────────────────────

const ACCOUNTING_SYSTEM_PROMPT = `You are an expert HSC-level Accounting tutor for the Bangladesh Higher Secondary Certificate examination.

CORE RULES — follow every one without exception:

1. **Accounting Worksheet format**
   When producing any worksheet, ledger, journal, trial balance, or financial statement you MUST use the project's standard *table notation*:
   \`\`\`
   *table
   Column1 | Column2 | Column3 | ...
   ---
   Row1Col1 | Row1Col2 | Row1Col3 | ...
   Row2Col1 | Row2Col2 | Row2Col3 | ...
   *end
   \`\`\`

2. **10-Column Accounting Worksheet** (কার্যপত্র)
   Use exactly these column headers when a full worksheet is requested:
   \`Account Name | Trial Balance Dr. | Trial Balance Cr. | Adjustments Dr. | Adjustments Cr. | Adjusted Trial Balance Dr. | Adjusted Trial Balance Cr. | Income Statement Dr. | Income Statement Cr. | Balance Sheet Dr. | Balance Sheet Cr.\`

3. **Journal entries** must include: Date | Particulars (with "Dr." / "Cr." labels) | L.F. | Debit (৳) | Credit (৳)

4. **Ledger (খতিয়ান)** must use the standard T-account *table notation* with Date | Particulars | J.F. | Amount columns on each side.

5. All currency amounts are in Bangladeshi Taka (৳). Use commas for thousands (e.g., ৳1,25,000). Never use dollar signs.

6. Use Bengali terms where standard in HSC exams (e.g., জাবেদা, খতিয়ান, রেওয়ামিল, কার্যপত্র) alongside English equivalents.

7. Show full working/calculations. Do not skip steps.

8. When answering MCQs or short questions, be concise but precise. Cite relevant accounting standards or textbook chapters when applicable.

9. Respond in the same language the user writes in (Bengali or English). If the user mixes both, prefer Bengali with English accounting terms.`;

// ─── Core Request Logic ──────────────────────────────────────────────────────

/**
 * Build the request headers for OpenRouter.
 */
function _buildHeaders(apiKey) {
    return {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`,
        'HTTP-Referer': OPENROUTER_CONFIG.referer,
        'X-Title': OPENROUTER_CONFIG.siteName,
    };
}

/**
 * Build the request body for a chat completion.
 * @param {string} model   - The model ID to use.
 * @param {string} prompt  - The user's message.
 * @param {Array}  history - Optional prior messages [{role, content}, ...].
 */
function _buildBody(model, prompt, history) {
    const messages = [
        { role: 'system', content: ACCOUNTING_SYSTEM_PROMPT },
    ];

    if (Array.isArray(history)) {
        messages.push(...history);
    }

    messages.push({ role: 'user', content: prompt });

    return JSON.stringify({
        model: model,
        messages: messages,
        temperature: 0.3,        // Lower temperature for structured accounting output
        max_tokens: 4096,
    });
}

/**
 * Determine whether an error/response warrants a fallback attempt.
 */
function _shouldFallback(status, bodyJson) {
    // Network-level failures
    if (!status) return true;

    // Rate-limited
    if (status === 429) return true;

    // Server overloaded / unavailable
    if (status === 502 || status === 503 || status === 504) return true;

    // OpenRouter-specific: model unavailable
    if (
        bodyJson &&
        bodyJson.error &&
        typeof bodyJson.error.message === 'string'
    ) {
        const msg = bodyJson.error.message.toLowerCase();
        if (
            msg.includes('unavailable') ||
            msg.includes('overloaded') ||
            msg.includes('rate limit') ||
            msg.includes('capacity') ||
            msg.includes('not available') ||
            msg.includes('no endpoints')
        ) {
            return true;
        }
    }

    return false;
}

/**
 * Execute a single completion request with timeout.
 * Returns { ok, status, data } — never throws.
 */
async function _fetchCompletion(model, prompt, history, apiKey) {
    const controller = new AbortController();
    const timer = setTimeout(
        () => controller.abort(),
        OPENROUTER_CONFIG.timeoutMs
    );

    try {
        const response = await fetch(OPENROUTER_CONFIG.apiUrl, {
            method: 'POST',
            headers: _buildHeaders(apiKey),
            body: _buildBody(model, prompt, history),
            signal: controller.signal,
        });

        clearTimeout(timer);

        let data;
        try {
            data = await response.json();
        } catch (_) {
            data = null;
        }

        return { ok: response.ok, status: response.status, data };
    } catch (err) {
        clearTimeout(timer);
        return {
            ok: false,
            status: null,
            data: { error: { message: err.message || 'Network error' } },
        };
    }
}

// ─── Public API ──────────────────────────────────────────────────────────────

/**
 * Send a prompt to the OpenRouter accounting assistant.
 *
 * @param {string} prompt   - The user's question / request.
 * @param {Array}  [history] - Optional conversation history.
 * @returns {Promise<{
 *   success: boolean,
 *   content: string,
 *   model: string,
 *   fallbackUsed: boolean,
 *   error: string|null
 * }>}
 *
 * This function NEVER throws. The dashboard can always safely read the result.
 */
async function askAccountingAssistant(prompt, history) {
    const apiKey = getApiKey();

    if (!apiKey) {
        return {
            success: false,
            content: '',
            model: '',
            fallbackUsed: false,
            error: 'OpenRouter API key is not set. Please add your key in the AI Settings panel.',
        };
    }

    // ── Attempt 1: Primary model ─────────────────────────────────────────
    const primary = await _fetchCompletion(
        OPENROUTER_CONFIG.primaryModel,
        prompt,
        history,
        apiKey
    );

    if (primary.ok && primary.data && primary.data.choices && primary.data.choices.length > 0) {
        return {
            success: true,
            content: primary.data.choices[0].message.content,
            model: OPENROUTER_CONFIG.primaryModel,
            fallbackUsed: false,
            error: null,
        };
    }

    // ── Determine if fallback is appropriate ─────────────────────────────
    if (!_shouldFallback(primary.status, primary.data)) {
        // Hard error (e.g. 401 auth failure) — no point retrying with another model
        const errMsg =
            (primary.data && primary.data.error && primary.data.error.message) ||
            `Request failed with status ${primary.status}`;
        return {
            success: false,
            content: '',
            model: OPENROUTER_CONFIG.primaryModel,
            fallbackUsed: false,
            error: errMsg,
        };
    }

    // ── Log the fallback event ───────────────────────────────────────────
    const reason =
        (primary.data && primary.data.error && primary.data.error.message) ||
        `HTTP ${primary.status || 'network error'}`;

    logFallbackEvent(
        reason,
        OPENROUTER_CONFIG.primaryModel,
        OPENROUTER_CONFIG.fallbackModel
    );

    // ── Attempt 2: Fallback model ────────────────────────────────────────
    const fallback = await _fetchCompletion(
        OPENROUTER_CONFIG.fallbackModel,
        prompt,
        history,
        apiKey
    );

    if (fallback.ok && fallback.data && fallback.data.choices && fallback.data.choices.length > 0) {
        return {
            success: true,
            content: fallback.data.choices[0].message.content,
            model: OPENROUTER_CONFIG.fallbackModel,
            fallbackUsed: true,
            error: null,
        };
    }

    // ── Both models failed ───────────────────────────────────────────────
    const fallbackErr =
        (fallback.data && fallback.data.error && fallback.data.error.message) ||
        `Fallback also failed (HTTP ${fallback.status || 'network error'})`;

    return {
        success: false,
        content: '',
        model: OPENROUTER_CONFIG.fallbackModel,
        fallbackUsed: true,
        error: `Primary model unavailable. Fallback error: ${fallbackErr}`,
    };
}

// ─── Dashboard Helper: render *table notation to HTML ────────────────────────

/**
 * Convert the *table … *end notation used by the AI into an HTML <table>.
 * This keeps the dashboard rendering intact regardless of model output.
 */
function renderTableNotation(text) {
    if (!text) return '';

    return text.replace(
        /\*table\s*\n([\s\S]*?)\*end/gi,
        function (_, tableBody) {
            const lines = tableBody
                .split('\n')
                .map((l) => l.trim())
                .filter((l) => l.length > 0);

            if (lines.length === 0) return '';

            let html = '<div class="table-responsive"><table class="ai-accounting-table">';
            let headerDone = false;

            for (const line of lines) {
                if (line.match(/^-+$/)) {
                    // separator row — skip (already used to delimit header)
                    headerDone = true;
                    continue;
                }

                const cells = line.split('|').map((c) => c.trim());
                const tag = headerDone ? 'td' : 'th';

                html += '<tr>';
                for (const cell of cells) {
                    html += `<${tag}>${cell}</${tag}>`;
                }
                html += '</tr>';

                if (!headerDone) headerDone = true; // first row is always header
            }

            html += '</table></div>';
            return html;
        }
    );
}
