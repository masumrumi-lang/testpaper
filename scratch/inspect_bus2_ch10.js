const fs = require('fs');

const content = fs.readFileSync('c:\\Users\\BMTF\\.antigravity\\testpaper\\data.js', 'utf8');
const evalCode = content + '\nreturn testDatabase;';
const testDatabase = (new Function(evalCode))();

const bus2 = testDatabase.bus2;
console.log("All chapter IDs and names in bus2:");
for (const chKey in bus2) {
    console.log(`- "${chKey}": "${bus2[chKey].chapterName}"`);
}
