const fs = require('fs');

const content = fs.readFileSync('c:\\Users\\BMTF\\.antigravity\\testpaper\\data.js', 'utf8');
const evalCode = content + '\nmodule.exports = testDatabase;';
const testDatabase = (new Function(evalCode + '\nreturn testDatabase;'))();

const bus2 = testDatabase.bus2;
if (!bus2) {
    console.log("No bus2 block found in database.");
    process.exit(1);
}

console.log("Chapters in bus2:");
for (const chKey in bus2) {
    const ch = bus2[chKey];
    console.log(`- Chapter ID: "${chKey}", chapterName: "${ch.chapterName}", subjectName: "${ch.subjectName}", mcqCount: ${ch.mcqData ? ch.mcqData.length : 0}`);
}
