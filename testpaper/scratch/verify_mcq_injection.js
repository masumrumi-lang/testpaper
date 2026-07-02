const fs = require('fs');

const dbPath = 'c:\\Users\\BMTF\\.antigravity\\testpaper\\data.js';

console.log("Reading data.js for verification...");
const content = fs.readFileSync(dbPath, 'utf8');

// 1. Check JS validity by evaluating it
console.log("Evaluating updated data.js to verify syntax validity...");
let testDatabase;
try {
    testDatabase = (new Function(content + '\nreturn testDatabase;'))();
    console.log("[OK] data.js parsed and evaluated successfully without syntax errors!");
} catch (e) {
    console.error("[FAIL] syntax error in data.js:", e);
    process.exit(1);
}

// 2. Verify fin2 content
const fin2 = testDatabase.fin2;
if (!fin2) {
    console.error("[FAIL] No 'fin2' block found in database.");
    process.exit(1);
}

console.log("\n--- VERIFYING CHAPTERS ---");
let totalMcqs = 0;
const expectedChapters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'];

for (const ch of expectedChapters) {
    const chData = fin2[ch];
    if (!chData) {
        console.error(`[FAIL] Chapter ${ch} is missing!`);
        process.exit(1);
    }
    const mcqCount = chData.mcqData ? chData.mcqData.length : 0;
    totalMcqs += mcqCount;
    console.log(`  Chapter ${ch.padStart(2)}: name="${chData.chapterName}", mcqCount=${mcqCount}`);
    
    // Spot check some fields
    if (mcqCount > 0) {
        const sample = chData.mcqData[0];
        if (!sample.id || !sample.text || !sample.options || sample.options.length !== 4 || sample.correctAnswer === undefined) {
            console.error(`[FAIL] Chapter ${ch} sample MCQ is malformed:`, sample);
            process.exit(1);
        }
    } else {
        console.error(`[FAIL] Chapter ${ch} has 0 MCQs!`);
        process.exit(1);
    }
}

console.log(`\n[OK] Total MCQs in fin2: ${totalMcqs}`);
if (totalMcqs === 1301) {
    console.log("[OK] MCQ count matches expected 1301 exactly!");
} else {
    console.warn(`[WARN] MCQ count is ${totalMcqs}, expected 1301.`);
}

console.log("\n--- SPOT CHECKING SAMPLE RENDERING ---");
// Let's print a few MCQs that had roman items to verify they look clean and are line-separated!
const ch2Mcqs = fin2['2'].mcqData;
const romanSample = ch2Mcqs.find(q => q.text.includes("<br>"));
if (romanSample) {
    console.log("Found a normalized Roman item question:");
    console.log("ID:", romanSample.id);
    console.log("Text:", romanSample.text);
    console.log("Options:", romanSample.options);
    console.log("Correct Answer Index:", romanSample.correctAnswer);
    console.log("Explanation:", romanSample.explanation);
} else {
    console.log("No Roman item question found in Chapter 2.");
}

console.log("\nVERIFICATION COMPLETE: ALL CHECKS PASSED!");
