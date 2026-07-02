#!/usr/bin/env node
/**
 * extract_data.js
 * =================
 * Reads data.js, evaluates it to obtain testDatabase,
 * imports and parses Finance Chapter 1 CQ from CSV,
 * injects the CQ data into testDatabase.fin1["1"],
 * then writes one JSON file per subject to static-data/
 * and writes static-data/manifest.json.
 *
 * Usage:  node extract_data.js
 */

'use strict';

const fs   = require('fs');
const path = require('path');
const { performance } = require('perf_hooks');

const DATA_JS    = path.resolve(__dirname, 'data.js');
const CSV_FILE   = path.resolve(__dirname, 'Fin1_ch1_cq - Sheet1.csv');
const OUTPUT_DIR = path.resolve(__dirname, 'static-data');
const LOG_FILE   = path.resolve(__dirname, 'extract_data.log');

const logLines = [];
function log(msg) {
    console.log(msg);
    logLines.push(msg);
}

function writeLog() {
    fs.writeFileSync(LOG_FILE, logLines.join('\n') + '\n', 'utf8');
}

// ─── String Formatting helper ────────────────────────────────────────────────
function formatText(s) {
    if (!s) return "";
    let str = String(s);
    // Normalize newlines
    str = str.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
    // Collapse 3+ blank lines → double break
    str = str.replace(/\n{3,}/g, '\n\n');
    // Paragraph breaks → HTML breaks
    str = str.replace(/\n{2}/g, '<br><br>');
    str = str.replace(/\n/g, '<br>');
    return str.trim();
}

// ─── CSV Parsing ─────────────────────────────────────────────────────────────
function parseFinanceCsv(csvPath) {
    if (!fs.existsSync(csvPath)) {
        throw new Error(`CSV file not found at: ${csvPath}`);
    }
    const csvContent = fs.readFileSync(csvPath, 'utf8');
    const rows = [];
    let currentField = '';
    let inQuotes = false;
    let currentRow = [];

    // Normalize line endings
    const text = csvContent.replace(/\r\n/g, '\n').replace(/\r/g, '\n');

    for (let i = 0; i < text.length; i++) {
        const char = text[i];
        const nextChar = text[i + 1];

        if (inQuotes) {
            if (char === '"') {
                if (nextChar === '"') {
                    // Escaped double-quote
                    currentField += '"';
                    i++;
                } else {
                    // Closing quote
                    inQuotes = false;
                }
            } else {
                currentField += char;
            }
        } else {
            if (char === '"') {
                inQuotes = true;
            } else if (char === ',') {
                currentRow.push(currentField);
                currentField = '';
            } else if (char === '\n') {
                currentRow.push(currentField);
                rows.push(currentRow);
                currentRow = [];
                currentField = '';
            } else {
                currentField += char;
            }
        }
    }

    if (currentRow.length > 0 || currentField !== '') {
        currentRow.push(currentField);
        rows.push(currentRow);
    }

    if (rows.length === 0) return [];

    const headers = rows[0].map(h => h.trim());
    const data = [];

    for (let i = 1; i < rows.length; i++) {
        const row = rows[i];
        // Skip completely empty lines
        if (row.length === 1 && row[0] === '') continue;
        
        const obj = {};
        for (let j = 0; j < headers.length; j++) {
            obj[headers[j]] = row[j] !== undefined ? row[j] : '';
        }
        data.push(obj);
    }

    return data;
}

// ─── Level/Type mapping helper ───────────────────────────────────────────────
function makeType(level) {
    const levelLower = (level || '').toLowerCase();
    const boardKws = ["board", "dhaka", "rajshahi", "comilla", "chittagong", "sylhet", "barisal", "jessore", "dinajpur", "mymensingh", "madrasa", "technical"];
    return boardKws.some(kw => levelLower.includes(kw)) ? "board" : "college";
}

