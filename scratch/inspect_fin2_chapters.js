const fs = require('fs');
const content = fs.readFileSync('c:\\Users\\BMTF\\.antigravity\\testpaper\\data.js', 'utf8');

const evalCode = content + '\nmodule.exports = testDatabase;';
const testDatabase = (new Function(evalCode + '\nreturn testDatabase;'))();

const fin2 = testDatabase.fin2;
console.log("Chapters in fin2:");
for (const chKey in fin2) {
    const ch = fin2[chKey];
    console.log(`- Chapter ID: "${chKey}", chapterName: "${ch.chapterName}", subjectName: "${ch.subjectName}"`);
}
