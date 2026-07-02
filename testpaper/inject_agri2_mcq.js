/**
 * inject_agri2_mcq.js
 * 
 * Production-grade injection script for Agriculture 2nd Paper MCQs.
 * Reads from: Agri2_all_ch_mcq - Sheet1.csv
 * Injects into: data.js (agr2 section only)
 * 
 * Features:
 * - Dynamic ID generation (max existing + 1)
 * - Roman-item formatting
 * - Agricultural terminology preservation
 * - UTF-8 safe
 * - Backup before write
 * - Syntax validation via Node.js
 * - Zero data corruption
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// ─── PATHS ───────────────────────────────────────────────────────────────────
const CSV_PATH = path.join(__dirname, 'Agri2_all_ch_mcq - Sheet1.csv');
const DATA_JS_PATH = path.join(__dirname, 'data.js');
const BACKUP_PATH = DATA_JS_PATH + '.bak_agri2_mcq';

// ─── CHAPTER NAME MAPPING ───────────────────────────────────────────────────
const CHAPTER_NAMES = {
    "1": "Chapter 1 : Fish Farming",
    "2": "Chapter 2 : Poultry Rearing",
    "3": "Chapter 3 : Animal Husbandry",
    "4": "Chapter 4 : Afforestation",
    "5": "Chapter 5 : Agricultural Economics and Cooperatives (Out of Short Syllabus)"
};

// ─── ANSWER MAPPING ──────────────────────────────────────────────────────────
const ANSWER_MAP = { 'a': 0, 'b': 1, 'c': 2, 'd': 3 };

// ─── CSV PARSER ──────────────────────────────────────────────────────────────
function parseCSV(csvText) {
    const rows = [];
    let inQuotes = false;
    const lines = csvText.split('\n');
    let fullLine = '';

    for (let i = 0; i < lines.length; i++) {
        let line = lines[i];
        // Remove trailing \r
        if (line.endsWith('\r')) line = line.slice(0, -1);

        if (!inQuotes) {
            fullLine = line;
        } else {
            fullLine += '\n' + line;
        }

        // Count quotes
        let quoteCount = 0;
        for (const ch of fullLine) {
            if (ch === '"') quoteCount++;
        }

        if (quoteCount % 2 !== 0) {
            // Odd number of quotes — we're inside a quoted field spanning lines
            inQuotes = true;
            continue;
        }

        inQuotes = false;
        rows.push(parseCSVLine(fullLine));
        fullLine = '';
    }

    return rows;
}

function parseCSVLine(line) {
    const fields = [];
    let current = '';
    let inQuotes = false;

    for (let i = 0; i < line.length; i++) {
        const ch = line[i];
        if (inQuotes) {
            if (ch === '"') {
                if (i + 1 < line.length && line[i + 1] === '"') {
                    current += '"';
                    i++; // skip escaped quote
                } else {
                    inQuotes = false;
                }
            } else {
                current += ch;
            }
        } else {
            if (ch === '"') {
                inQuotes = true;
            } else if (ch === ',') {
                fields.push(current);
                current = '';
            } else {
                current += ch;
            }
        }
    }
    fields.push(current);
    return fields;
}

// ─── TEXT NORMALIZATION ──────────────────────────────────────────────────────
function normalizeText(text) {
    if (!text) return '';
    let t = text.trim();
    // Normalize duplicate spaces (but not inside HTML tags)
    t = t.replace(/  +/g, ' ');
    // Normalize excessive blank lines
    t = t.replace(/\n{3,}/g, '\n\n');
    return t;
}

// ─── ROMAN ITEM FORMATTING ──────────────────────────────────────────────────
function formatRomanItems(text) {
    if (!text) return text;

    // Detect if we have consecutive Roman items like (i) / (ii) / (iii) or i. / ii. / iii.
    let normalized = text;

    const parenRegex = /\((i{1,3}v?|iv|v|vi{0,3})\)/g;
    const dotRegex = /\b(i{1,3}v?|iv|v|vi{0,3})\./g;
    
    let matchType = null;
    let matches = [];
    
    let parenMatches = [...normalized.matchAll(parenRegex)];
    if (parenMatches.length >= 2 && parenMatches[0][1] === 'i' && parenMatches[1][1] === 'ii') {
        matchType = 'paren';
        matches = parenMatches;
    } else {
        let dotMatches = [...normalized.matchAll(dotRegex)];
        if (dotMatches.length >= 2 && dotMatches[0][1] === 'i' && dotMatches[1][1] === 'ii') {
            matchType = 'dot';
            matches = dotMatches;
        }
    }
    
    if (matchType && matches.length >= 2) {
        const startIdx = matches[0].index;
        const questionPart = normalized.substring(0, startIdx).trim();
        const itemsPart = normalized.substring(startIdx);
        
        const delimiterRegex = matchType === 'paren' ? /\s*\((i{1,3}v?|iv|v|vi{0,3})\)\s*/g : /\s*\b(i{1,3}v?|iv|v|vi{0,3})\.\s*/g;
        
        const splitParts = itemsPart.split(delimiterRegex);
        const items = [];
        for (let i = 1; i < splitParts.length; i += 2) {
            const roman = splitParts[i];
            let content = splitParts[i+1] || '';
            
            if (i + 2 >= splitParts.length) {
                // Last item
                const qMatch = content.match(/\s*(Which of the following|Q\b|\?)/i);
                if (qMatch) {
                    const idx = qMatch.index;
                    const itemContent = content.substring(0, idx).trim();
                    const trailingQuestion = content.substring(idx).trim();
                    items.push(matchType === 'paren' ? `(${roman}) ${itemContent}` : `(${roman}) ${itemContent}`); // Format dot as (i) as requested
                    
                    const formattedItems = items.join('<br>\n');
                    const htmlBlock = `\n\n<p class="ml-4 my-2 text-gray-600 dark:text-gray-400">\n${formattedItems}\n</p>\n\n`;
                    
                    let result = questionPart;
                    if (result) result += '\n\n';
                    result += htmlBlock;
                    if (trailingQuestion) result += trailingQuestion;
                    return result;
                }
            }
            // Standardize output format to use paren (i) for Roman items
            items.push(`(${roman}) ${content.trim()}`);
        }
        
        const formattedItems = items.join('<br>\n');
        const htmlBlock = `\n\n<p class="ml-4 my-2 text-gray-600 dark:text-gray-400">\n${formattedItems}\n</p>`;
        
        return questionPart ? (questionPart + htmlBlock) : htmlBlock;
    }
    
    return text;
}