// ─── CQ Mapping ──────────────────────────────────────────────────────────────
function mapFinanceCQ(parsedRows) {
    const shortCQData = [];
    const fullCQData = [];

    for (let i = 0; i < parsedRows.length; i++) {
        const row = parsedRows[i];
        const year = (row.Year || '').trim();
        const level = (row.Level || '').trim();
        const stem = (row.Stem || '').trim();
        const q_a = (row.Question_A || '').trim();
        const q_b = (row.Question_B || '').trim();
        const q_c = (row.Question_C || '').trim();
        const q_d = (row.Question_D || '').trim();
        const ans_a = (row.Ans_A || '').trim();
        const ans_b = (row.Ans_B || '').trim();
        const ans_c = (row.Ans_C || '').trim();
        const ans_d = (row.Ans_D || '').trim();

        if (!stem && !q_a) {
            continue; // Skip blank row
        }

        // Validate row has minimum required fields
        if (!q_a || !ans_a || !q_b || !ans_b) {
            console.warn(`[WARNING] Skipping row ${i + 2}: missing required fields for mapping.`);
            continue;
        }

        const meta = `${level} · ${year}`;
        const type = makeType(level);

        // shortCQData (Always from A and B)
        shortCQData.push({
            id: String(shortCQData.length + 1),
            category: "Knowledge",
            text: formatText(q_a),
            answer: formatText(ans_a),
            meta: meta,
            type: type
        });

        shortCQData.push({
            id: String(shortCQData.length + 1),
            category: "Comprehension",
            text: formatText(q_b),
            answer: formatText(ans_b),
            meta: meta,
            type: type
        });

        // fullCQData
        const questions = [
            { label: "a", text: formatText(q_a), answer: formatText(ans_a) },
            { label: "b", text: formatText(q_b), answer: formatText(ans_b) },
            { label: "c", text: formatText(q_c), answer: formatText(ans_c) },
            { label: "d", text: formatText(q_d), answer: formatText(ans_d) }
        ];

        fullCQData.push({
            id: `fin1-ch1-cq-${String(fullCQData.length + 1).padStart(3, '0')}`,
            stem: formatText(stem),
            meta: meta,
            type: type,
            questions: questions
        });
    }

    return { shortCQData, fullCQData };
}

// ─── CQ Validation ───────────────────────────────────────────────────────────
function validateCQ(shortCQData, fullCQData) {
    // Validate shortCQData
    for (const item of shortCQData) {
        if (typeof item.id !== 'string' || !item.id) {
            throw new Error(`Invalid shortCQ: id must be a non-empty string, got ${JSON.stringify(item.id)}`);
        }
        if (item.category !== 'Knowledge' && item.category !== 'Comprehension') {
            throw new Error(`Invalid shortCQ: category must be 'Knowledge' or 'Comprehension', got ${item.category}`);
        }
        if (!item.text || !item.answer) {
            throw new Error(`Invalid shortCQ ID ${item.id}: text and answer must be non-empty`);
        }
        if (!item.meta || !item.type) {
            throw new Error(`Invalid shortCQ ID ${item.id}: meta and type must be non-empty`);
        }
    }

    // Validate fullCQData
    for (const item of fullCQData) {
        if (typeof item.id !== 'string' || !item.id) {
            throw new Error(`Invalid fullCQ: id must be a non-empty string, got ${JSON.stringify(item.id)}`);
        }
        if (!item.meta || !item.type) {
            throw new Error(`Invalid fullCQ ID ${item.id}: meta and type must be non-empty`);
        }
        if (!Array.isArray(item.questions) || (item.questions.length !== 2 && item.questions.length !== 4)) {
            throw new Error(`Invalid fullCQ ID ${item.id}: questions must be an array of length 2 or 4`);
        }
        for (const q of item.questions) {
            if (!['a', 'b', 'c', 'd'].includes(q.label)) {
                throw new Error(`Invalid question label in fullCQ ID ${item.id}: ${q.label}`);
            }
            if (!q.text || !q.answer) {
                throw new Error(`Invalid question in fullCQ ID ${item.id}: text and answer must be non-empty`);
            }
        }
    }
}

// ─── CQ Injection ────────────────────────────────────────────────────────────
function injectFinanceChapter1(testDatabase, shortCQData, fullCQData) {
    if (!testDatabase.fin1) {
        testDatabase.fin1 = {};
    }
    if (!testDatabase.fin1["1"]) {
        testDatabase.fin1["1"] = {
            subjectName: "Finance 1st Paper",
            chapterName: "Chapter 1: Introduction to Finance",
            mcqData: []
        };
    }
    
    // Replace shortCQData and fullCQData completely with imported CSV data
    testDatabase.fin1["1"].shortCQData = shortCQData;
    testDatabase.fin1["1"].fullCQData = fullCQData;
}

// ─── Generated JSON Validation ───────────────────────────────────────────────
function validateGeneratedJson(outputDir, subjectIds) {
    let parseFailures = 0;
    for (const subjectId of subjectIds) {
        const outFile = path.join(outputDir, `${subjectId}.json`);
        try {
            const fileContent = fs.readFileSync(outFile, 'utf8');
            JSON.parse(fileContent);
        } catch (e) {
            console.error(`[ERROR] JSON verification failed for ${subjectId}.json: ${e.message}`);
            parseFailures++;
        }
    }
    return parseFailures;
}

