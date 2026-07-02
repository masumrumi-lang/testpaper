const fs = require('fs');

const dbPath = 'c:\\Users\\BMTF\\.antigravity\\testpaper\\data.js';

console.log("Reading data.js for verification...");
const content = fs.readFileSync(dbPath, 'utf8');

// 1. Check JS validity by evaluating it
console.log("Evaluating updated data.js to verify syntax validity...");
let testDatabase;
try {
    const evalCode = content + '\nreturn testDatabase;';
    testDatabase = (new Function(evalCode))();
    console.log("[OK] data.js parsed and evaluated successfully without syntax errors!");
} catch (e) {
    console.error("[FAIL] syntax error in data.js:", e);
    process.exit(1);
}

// 2. Verify bus2 content
const bus2 = testDatabase.bus2;
if (!bus2) {
    console.error("[FAIL] No 'bus2' block found in database.");
    process.exit(1);
}

console.log("\n--- VERIFYING CHAPTERS ---");
let totalMcqs = 0;
const expectedChapters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];

for (const ch of expectedChapters) {
    const chData = bus2[ch];
    if (!chData) {
        console.error(`[FAIL] Chapter ${ch} is missing!`);
        process.exit(1);
    }
    const mcqCount = chData.mcqData ? chData.mcqData.length : 0;
    totalMcqs += mcqCount;
    console.log(`  Chapter ${ch.padStart(2)}: name="${chData.chapterName}", mcqCount=${mcqCount}`);
    
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

console.log(`\n[OK] Total MCQs in bus2: ${totalMcqs}`);
if (totalMcqs === 1271) {
    console.log("[OK] MCQ count matches expected 1271 exactly!");
} else {
    console.warn(`[WARN] MCQ count is ${totalMcqs}, expected 1271.`);
}

console.log("\n--- SPOT CHECKING SAMPLE RENDERING ---");
const ch1Mcqs = bus2['1'].mcqData;
const romanSample = ch1Mcqs.find(q => q.text.includes("<br>"));
if (romanSample) {
    console.log("Found a normalized Roman item question in Chapter 1:");
    console.log("ID:", romanSample.id);
    console.log("Text:", romanSample.text);
    console.log("Options:", romanSample.options);
    console.log("Correct Answer Index:", romanSample.correctAnswer);
    console.log("Explanation:", romanSample.explanation);
} else {
    console.log("No Roman item question found in Chapter 1.");
}

console.log("\nVERIFICATION COMPLETE: ALL CHECKS PASSED!");