// ─── QUESTION TEXT FORMATTING ────────────────────────────────────────────────
function formatQuestionText(rawText) {
    if (!rawText) return '<p></p>';
    
    let text = normalizeText(rawText);
    
    // Apply Roman item formatting
    text = formatRomanItems(text);
    
    // If text already contains HTML tags, preserve them
    if (text.includes('<p') || text.includes('<table') || text.includes('<div')) {
        return text;
    }
    
    // Convert \n\n to paragraph breaks
    if (text.includes('\n\n')) {
        const paragraphs = text.split('\n\n').map(p => p.trim()).filter(p => p);
        const formatted = paragraphs.map(p => {
            if (p.startsWith('<p') || p.startsWith('<table') || p.startsWith('<div')) {
                return p;
            }
            return `<p>${p}</p>`;
        });
        return formatted.join('');
    }
    
    // Wrap in <p> if not already
    if (!text.startsWith('<')) {
        return `<p>${text}</p>`;
    }
    
    return text;
}

// ─── EXPLANATION FORMATTING ──────────────────────────────────────────────────
function formatExplanation(rawText) {
    if (!rawText) return '';
    
    let text = normalizeText(rawText);
    
    // If already contains HTML, preserve it
    if (text.includes('<p') || text.includes('<table')) {
        return text;
    }
    
    // Convert \n\n to <br><br> within a <p>
    text = text.replace(/\n\n/g, '<br><br>');
    // Convert single \n to <br>
    text = text.replace(/\n/g, '<br>');
    
    return `<p>${text}</p>`;
}

