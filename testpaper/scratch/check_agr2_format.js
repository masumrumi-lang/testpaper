const fs = require('fs');
const c = fs.readFileSync('data.js', 'utf-8');

// Find agr2
const idx = c.indexOf('"agr2"');
console.log('agr2 found at index:', idx);

if (idx >= 0) {
    console.log('\n--- FIRST 2000 chars of agr2 block ---');
    console.log(c.substring(idx, idx + 2000));
}

// Also check format of an existing subject for comparison
const agr1Idx = c.indexOf('"agr1"');
console.log('\n--- agr1 first 1500 chars for comparison ---');
if (agr1Idx >= 0) {
    console.log(c.substring(agr1Idx, agr1Idx + 1500));
}
