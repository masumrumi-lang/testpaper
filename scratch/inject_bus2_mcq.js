const fs = require('fs');
const path = require('path');

const csvPath = 'c:\\Users\\BMTF\\.antigravity\\testpaper\\Bus2_all_ch_mcq - Sheet1.csv';
const dbPath = 'c:\\Users\\BMTF\\.antigravity\\testpaper\\data.js';
const backupPath = dbPath + '.bak_bus2_mcq';

// Simple CSV parser that handles quotes and commas correctly
function parseCSV(content) {
    const lines = [];
    let row = [];
    let col = '';
    let inQuotes = false;
    
    for (let i = 0; i < content.length; i++) {
        const char = content[i];
        const nextChar = content[i + 1];
        
        if (inQuotes) {
            if (char === '"') {
                if (nextChar === '"') {
                    col += '"';
                    i++; // Skip next quote
                } else {
                    inQuotes = false;
                }
            } else {
                col += char;
            }
        } else {
            if (char === '"') {
                inQuotes = true;
            } else if (char === ',') {
                row.push(col);
                col = '';
            } else if (char === '\r' || char === '\n') {
                if (char === '\r' && nextChar === '\n') {
                    i++;
                }
                row.push(col);
                lines.push(row);
                row = [];
                col = '';
            } else {
                col += char;
            }
        }
    }
    if (row.length > 0 || col !== '') {
        row.push(col);
        lines.push(row);
    }
    
    const headers = lines[0].map(h => h.trim());
    const data = [];
    for (let i = 1; i < lines.length; i++) {
        const r = lines[i];
        if (r.length < headers.length) continue;
        const obj = {};
        headers.forEach((h, idx) => {
            obj[h] = r[idx] ? r[idx].trim() : '';
        });
        
        if (Object.values(obj).some(v => v !== '')) {
            data.push(obj);
        }
    }
    return data;
}

// Roman item text normalizer
function parseRomanQuestion(text) {
    // 1. Remove duplicate spaces and excessive blank lines
    text = text.replace(/\s+/g, ' ').trim();

    // 2. Identify Roman numerals. We check for standard patterns.
    const markerSets = [
        { type: 'paren', items: ['(i)', '(ii)', '(iii)', '(iv)', '(v)'] },
        { type: 'dot', items: ['i.', 'ii.', 'iii.', 'iv.', 'v.'] },
        { type: 'comma', items: ['i,', 'ii,', 'iii,', 'iv,', 'v,'] }
    ];

    let foundSet = null;
    let positions = [];

    for (const set of markerSets) {
        const p = [];
        const idx0 = text.toLowerCase().indexOf(set.items[0]);
        const idx1 = text.toLowerCase().indexOf(set.items[1]);
        if (idx0 !== -1 && idx1 !== -1 && idx0 < idx1) {
            p.push(idx0);
            p.push(idx1);
            for (let k = 2; k < set.items.length; k++) {
                const idxK = text.toLowerCase().indexOf(set.items[k]);
                if (idxK !== -1 && idxK > p[p.length - 1]) {
                    p.push(idxK);
                } else {
                    break;
                }
            }
            if (p.length >= 2) {
                foundSet = set;
                positions = p;
                break;
            }
        }
    }

    if (!foundSet) {
        return wrapInP(text);
    }

    const stem = text.slice(0, positions[0]).trim();
    const items = [];
    for (let i = 0; i < positions.length; i++) {
        const start = positions[i] + foundSet.items[i].length;
        const end = (i + 1 < positions.length) ? positions[i + 1] : text.length;
        let itemText = text.slice(start, end).trim();
        items.push(itemText);
    }

    let suffix = "";
    let lastItem = items[items.length - 1];
    const suffixRegex = /(Which\s+(?:one|of\s+the\s+following)\s+is\s+correct\??)/i;
    const match = lastItem.match(suffixRegex);
    if (match) {
        const index = match.index;
        suffix = lastItem.slice(index).trim();
        items[items.length - 1] = lastItem.slice(0, index).trim();
    }

    let html = "";
    if (stem) {
        html += wrapInP(stem);
    }
    
    const formattedItems = items.map((item, idx) => {
        let cleaned = item.replace(/^[,.\s]+|[,.\s]+$/g, '').trim();
        return `(${romanChar(idx + 1)}) ${cleaned}`;
    }).join('<br>');

    html += `<p class='ml-4 my-2 text-gray-600 dark:text-gray-400'>${formattedItems}</p>`;

    if (suffix) {
        html += wrapInP(suffix);
    }

    return html;
}

function romanChar(num) {
    const chars = ['', 'i', 'ii', 'iii', 'iv', 'v'];
    return chars[num] || '';
}

function wrapInP(text) {
    if (!text) return '';
    if (text.startsWith('<p>') && text.endsWith('</p>')) {
        return text;
    }
    if (text.includes('<p>') || text.includes('</div>') || text.includes('<br>')) {
        return text; // already has HTML
    }
    return `<p>${text}</p>`;
}