// ─── ESCAPE FOR JS STRING ───────────────────────────────────────────────────
function escapeForJS(str) {
    if (!str) return '';
    return str
        .replace(/\\/g, '\\\\')
        .replace(/"/g, '\\"')
        .replace(/\n/g, '\\n')
        .replace(/\r/g, '')
        .replace(/\t/g, '\\t');
}

// ─── FIND MAX NUMERIC ID IN data.js ─────────────────────────────────────────
function findMaxMCQId(content) {
    const regex = /"?id"?\s*:\s*(\d+)/g;
    let maxId = 0;
    let match;
    while ((match = regex.exec(content)) !== null) {
        const id = parseInt(match[1], 10);
        if (id > maxId) maxId = id;
    }
    return maxId;
}

// ─── FIND AGR1 BLOCK BOUNDARIES ─────────────────────────────────────────────
function findAgr1Block(content) {
    const startMatch = content.match(/"agr1"\s*:\s*\{/);
    if (!startMatch) {
        throw new Error('Could not find "agr1" key in data.js');
    }
    
    const keyStart = startMatch.index;
    const braceStart = content.indexOf('{', keyStart + 5);
    
    let braceCount = 0;
    let endPos = -1;
    for (let i = braceStart; i < content.length; i++) {
        if (content[i] === '{') braceCount++;
        else if (content[i] === '}') {
            braceCount--;
            if (braceCount === 0) {
                endPos = i + 1;
                break;
            }
        }
    }
    
    if (endPos === -1) {
        throw new Error('Could not find matching closing brace for agr1 block');
    }
    
    return { keyStart, braceStart, endPos };
}

// ─── BUILD MCQ OBJECT STRING ────────────────────────────────────────────────
function buildMCQString(mcq, indent) {
    const pad = ' '.repeat(indent);
    const pad2 = ' '.repeat(indent + 4);
    
    let str = `${pad}{\n`;
    str += `${pad2}"id": ${mcq.id},\n`;
    str += `${pad2}"text": "${escapeForJS(mcq.text)}",\n`;
    str += `${pad2}"meta": "${escapeForJS(mcq.meta)}",\n`;
    str += `${pad2}"type": "${escapeForJS(mcq.type)}",\n`;
    str += `${pad2}"options": [\n`;
    for (let i = 0; i < mcq.options.length; i++) {
        const comma = i < mcq.options.length - 1 ? ',' : '';
        str += `${pad2}    "${escapeForJS(mcq.options[i])}"${comma}\n`;
    }
    str += `${pad2}],\n`;
    str += `${pad2}"correctAnswer": ${mcq.correctAnswer},\n`;
    str += `${pad2}"explanation": "${escapeForJS(mcq.explanation)}"\n`;
    str += `${pad}}`;
    return str;
}

// ─── BUILD CHAPTER BLOCK STRING ─────────────────────────────────────────────
function buildChapterBlock(chapterNum, mcqs) {
    const chapterName = CHAPTER_NAMES[chapterNum] || `Chapter ${chapterNum}`;
    
    let str = `        "${chapterNum}": {\n`;
    str += `            "subjectName": "Agriculture 2nd Paper",\n`;
    str += `            "chapterName": "${escapeForJS(chapterName)}",\n`;
    str += `            "mcqData": [\n`;
    
    for (let i = 0; i < mcqs.length; i++) {
        str += buildMCQString(mcqs[i], 16);
        if (i < mcqs.length - 1) str += ',';
        str += '\n';
    }
    
    str += `            ],\n`;
    str += `            "shortCQData": [],\n`;
    str += `            "fullCQData": []\n`;
    str += `        }`;
    
    return str;
}

// ─── MAIN ────────────────────────────────────────────────────────────────────
function main() {
    console.log('=== AGR2 MCQ INJECTION SCRIPT ===\n');
    
    // 1. Read CSV
    console.log('1. Reading CSV file...');
    if (!fs.existsSync(CSV_PATH)) {
        console.error(`FATAL: CSV file not found: ${CSV_PATH}`);
        process.exit(1);
    }
    const csvRaw = fs.readFileSync(CSV_PATH, 'utf-8');
    const csvRows = parseCSV(csvRaw);
    
    if (csvRows.length < 2) {
        console.error('FATAL: CSV file appears empty or has no data rows.');
        process.exit(1);
    }
    
    const headers = csvRows[0];
    console.log(`   Headers: ${headers.join(', ')}`);
    console.log(`   Total data rows: ${csvRows.length - 1}`);
    
    // Validate headers
    const expectedHeaders = ['Year', 'Subject', 'Chapter', 'Level', 'Category', 'Question', 'Option A', 'Option B', 'Option C', 'Option D', 'Correct Answer', 'Explanation'];
    for (const h of expectedHeaders) {
        if (!headers.includes(h)) {
            console.error(`FATAL: Missing expected column: "${h}"`);
            process.exit(1);
        }
    }
    
    const colIdx = {};
    for (const h of expectedHeaders) {
        colIdx[h] = headers.indexOf(h);
    }
    
    // 2. Read data.js
    console.log('\n2. Reading data.js...');
    if (!fs.existsSync(DATA_JS_PATH)) {
        console.error(`FATAL: data.js not found: ${DATA_JS_PATH}`);
        process.exit(1);
    }
    const dataJsContent = fs.readFileSync(DATA_JS_PATH, 'utf-8');
    console.log(`   File size: ${dataJsContent.length} characters`);
    
    // 3. Find max existing MCQ ID
    console.log('\n3. Finding max existing MCQ ID...');
    const maxExistingId = findMaxMCQId(dataJsContent);
    console.log(`   Max existing MCQ ID: ${maxExistingId}`);
    let nextId = maxExistingId + 1;
    console.log(`   Starting ID for new MCQs: ${nextId}`);
    
    // 4. Find agr1 block to place agr2 right after it
    console.log('\n4. Locating agr1 block end in data.js...');
    const { keyStart, braceStart, endPos } = findAgr1Block(dataJsContent);
    console.log(`   agr1 block: ends at index ${endPos}`);
    
    // 5. Parse CSV into chapter-grouped MCQs
    console.log('\n5. Parsing CSV data into MCQ objects...');
    const chapterMCQs = {};
    let parseErrors = [];
    let totalParsed = 0;
    
    for (let rowIdx = 1; rowIdx < csvRows.length; rowIdx++) {
        const row = csvRows[rowIdx];
        
        // Skip empty rows
        if (!row || row.length < expectedHeaders.length || !row[colIdx['Question']]) {
            continue;
        }
        
        const chapter = (row[colIdx['Chapter']] || '').trim();
        const question = (row[colIdx['Question']] || '').trim();
        const optionA = (row[colIdx['Option A']] || '').trim();
        const optionB = (row[colIdx['Option B']] || '').trim();
        const optionC = (row[colIdx['Option C']] || '').trim();
        const optionD = (row[colIdx['Option D']] || '').trim();
        const correctAnswer = (row[colIdx['Correct Answer']] || '').trim().toLowerCase();
        const explanation = (row[colIdx['Explanation']] || '').trim();
        const level = (row[colIdx['Level']] || '').trim();
        const category = (row[colIdx['Category']] || '').trim();
        const year = (row[colIdx['Year']] || '').trim();
        
        // Validate chapter
        if (!chapter || !CHAPTER_NAMES[chapter]) {
            parseErrors.push(`Row ${rowIdx + 1}: Invalid chapter "${chapter}"`);
            continue;
        }
        
        // Validate options
        if (!optionA || !optionB || !optionC || !optionD) {
            parseErrors.push(`Row ${rowIdx + 1}: Missing option(s) in chapter ${chapter}`);
            continue;
        }
        
        // Validate correct answer
        if (!ANSWER_MAP.hasOwnProperty(correctAnswer)) {
            parseErrors.push(`Row ${rowIdx + 1}: Invalid correct answer "${correctAnswer}" (expected a/b/c/d)`);
            continue;
        }
        
        // Build meta string
        let meta = '';
        if (level && year) {
            meta = `${level} · ${year}`;
        } else if (level) {
            meta = level;
        } else if (year) {
            meta = year;
        } else {
            meta = 'HSC Standard · General Practice';
        }
        
        // Build type
        let type = 'general practice';
        if (category) {
            const catLower = category.toLowerCase();
            if (catLower === 'board') type = 'board';
            else if (catLower === 'college') type = 'college';
            else type = catLower;
        }
        
        const formattedText = formatQuestionText(question);
        const formattedExplanation = formatExplanation(explanation);
        
        const mcq = {
            id: nextId++,
            text: formattedText,
            meta: meta,
            type: type,
            options: [optionA, optionB, optionC, optionD],
            correctAnswer: ANSWER_MAP[correctAnswer],
            explanation: formattedExplanation
        };
        
        if (!chapterMCQs[chapter]) chapterMCQs[chapter] = [];
        chapterMCQs[chapter].push(mcq);
        totalParsed++;
    }
    
    console.log(`   Total MCQs parsed: ${totalParsed}`);
    console.log(`   Chapters with MCQs: ${Object.keys(chapterMCQs).sort((a,b) => parseInt(a) - parseInt(b)).join(', ')}`);
    
    for (const ch of Object.keys(chapterMCQs).sort((a,b) => parseInt(a) - parseInt(b))) {
        console.log(`     Chapter ${ch}: ${chapterMCQs[ch].length} MCQs`);
    }
    
    if (parseErrors.length > 0) {
        console.log(`\n   ⚠ Parse warnings (${parseErrors.length}):`);
        for (const err of parseErrors.slice(0, 10)) {
            console.log(`     ${err}`);
        }
    }
    
    if (totalParsed === 0) {
        console.error('\nFATAL: No MCQs were parsed. Aborting.');
        process.exit(1);
    }
    
    // 6. Validate
    console.log('\n6. Validating all MCQs...');
    const idSet = new Set();
    let validationErrors = [];
    
    for (const ch of Object.keys(chapterMCQs)) {
        for (const mcq of chapterMCQs[ch]) {
            if (idSet.has(mcq.id)) {
                validationErrors.push(`Duplicate ID: ${mcq.id}`);
            }
            idSet.add(mcq.id);
            
            if (mcq.options.length !== 4) {
                validationErrors.push(`ID ${mcq.id}: Expected 4 options, got ${mcq.options.length}`);
            }
            
            if (mcq.correctAnswer < 0 || mcq.correctAnswer > 3) {
                validationErrors.push(`ID ${mcq.id}: correctAnswer ${mcq.correctAnswer} out of range`);
            }
        }
    }
    
    if (validationErrors.length > 0) {
        console.error(`\n   VALIDATION ERRORS (${validationErrors.length}):`);
        for (const err of validationErrors) {
            console.error(`     ${err}`);
        }
        console.error('\nFATAL: Validation failed. Aborting.');
        process.exit(1);
    }
    console.log('   ✓ All MCQs validated successfully.');
    
    // 7. Build the new agr2 block
    console.log('\n7. Building new agr2 block...');
    let agr2Block = `    "agr2": {\n`;
    const sortedChapters = Object.keys(chapterMCQs).sort((a, b) => parseInt(a) - parseInt(b));
    for (let i = 0; i < sortedChapters.length; i++) {
        const ch = sortedChapters[i];
        agr2Block += buildChapterBlock(ch, chapterMCQs[ch]);
        if (i < sortedChapters.length - 1) {
            agr2Block += ',';
        }
        agr2Block += '\n';
    }
    agr2Block += `    }`;
    
    // 8. Reconstruct data.js
    console.log('\n8. Reconstructing data.js...');
    const newContent = dataJsContent.substring(0, endPos) + ',\n\n' + agr2Block + dataJsContent.substring(endPos);
    console.log(`   New file size: ${newContent.length} characters`);
    
    // 9. Write to temp file and validate syntax
    console.log('\n9. Writing to temp file and validating syntax...');
    const tempPath = DATA_JS_PATH + '.temp_agr2.js';
    fs.writeFileSync(tempPath, newContent, 'utf-8');
    
    try {
        execSync(`node -c "${tempPath}"`, { encoding: 'utf-8', stdio: 'pipe' });
        console.log('   ✓ Syntax validation PASSED');
    } catch (err) {
        console.error('   ✗ SYNTAX ERROR in generated file:');
        console.error(err.stderr || err.message);
        fs.unlinkSync(tempPath);
        process.exit(1);
    }
    
    // 10. Backup and finalize
    console.log('\n10. Creating backup and finalizing...');
    if (!fs.existsSync(BACKUP_PATH)) {
        fs.copyFileSync(DATA_JS_PATH, BACKUP_PATH);
        console.log(`   ✓ Backup created: ${BACKUP_PATH}`);
    } else {
        console.log(`   ℹ Backup already exists: ${BACKUP_PATH}`);
    }
    
    fs.renameSync(tempPath, DATA_JS_PATH);
    console.log('   ✓ data.js updated successfully!');
    console.log('\n========================================');
    console.log(`Successfully injected ${totalParsed} MCQs into testDatabase.agr2!`);
    console.log('========================================');
}

main();
