const fs = require('fs');
const path = require('path');

const inputPath = path.join(__dirname, 'Acc2_ch1_cq - Sheet1.csv');
const outputPath = path.join(__dirname, 'Acc2_ch1_cq_clean.csv');

const COLUMNS = [
    "Year", "Subject", "Chapter", "Level", "Category", "Stem",
    "Question_A", "Question_B", "Question_C",
    "Ans_A", "Ans_B", "Ans_C",
];

function isSeparator(line) {
    const core = line.replace(/[-=|:\s]/g, "");
    return line.trim().length > 0 && core.length === 0;
}

function simpleStrip(text) {
    return text.replace(/\*\*/g, "").replace(/__/g, "").replace(/`/g, "").replace(/\$/g, "");
}

function pipeRow(line) {
    const cells = line.split("|").map(c => simpleStrip(c.trim())).filter(c => c);
    return cells.join(" | ");
}

function cellToPlain(raw) {
    if (!raw) return "";
    const lines = raw.replace(/\r\n/g, "\n").replace(/\r/g, "\n").split("\n");
    const parts = [];
    for (const line of lines) {
        const s = line.trim();
        if (!s || isSeparator(s)) continue;
        let part = s.includes("|") ? pipeRow(s) : simpleStrip(s);
        part = part.trim();
        if (part) parts.push(part);
    }
    const result = parts.join(" // ");
    return result.replace(/[ \t]{2,}/g, " ").trim();
}

function parseCSVLine(line) {
    const result = [];
    let current = '';
    let inQuotes = false;
    for (let i = 0; i < line.length; i++) {
        const char = line[i];
        if (char === '"') {
            if (inQuotes && line[i+1] === '"') {
                current += '"';
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (char === ',' && !inQuotes) {
            result.push(current);
            current = '';
        } else {
            current += char;
        }
    }
    result.push(current);
    return result;
}

function main() {
    console.log("Reading raw file...");
    const raw = fs.readFileSync(inputPath, 'utf8');
    
    const lines = raw.split("\n");
    const rows = [];
    let currentRow = "";
    
    for (const line of lines) {
        if (/^(201[0-9]|202[0-9]),/.test(line) || /^Year,Subject/.test(line)) {
            if (currentRow) rows.push(currentRow);
            currentRow = line;
        } else {
            currentRow += "\n" + line;
        }
    }
    if (currentRow) rows.push(currentRow);
    
    console.log(`Detected ${rows.length} rows.`);
    
    const cleaned = [];
    for (let i = 1; i < rows.length; i++) { // Skip header
        let r = rows[i];
        if ((r.match(/"/g) || []).length % 2 !== 0) {
            r += '"';
        }
        const cols = parseCSVLine(r);
        while(cols.length < 12) cols.push("");
        
        const cleanCols = cols.slice(0, 12).map(c => cellToPlain(c));
        cleaned.push(cleanCols);
    }
    
    console.log("Writing output...");
    let outCsv = COLUMNS.map(c => `"${c}"`).join(",") + "\n";
    for (const row of cleaned) {
        outCsv += row.map(c => `"${c.replace(/"/g, '""')}"`).join(",") + "\n";
    }
    
    fs.writeFileSync(outputPath, outCsv, 'utf8');
    console.log("Done!");
}

main();
