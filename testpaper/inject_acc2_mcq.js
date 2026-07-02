/**
 * inject_acc2_mcq.js
 * 
 * Production-grade injection script for Accounting 2nd Paper MCQs.
 * Reads from: Acc2_all_ch_mcq - Sheet1.csv
 * Injects into: data.js (acc2 section only)
 * 
 * Features:
 * - Dynamic ID generation (max existing + 1)
 * - Roman-item formatting
 * - Accounting formula preservation
 * - UTF-8 safe
 * - Backup before write
 * - Syntax validation via Node.js
 * - Zero data corruption
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// ─── PATHS ───────────────────────────────────────────────────────────────────
const CSV_PATH = path.join(__dirname, 'Acc2_all_ch_mcq - Sheet1.csv');
const DATA_JS_PATH = path.join(__dirname, 'data.js');
const BACKUP_PATH = DATA_JS_PATH + '.bak_acc2_mcq';

// ─── CHAPTER NAME MAPPING ───────────────────────────────────────────────────
const CHAPTER_NAMES = {
    "1": "Chapter 1 : Accounts of Not-for-Profit Organizations",
    "2": "Chapter 2 : Partnership Business Accounts",
    "3": "Chapter 3 : Cash Flow Statement",
    "4": "Chapter 4: Capital of Joint Stock Companies",
    "5": "Chapter 5 : Financial Statements of Joint Stock Companies",
    "6": "Chapter 6 : Financial Statement Analysis",
    "7": "Chapter 7 : Cost Accounting",
    "8": "Chapter 8 : Accounting for Inventory",
    "9": "Chapter 9 : Cost and Classification of Cost",
    "10": "Chapter 10 : Introduction to Management Accounting"
};

// ─── ANSWER MAPPING ──────────────────────────────────────────────────────────
const ANSWER_MAP = { 'a': 0, 'b': 1, 'c': 2, 'd': 3 };

// ─── CSV PARSER ──────────────────────────────────────────────────────────────
function parseCSV(csvText) {
    const rows = [];
    let current = '';
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

    // Pattern 1: (i) Item1 (ii) Item2 ...  or  (i) Item1\n(ii) Item2\n...
    // Pattern 2: i. Item1 ii. Item2 ...
    // Only when 2+ consecutive items detected

    // Detect pattern: (i) ... (ii) ... (iii) ... (iv) ...
    const romanParenPattern = /\(i\)\s+.+?\s+\(ii\)\s+/;
    // Detect pattern: i. ... ii. ... iii. ...
    const romanDotPattern = /\bi\.\s+.+?\s+ii\.\s+/;

    if (romanParenPattern.test(text) || romanDotPattern.test(text)) {
        // Extract the question part (before the Roman items) and the items
        // Handle (i)/(ii)/(iii)/(iv) pattern
        let match = text.match(/^(.*?)(\(i\)\s+.+)$/s);
        if (match) {
            const questionPart = match[1].trim();
            const itemsPart = match[2].trim();
            
            // Split on (i), (ii), (iii), (iv) boundaries
            const items = [];
            const itemRegex = /\((i{1,3}v?|iv|v|vi{0,3})\)\s+/g;
            let lastIndex = 0;
            let m;
            const positions = [];
            
            while ((m = itemRegex.exec(itemsPart)) !== null) {
                positions.push({ index: m.index, length: m[0].length, marker: m[0].trim() });
            }
            
            if (positions.length >= 2) {
                for (let i = 0; i < positions.length; i++) {
                    const start = positions[i].index;
                    const end = i + 1 < positions.length ? positions[i + 1].index : itemsPart.length;
                    const itemText = itemsPart.substring(start, end).trim();
                    items.push(itemText);
                }
                
                const formattedItems = items.join('<br>');
                const htmlBlock = `<p class="ml-4 my-2 text-gray-600 dark:text-gray-400">${formattedItems}</p>`;
                
                if (questionPart) {
                    return questionPart + htmlBlock;
                } else {
                    return htmlBlock;
                }
            }
        }

        // Handle i./ii./iii. pattern
        match = text.match(/^(.*?)\bi\.\s+(.+)$/s);
        if (match) {
            const questionPart = match[1].trim();
            const itemsPart = 'i. ' + match[2].trim();
            
            const items = [];
            const itemRegex = /\b(i{1,3}v?|iv|v|vi{0,3})\.\s+/g;
            let m2;
            const positions = [];
            
            while ((m2 = itemRegex.exec(itemsPart)) !== null) {
                positions.push({ index: m2.index, length: m2[0].length, marker: m2[0].trim() });
            }
            
            if (positions.length >= 2) {
                for (let i = 0; i < positions.length; i++) {
                    const start = positions[i].index;
                    const end = i + 1 < positions.length ? positions[i + 1].index : itemsPart.length;
                    items.push(itemsPart.substring(start, end).trim());
                }
                
                const formattedItems = items.join('<br>');
                const htmlBlock = `<p class="ml-4 my-2 text-gray-600 dark:text-gray-400">${formattedItems}</p>`;
                
                if (questionPart) {
                    return questionPart + htmlBlock;
                } else {
                    return htmlBlock;
                }
            }
        }
    }

    // Also handle newline-separated Roman items already present
    // e.g. \n(i) Item1\n(ii) Item2\n(iii) Item3
    const newlineRomanPattern = /\n\(i\)\s+/;
    if (newlineRomanPattern.test(text)) {
        const parts = text.split(/\n(?=\(i\)\s)/);
        if (parts.length === 2) {
            const questionPart = parts[0].trim();
            const itemsPart = parts[1].trim();
            
            // Split items by newline
            const itemLines = itemsPart.split('\n').map(l => l.trim()).filter(l => l);
            
            if (itemLines.length >= 2) {
                const formattedItems = itemLines.join('<br>');
                const htmlBlock = `<p class="ml-4 my-2 text-gray-600 dark:text-gray-400">${formattedItems}</p>`;
                return questionPart + htmlBlock;
            }
        }
    }

    // Handle \n\ni. / \n\nii. patterns
    const newlineDotPattern = /\n\ni\.\s+/;
    if (newlineDotPattern.test(text)) {
        const parts = text.split(/\n\n(?=i\.\s)/);
        if (parts.length === 2) {
            const questionPart = parts[0].trim();
            const itemsPart = parts[1].trim();
            const itemLines = itemsPart.split('\n').map(l => l.trim()).filter(l => l);
            
            if (itemLines.length >= 2) {
                const formattedItems = itemLines.join('<br>');
                const htmlBlock = `<p class="ml-4 my-2 text-gray-600 dark:text-gray-400">${formattedItems}</p>`;
                return questionPart + htmlBlock;
            }
        }
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
        // Check if any paragraph already has HTML
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
    const regex = /"id"\s*:\s*(\d+)/g;
    let maxId = 0;
    let match;
    while ((match = regex.exec(content)) !== null) {
        const id = parseInt(match[1], 10);
        if (id > maxId) maxId = id;
    }
    return maxId;
}

// ─── FIND ACC2 BLOCK BOUNDARIES ─────────────────────────────────────────────
function findAcc2Block(content) {
    const startMatch = content.match(/"acc2"\s*:\s*\{/);
    if (!startMatch) {
        throw new Error('Could not find "acc2" key in data.js');
    }
    
    const keyStart = startMatch.index; // Start of "acc2": {
    const braceStart = content.indexOf('{', keyStart + 5); // The opening brace
    
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
        throw new Error('Could not find matching closing brace for acc2 block');
    }
    
    return { keyStart, braceStart, endPos };
}

// ─── PARSE EXISTING ACC2 CHAPTERS ───────────────────────────────────────────
function parseExistingAcc2Chapters(content, braceStart, endPos) {
    const acc2Content = content.substring(braceStart, endPos);
    
    // Find all chapter keys like "2": {, "4": {
    const chapterRegex = /"(\d+)"\s*:\s*\{/g;
    const chapters = {};
    let m;
    while ((m = chapterRegex.exec(acc2Content)) !== null) {
        chapters[m[1]] = true;
    }
    return Object.keys(chapters);
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
    
    let str = `    "${chapterNum}": {\n`;
    str += `        "subjectName": "Accounting 2nd Paper",\n`;
    str += `        "chapterName": "${escapeForJS(chapterName)}",\n`;
    str += `        "mcqData": [\n`;
    
    for (let i = 0; i < mcqs.length; i++) {
        str += buildMCQString(mcqs[i], 12);
        if (i < mcqs.length - 1) str += ',';
        str += '\n';
    }
    
    str += `        ],\n`;
    str += `        "shortCQData": [],\n`;
    str += `        "fullCQData": []\n`;
    str += `    }`;
    
    return str;
}

// ─── MAIN ────────────────────────────────────────────────────────────────────
function main() {
    console.log('=== ACC2 MCQ INJECTION SCRIPT ===\n');
    
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
    
    // Validate header columns
    const expectedHeaders = ['Year', 'Subject', 'Chapter', 'Level', 'Category', 'Question', 'Option A', 'Option B', 'Option C', 'Option D', 'Correct Answer', 'Explanation'];
    for (const h of expectedHeaders) {
        if (!headers.includes(h)) {
            console.error(`FATAL: Missing expected column: "${h}"`);
            process.exit(1);
        }
    }
    
    // Column indices
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
    
    // 4. Find acc2 block
    console.log('\n4. Locating acc2 block in data.js...');
    const { keyStart, braceStart, endPos } = findAcc2Block(dataJsContent);
    console.log(`   acc2 block: chars ${keyStart} to ${endPos}`);
    
    const existingChapters = parseExistingAcc2Chapters(dataJsContent, braceStart, endPos);
    console.log(`   Existing acc2 chapters: ${existingChapters.join(', ')}`);
    
    // 5. Parse CSV into chapter-grouped MCQs
    console.log('\n5. Parsing CSV data into MCQ objects...');
    const chapterMCQs = {}; // { "1": [mcq, ...], "2": [...], ... }
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
        
        // Validate question
        if (!question) {
            parseErrors.push(`Row ${rowIdx + 1}: Empty question in chapter ${chapter}`);
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
        
        // Format question text
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
        for (const err of parseErrors.slice(0, 20)) {
            console.log(`     ${err}`);
        }
        if (parseErrors.length > 20) {
            console.log(`     ... and ${parseErrors.length - 20} more`);
        }
    }
    
    if (totalParsed === 0) {
        console.error('\nFATAL: No MCQs were parsed. Aborting.');
        process.exit(1);
    }
    
    // 6. Validate all MCQs
    console.log('\n6. Validating all MCQs...');
    const idSet = new Set();
    let validationErrors = [];
    
    for (const ch of Object.keys(chapterMCQs)) {
        for (const mcq of chapterMCQs[ch]) {
            // Check for duplicate IDs
            if (idSet.has(mcq.id)) {
                validationErrors.push(`Duplicate ID: ${mcq.id} in chapter ${ch}`);
            }
            idSet.add(mcq.id);
            
            // Check options count
            if (mcq.options.length !== 4) {
                validationErrors.push(`ID ${mcq.id}: Expected 4 options, got ${mcq.options.length}`);
            }
            
            // Check correctAnswer range
            if (mcq.correctAnswer < 0 || mcq.correctAnswer > 3) {
                validationErrors.push(`ID ${mcq.id}: correctAnswer ${mcq.correctAnswer} out of range`);
            }
            
            // Check question is not empty
            if (!mcq.text || mcq.text === '<p></p>') {
                validationErrors.push(`ID ${mcq.id}: Empty question text`);
            }
        }
    }
    
    // Check sequential IDs
    const allIds = Array.from(idSet).sort((a, b) => a - b);
    for (let i = 1; i < allIds.length; i++) {
        if (allIds[i] !== allIds[i - 1] + 1) {
            validationErrors.push(`Non-sequential IDs: gap between ${allIds[i - 1]} and ${allIds[i]}`);
        }
    }
    
    if (validationErrors.length > 0) {
        console.error(`\n   VALIDATION ERRORS (${validationErrors.length}):`);
        for (const err of validationErrors) {
            console.error(`     ${err}`);
        }
        console.error('\nFATAL: Validation failed. Aborting injection.');
        process.exit(1);
    }
    console.log('   ✓ All MCQs validated successfully.');
    console.log(`   ID range: ${allIds[0]} to ${allIds[allIds.length - 1]}`);
    
    // 7. Build the new acc2 block
    console.log('\n7. Building new acc2 block...');
    
    // We need to reconstruct the acc2 object.
    // Strategy: Parse existing acc2 block content, inject mcqData into existing chapters,
    // and create new chapter blocks for chapters that don't exist yet.
    
    const acc2Block = dataJsContent.substring(braceStart, endPos);
    
    // For existing chapters (2, 4): We need to replace their empty mcqData: [] with the new data
    // For new chapters (1, 3, 5, 6, 7, 8, 9, 10): We need to add new chapter blocks
    
    let newAcc2Content = acc2Block;
    
    // First, inject MCQs into existing chapters that have empty mcqData
    for (const existingCh of existingChapters) {
        if (chapterMCQs[existingCh] && chapterMCQs[existingCh].length > 0) {
            console.log(`   Injecting ${chapterMCQs[existingCh].length} MCQs into existing chapter ${existingCh}...`);
            
            // Find the "mcqData": [] in this chapter's block
            // We need to find the specific chapter's mcqData
            const chapterKeyPattern = new RegExp(`"${existingCh}"\\s*:\\s*\\{`);
            const chapterMatch = chapterKeyPattern.exec(newAcc2Content);
            
            if (chapterMatch) {
                // Find mcqData: [] after this chapter key
                const afterChapterKey = newAcc2Content.indexOf('"mcqData"', chapterMatch.index);
                if (afterChapterKey !== -1) {
                    // Find the opening [ of mcqData
                    const mcqArrayStart = newAcc2Content.indexOf('[', afterChapterKey);
                    if (mcqArrayStart !== -1) {
                        // Find the matching ]
                        let bracketCount = 0;
                        let mcqArrayEnd = -1;
                        for (let i = mcqArrayStart; i < newAcc2Content.length; i++) {
                            if (newAcc2Content[i] === '[') bracketCount++;
                            else if (newAcc2Content[i] === ']') {
                                bracketCount--;
                                if (bracketCount === 0) {
                                    mcqArrayEnd = i + 1;
                                    break;
                                }
                            }
                        }
                        
                        if (mcqArrayEnd !== -1) {
                            // Build the MCQ array content
                            let mcqArrayStr = '[\n';
                            const mcqs = chapterMCQs[existingCh];
                            for (let i = 0; i < mcqs.length; i++) {
                                mcqArrayStr += buildMCQString(mcqs[i], 12);
                                if (i < mcqs.length - 1) mcqArrayStr += ',';
                                mcqArrayStr += '\n';
                            }
                            mcqArrayStr += '        ]';
                            
                            // Replace
                            newAcc2Content = newAcc2Content.substring(0, mcqArrayStart) + mcqArrayStr + newAcc2Content.substring(mcqArrayEnd);
                        }
                    }
                }
            }
        }
    }
    
    // Now add new chapters that don't exist yet
    const newChapters = Object.keys(chapterMCQs)
        .filter(ch => !existingChapters.includes(ch))
        .sort((a, b) => parseInt(a) - parseInt(b));
    
    if (newChapters.length > 0) {
        console.log(`   Creating ${newChapters.length} new chapter blocks: ${newChapters.join(', ')}`);
        
        // Find the position just before the closing } of acc2
        // The acc2 block is: { "2": {...}, "4": {...} }
        // We need to insert new chapters before the final }
        
        // Find the last } in newAcc2Content
        let lastBrace = newAcc2Content.lastIndexOf('}');
        // But the last } is the acc2's closing brace.
        // We need to go back one more to find the last chapter's closing brace
        // Actually, we need to insert a comma after the last existing chapter and then add new chapters
        
        // Strategy: find the second-to-last } (end of last chapter), add comma + new chapters
        // Actually let's be more careful. Let's find where the last chapter block ends.
        
        // The structure is: { "2": { ... }, "4": { ... } }
        // We need to insert after the last chapter's } and before the final }
        
        // Let's find the last chapter's closing position
        // Find the closing brace of acc2 (which is the last char)
        const acc2ClosingBrace = newAcc2Content.length - 1; // Should be '}'
        
        // Build new chapter strings
        let newChapterStr = '';
        for (const ch of newChapters) {
            newChapterStr += ',\n' + buildChapterBlock(ch, chapterMCQs[ch]);
        }
        
        // Insert before the closing brace
        newAcc2Content = newAcc2Content.substring(0, acc2ClosingBrace) + newChapterStr + '\n' + newAcc2Content.substring(acc2ClosingBrace);
    }
    
    // 8. Reconstruct data.js with the new acc2 block
    console.log('\n8. Reconstructing data.js...');
    
    // Check what comes after the acc2 block
    const afterAcc2 = dataJsContent.substring(endPos).trimStart();
    const hasTrailingComma = afterAcc2.startsWith(',');
    
    let newContent;
    if (hasTrailingComma) {
        // acc2 block was followed by a comma — replace acc2 block only
        newContent = dataJsContent.substring(0, braceStart) + newAcc2Content + dataJsContent.substring(endPos);
    } else {
        // Check if original had a comma between acc2 and next block
        // Looking at the original: the acc2 ends with },\n\n    "ict":
        // So the comma is part of the content between endPos and the next key
        newContent = dataJsContent.substring(0, braceStart) + newAcc2Content + dataJsContent.substring(endPos);
    }
    
    console.log(`   New file size: ${newContent.length} characters`);
    
    // 9. Write to temp file and validate syntax
    console.log('\n9. Writing to temp file and validating syntax...');
    const tempPath = DATA_JS_PATH + '.temp_acc2.js';
    fs.writeFileSync(tempPath, newContent, 'utf-8');
    
    try {
        execSync(`node -c "${tempPath}"`, { encoding: 'utf-8', stdio: 'pipe' });
        console.log('   ✓ Syntax validation PASSED');
    } catch (err) {
        console.error('   ✗ SYNTAX ERROR in generated file:');
        console.error(err.stderr || err.message);
        
        // Clean up temp file
        fs.unlinkSync(tempPath);
        
        console.error('\nFATAL: Syntax validation failed. Aborting injection.');
        console.error('No changes have been made to data.js.');
        process.exit(1);
    }
    
    // 10. Create backup and finalize
    console.log('\n10. Creating backup and finalizing...');
    
    if (!fs.existsSync(BACKUP_PATH)) {
        fs.copyFileSync(DATA_JS_PATH, BACKUP_PATH);
        console.log(`   ✓ Backup created: ${BACKUP_PATH}`);
    } else {
        console.log(`   ℹ Backup already exists: ${BACKUP_PATH}`);
    }
    
    // Replace data.js with the validated temp file
    fs.renameSync(tempPath, DATA_JS_PATH);
    console.log('   ✓ data.js updated successfully!');
    
    // 11. Final summary
    console.log('\n════════════════════════════════════════════════');
    console.log('  INJECTION SUMMARY');
    console.log('════════════════════════════════════════════════');
    console.log(`  Total MCQs injected: ${totalParsed}`);
    console.log(`  ID range: ${allIds[0]} – ${allIds[allIds.length - 1]}`);
    console.log(`  Chapters modified: ${existingChapters.filter(ch => chapterMCQs[ch]).join(', ') || 'none'}`);
    console.log(`  Chapters created: ${newChapters.join(', ') || 'none'}`);
    console.log('  Backup: ' + BACKUP_PATH);
    console.log('  Status: ✓ SUCCESS');
    console.log('════════════════════════════════════════════════');
}

// Run
main();