function run() {
    console.log("Creating backup copy of data.js...");
    fs.copyFileSync(dbPath, backupPath);
    console.log(`Backup created successfully at: ${backupPath}`);

    console.log("Reading data.js...");
    const dbContent = fs.readFileSync(dbPath, 'utf8');

    // 1. Determine maximum MCQ ID dynamically
    const idRegex = /(?:"id"|id)\s*:\s*(\d+)/g;
    let match;
    let maxId = 0;
    while ((match = idRegex.exec(dbContent)) !== null) {
        const idVal = parseInt(match[1], 10);
        if (idVal > maxId) {
            maxId = idVal;
        }
    }
    console.log(`Current maximum MCQ ID: ${maxId}`);
    let nextId = maxId + 1;
    console.log(`Next assigned MCQ ID will start from: ${nextId}`);

    // 2. Parse CSV
    console.log("Reading and parsing CSV...");
    const csvContent = fs.readFileSync(csvPath, 'utf8');
    const rawMcqs = parseCSV(csvContent);
    console.log(`Parsed ${rawMcqs.length} raw MCQs from CSV.`);

    // 3. Extract bus2 block
    const startIdx = dbContent.indexOf('"bus2":');
    if (startIdx === -1) {
        throw new Error("Could not find 'bus2' block in data.js");
    }

    let braceCount = 0;
    let foundFirstBrace = false;
    let endIdx = -1;
    for (let i = startIdx; i < dbContent.length; i++) {
        const char = dbContent[i];
        if (char === '{') {
            braceCount++;
            foundFirstBrace = true;
        } else if (char === '}') {
            braceCount--;
            if (foundFirstBrace && braceCount === 0) {
                endIdx = i + 1;
                break;
            }
        }
    }

    if (endIdx === -1) {
        throw new Error("Could not find matching closing brace for 'bus2'");
    }

    const bus2BlockStr = dbContent.slice(startIdx, endIdx);
    const jsonStr = bus2BlockStr.split(':').slice(1).join(':').trim();
    
    // Evaluate bus2 block to JS object
    const bus2Data = (new Function(`return ${jsonStr}`))();
    console.log("Successfully parsed bus2 block from data.js.");

    // Map correct answer option key
    const ansMap = { a: 0, b: 1, c: 2, d: 3 };

    // Group new MCQs by Chapter
    const newMcqsByChapter = {};
    for (let ch = 1; ch <= 10; ch++) {
        newMcqsByChapter[ch] = [];
    }

    rawMcqs.forEach((row, index) => {
        const rowNum = index + 2;
        let chStr = (row['Chapter'] || '').trim();
        
        // Map "Controlling" to 10
        if (chStr.toLowerCase() === 'controlling') {
            chStr = '10';
        }
        
        const ch = parseInt(chStr, 10);
        if (isNaN(ch) || ch < 1 || ch > 10) {
            console.warn(`Row ${rowNum}: Invalid chapter "${row['Chapter']}". Skipping.`);
            return;
        }

        const question = parseRomanQuestion(row['Question'] || '');
        const ansChar = (row['Correct Answer'] || '').toLowerCase().trim();
        const correctAnswer = ansMap[ansChar];
        if (correctAnswer === undefined) {
            throw new Error(`Row ${rowNum}: Invalid Correct Answer "${row['Correct Answer']}"`);
        }

        const options = [
            (row['Option A'] || '').trim(),
            (row['Option B'] || '').trim(),
            (row['Option C'] || '').trim(),
            (row['Option D'] || '').trim()
        ];

        // Validate exactly 4 non-empty options
        if (options.some(opt => opt === '')) {
            throw new Error(`Row ${rowNum}: Options contain empty strings.`);
        }

        const level = (row['Level'] || '').trim();
        const year = (row['Year'] || '').trim();
        const meta = `${level} · ${year}`;
        const type = (row['Category'] || '').trim().toLowerCase();
        
        let explanation = '';
        if (row['Explanation']) {
            explanation = wrapInP(row['Explanation'].trim());
        }

        const id = nextId++;

        newMcqsByChapter[ch].push({
            id,
            text: question,
            meta,
            type,
            options,
            correctAnswer,
            explanation
        });
    });

    // Validations & Injection
    console.log("\n--- RUNNING PRE-INJECTION VALIDATIONS ---");
    const newIds = new Set();
    let totalInjected = 0;
    
    for (let ch = 1; ch <= 10; ch++) {
        const mcqs = newMcqsByChapter[ch];
        const originalCount = bus2Data[ch.toString()].mcqData ? bus2Data[ch.toString()].mcqData.length : 0;
        console.log(`Chapter ${ch}: existing=${originalCount}, parsed from CSV=${mcqs.length}`);
        
        if (mcqs.length === 0) {
            throw new Error(`Validation Error: Chapter ${ch} received 0 MCQs from CSV.`);
        }

        mcqs.forEach(mcq => {
            // Verify fields
            if (!mcq.id || !mcq.text || !mcq.options || mcq.options.length !== 4 || mcq.correctAnswer === undefined) {
                throw new Error(`Validation Error: MCQ ID ${mcq.id} has invalid structure.`);
            }
            // Verify correct answer references existing option
            if (mcq.correctAnswer < 0 || mcq.correctAnswer > 3) {
                throw new Error(`Validation Error: MCQ ID ${mcq.id} has invalid correctAnswer index.`);
            }
            // Verify duplicate IDs
            if (newIds.has(mcq.id)) {
                throw new Error(`Validation Error: Duplicate ID ${mcq.id} detected.`);
            }
            newIds.add(mcq.id);
        });

        // Set the new mcqData array
        bus2Data[ch.toString()].mcqData = mcqs;
        totalInjected += mcqs.length;
    }

    console.log("[OK] Pre-injection validations passed successfully!");
    console.log(`Total MCQs to inject: ${totalInjected}`);

    // Re-serialize the bus2 block
    const serializedBus2 = JSON.stringify(bus2Data, null, 4);
    
    // Replace in dbContent
    const updatedDbContent = dbContent.slice(0, startIdx) + `"bus2": ` + serializedBus2 + dbContent.slice(endIdx);
    
    // Write back to data.js
    console.log("Writing updated database to data.js...");
    fs.writeFileSync(dbPath, updatedDbContent, 'utf8');
    console.log("[OK] Injected successfully!");
}

try {
    run();
} catch (e) {
    console.error("FAILED EXECUTION:", e);
    process.exit(1);
}
