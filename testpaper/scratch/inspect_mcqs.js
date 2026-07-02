const fs = require('fs');

const content = fs.readFileSync('c:\\Users\\BMTF\\.antigravity\\testpaper\\data.js', 'utf8');

// The file defines `const testDatabase = { ... }`.
// Let's append `module.exports = testDatabase;` and evaluate it or require it.
// To be safe and clean, let's replace `const testDatabase =` with `const testDatabase =` and add `global.testDatabase = testDatabase;`
// Then we run it.
const evalCode = content + '\nmodule.exports = testDatabase;';

let testDatabase;
try {
    // We can run eval in a clean context
    testDatabase = (new Function(evalCode + '\nreturn testDatabase;'))();
} catch (e) {
    console.error("Failed to eval:", e);
    process.exit(1);
}

const fin1 = testDatabase.fin1;
if (!fin1) {
    console.log("No fin1 block found");
    process.exit(1);
}

console.log("Successfully loaded database. Scanning for roman item MCQs in fin1...");

let count = 0;
for (const chKey in fin1) {
    const ch = fin1[chKey];
    const mcqData = ch.mcqData || [];
    for (const mcq of mcqData) {
        if (mcq.text && (mcq.text.includes('(i)') || mcq.text.includes('i.') || mcq.text.includes('i & ii') || mcq.text.includes('<br>'))) {
            console.log(`\nChapter ${chKey} MCQ id ${mcq.id}:`);
            console.log(JSON.stringify(mcq, null, 2));
            count++;
            if (count >= 5) break;
        }
    }
    if (count >= 5) break;
}