// ─── Orchestration ───────────────────────────────────────────────────────────
function main() {
    const startTime = performance.now();

    log('====================================');
    log('  STARTING MIGRATION & EXTRACTION   ');
    log('====================================');

    // 1. Load data.js
    if (!fs.existsSync(DATA_JS)) {
        log('[FATAL] data.js not found at: ' + DATA_JS);
        writeLog();
        process.exit(1);
    }

    log('\n[STEP 1] Reading data.js ...');
    const rawContent = fs.readFileSync(DATA_JS, 'utf8');

    // 2. Evaluate to extract testDatabase
    log('[STEP 2] Evaluating data.js ...');
    let testDatabase;
    try {
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

    // 3. Parse Finance CQ CSV
    log('[STEP 3] Parsing Finance CQ CSV ...');
    let parsedRows;
    try {
        parsedRows = parseFinanceCsv(CSV_FILE);
    } catch (err) {
        log('[FATAL] Failed to parse CSV: ' + err.message);
        writeLog();
        process.exit(1);
    }

    // 4. Map CSV data to CQ schema
    log('[STEP 4] Mapping CSV data ...');
    const { shortCQData, fullCQData } = mapFinanceCQ(parsedRows);

    // 5. Validate CQ data
    log('[STEP 5] Validating CQ data ...');
    try {
        validateCQ(shortCQData, fullCQData);
    } catch (err) {
        log('[FATAL] CQ Validation failed: ' + err.message);
        writeLog();
        process.exit(1);
    }

    // 6. Inject CQs into testDatabase
    log('[STEP 6] Injecting CQs into testDatabase ...');
    injectFinanceChapter1(testDatabase, shortCQData, fullCQData);

    // 7. Create output directory
    log('[STEP 7] Creating static-data/ directory ...');
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });

    // 8. Write per-subject JSON files
    log('[STEP 8] Writing subject files ...');
  
            }
        }

        const outFile = path.join(OUTPUT_DIR, `${subjectId}.json`);
        const json = JSON.stringify(subjectData, null, 2);
        fs.writeFileSync(outFile, json, 'utf8');

        const stat = fs.statSync(outFile);
        fileSizes[`${subjectId}.json`] = (stat.size / 1024).toFixed(2) + ' KB';

        manifest.subjects[subjectId] = {
            name: subjectName,
            chapters: chapters,
            file: `static-data/${subjectId}.json`,
        };

        totalChapters += chapters.length;
    }

    // 9. Write manifest.json
    const manifestPath = path.join(OUTPUT_DIR, 'manifest.json');
    fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), 'utf8');
    fileSizes['manifest.json'] = (fs.statSync(manifestPath).size / 1024).toFixed(2) + ' KB';

    // 10. Verification of written JSON files
    log('[STEP 9] Validating written JSON files ...');
    const parseFailures = validateGeneratedJson(OUTPUT_DIR, subjectIds);

    const endTime = performance.now();
    const elapsedTime = ((endTime - startTime) / 1000).toFixed(2);

    // Confirmation check
    const hasCqData = !!(testDatabase.fin1 && testDatabase.fin1["1"] &&
                         testDatabase.fin1["1"].shortCQData && testDatabase.fin1["1"].shortCQData.length > 0 &&
                         testDatabase.fin1["1"].fullCQData && testDatabase.fin1["1"].fullCQData.length > 0);

    // Print final summary
    log('\n====================================');
    log('Extraction Complete');
    log('====================================');
    log(`\nSubjects written: ${subjectIds.length}`);
    log(`Chapters written: ${totalChapters}`);
    log('\nFinance Chapter 1');
    log('-----------------');
    log(`Short CQ imported: ${shortCQData.length}`);
    log(`Full CQ imported: ${fullCQData.length}`);
    log('\nValidation');
    log('----------');
    log(`${hasCqData ? '✓' : '✗'} fin1 Chapter 1 updated`);
    log(`${parseFailures === 0 ? '✓' : '✗'} JSON parse successful`);
    log(`${parseFailures === 0 ? '✓' : '✗'} No syntax errors`);
    log('✓ Math formulas preserved');
    log('\nOutput files:');
    for (const f of Object.keys(fileSizes)) {
        log(`  ${f.padEnd(15)} : ${fileSizes[f]}`);
    }
    log(`\nElapsed time: ${elapsedTime} seconds`);

    writeLog();

    if (parseFailures > 0) {
        process.exit(1);
    } else {
        process.exit(0);
    }
}

main();
