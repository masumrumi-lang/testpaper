const fs = require('fs');
const content = fs.readFileSync('data.js', 'utf8');

const fin1Index = content.indexOf('"fin1":');
if (fin1Index === -1) {
    console.log("Could not find 'fin1' in data.js");
} else {
    console.log("Found 'fin1' at index:", fin1Index);
    console.log("Snippet around 'fin1':");
    console.log(content.substring(Math.max(0, fin1Index - 200), fin1Index + 1200));
}
