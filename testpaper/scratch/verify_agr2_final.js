const fs = require('fs');
const content = fs.readFileSync('data.js', 'utf-8');

// Extract agr2 block
const agr2Start = content.indexOf('"agr2"');
console.log('agr2 starts at:', agr2Start);

// Find end of agr2 block by brace matching
const braceStart = content.indexOf('{', agr2Start + 6);
let depth = 0;
let agr2End = -1;
for (let i = braceStart; i < content.length; i++) {
    if (content[i] === '{') depth++;
    else if (content[i] === '}') {
        depth--;
        if (depth === 0) { agr2End = i + 1; break; }
    }
}
console.log('agr2 ends at:', agr2End);

const agr2Block = content.substring(agr2Start, agr2End);

// Count IDs
const idMatches = [...agr2Block.matchAll(/"id":\s*(\d+)/g)];
console.log('\nTotal MCQs:', idMatches.length);
console.log('ID range:', idMatches[0][1], '-', idMatches[idMatches.length-1][1]);

// Count options arrays
const optionsBlocks = [...agr2Block.matchAll(/"options":\s*\[([\s\S]*?)\]/g)];
console.log('Options arrays found:', optionsBlocks.length);

// Verify each has 4 options (count string entries by looking for quoted strings)
let badOptions = 0;
for (let i = 0; i < optionsBlocks.length; i++) {
    const block = optionsBlocks[i][1];
    // Count the quoted strings that are option values (line-by-line)
    const lines = block.split('\n').filter(l => l.trim() && l.trim().startsWith('"'));
    if (lines.length !== 4) {
        badOptions++;
        if (badOptions <= 5) {
            console.log(`  WARNING: MCQ index ${i} (ID: ${idMatches[i]?.[1]}) has ${lines.length} options`);
        }
    }
}
if (badOptions === 0) {
    console.log('  [OK] All MCQs have exactly 4 options');
} else {
    console.log(`  [FAIL] ${badOptions} MCQs have wrong option count`);
}

// Verify correctAnswer values
const correctAnswers = [...agr2Block.matchAll(/"correctAnswer":\s*(\d+)/g)];
console.log('\ncorrectAnswer values found:', correctAnswers.length);
const badAnswers = correctAnswers.filter(m => parseInt(m[1]) < 0 || parseInt(m[1]) > 3);
if (badAnswers.length === 0) {
    console.log('  [OK] All correctAnswer values are 0-3');
} else {
    console.log(`  [FAIL] ${badAnswers.length} bad correctAnswer values`);
}

// Count chapters
const chapters = [...agr2Block.matchAll(/"subjectName":\s*"Agriculture 2nd Paper"/g)];
console.log('\nChapter blocks:', chapters.length);

// Count per chapter key
for (let ch = 1; ch <= 5; ch++) {
    const chKey = `"${ch}": {`;
    if (agr2Block.includes(chKey)) {
        const chStart = agr2Block.indexOf(chKey);
        let chDepth = 0;
        let chEnd = -1;
        const chBraceStart = agr2Block.indexOf('{', chStart + chKey.length - 1);
        for (let i = chBraceStart; i < agr2Block.length; i++) {
            if (agr2Block[i] === '{') chDepth++;
            else if (agr2Block[i] === '}') {
                chDepth--;
                if (chDepth === 0) { chEnd = i + 1; break; }
            }
        }
        const chBlock = agr2Block.substring(chStart, chEnd);
        const chIds = [...chBlock.matchAll(/"id":\s*(\d+)/g)];
        console.log(`  Chapter ${ch}: ${chIds.length} MCQs (IDs: ${chIds[0][1]}-${chIds[chIds.length-1][1]})`);
    } else {
        console.log(`  Chapter ${ch}: NOT FOUND`);
    }
}

// Overall syntax
console.log('\n[OK] data.js syntax already validated by node -c during injection');
console.log('\n======== FINAL VERDICT ========');
if (badOptions === 0 && badAnswers.length === 0 && idMatches.length === 217) {
    console.log('PASS: All 217 MCQs injected correctly with proper format');
} else {
    console.log('ISSUES FOUND - review above');
}
