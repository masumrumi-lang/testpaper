const fs = require('fs');
const glob = require('glob');

function bnToEnDigits(bnStr) {
    const mapping = { '০': '0', '১': '1', '২': '2', '৩': '3', '৪': '4', '৫': '5', '৬': '6', '৭': '7', '৮': '8', '৯': '9' };
    return bnStr.replace(/[০-৯]/g, m => mapping[m]);
}

function extractNumbers(text) {
    const enText = bnToEnDigits(text);
    const matches = enText.match(/\b\d{2,}\b/g) || [];
    return new Set(matches);
}

// Parse Bengali questions
const rawBn = fs.readFileSync('raw_board.txt', 'utf-8');
const bnBlocks = rawBn.trim().split(/\n(?=\d{2}\nQuestion \d{2})/);
const bnQuestions = [];

bnBlocks.forEach(block => {
    const lines = block.trim().split('\n');
    if (lines.length < 3) return;
    const qNum = lines[0].trim();
    
    const metaMatch = block.match(/([A-Za-z]+)\s*·\s*(\d{4})/);
    const meta = metaMatch ? `${metaMatch[1]} ${metaMatch[2]}` : "";
    const nums = extractNumbers(block);
    
    bnQuestions.push({ id: qNum, meta, nums, block });
});

// Parse English questions
const enQuestions = [];
const files = fs.readdirSync('.').filter(f => f.startsWith('fullCQ_board_part') && f.endsWith('.js')).sort();

files.forEach(file => {
    const content = fs.readFileSync(file, 'utf-8');
    const regex = /{\s*id:\s*"(\d+)",\s*stem:\s*"(.*?)",\s*meta:\s*"(.*?)",\s*questions:\s*\[([\s\S]*?)\]\s*}/g;
    let match;
    while ((match = regex.exec(content)) !== null) {
        const id = match[1];
        const stem = match[2];
        const metaRaw = match[3].replace(//g, '').replace(/\s+/g, ' ').trim();
        const questionsBlock = match[4];
        
        const nums = extractNumbers(stem + ' ' + questionsBlock);
        
        enQuestions.push({
            id: id,
            meta: metaRaw,
            nums: nums,
            block: match[0]
        });
    }
});

let matched = 0;
const unmatched = [];

bnQuestions.forEach(bn => {
    let bestMatch = null;
    let bestScore = 0;
    
    const bnMetaBoard = bn.meta.split(' ')[0] || "";
    const bnMetaYear = bn.meta.split(' ')[1] || "";
    
    enQuestions.forEach(en => {
        const enMetaParts = en.meta.split(' ');
        const enMetaBoard = enMetaParts[0] || "";
        const enMetaYear = enMetaParts[enMetaParts.length - 1] || "";
        
        if (bnMetaYear !== enMetaYear) return;
        if (bnMetaBoard !== enMetaBoard) return;
        
        let common = 0;
        for (let num of bn.nums) {
            if (en.nums.has(num)) common++;
        }
        
        if (common > bestScore) {
            bestScore = common;
            bestMatch = en;
        }
    });
    
    if (bestMatch && bestScore > 1) { // at least 2 numbers in common
        matched++;
        // Save matched to file
        fs.appendFileSync('matched_questions.js', `// Matched BN ID ${bn.id} with EN ID ${bestMatch.id}\n${bestMatch.block},\n\n`);
    } else {
        unmatched.push(bn.id);
        fs.appendFileSync('unmatched_questions.js', `// Unmatched BN ID ${bn.id}\n/*\n${bn.block}\n*/\n\n`);
    }
});

console.log(`Matched: ${matched}/${bnQuestions.length}`);
console.log(`Unmatched IDs: ${unmatched.join(', ')}`);
