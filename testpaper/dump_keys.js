const fs = require('fs');
const content = fs.readFileSync('c:/Users/BMTF/.antigravity/testpaper/data.js', 'utf8');
// Simple extraction of keys from the top level object
const match = content.match(/const testDatabase = \{([\s\S]*?)\};/);
if (match) {
    const body = match[1];
    const keys = [];
    // This is a bit hacky but should work for a quick look
    const keyRegex = /^\s*"([^"]+)"\s*:/gm;
    let m;
    while ((m = keyRegex.exec(body)) !== null) {
        keys.push(m[1]);
    }
    console.log("Keys found:", keys);
} else {
    console.log("Could not find testDatabase");
}
