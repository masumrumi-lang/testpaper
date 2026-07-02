const fs = require('fs');

const d = fs.readFileSync('data.js', 'utf8');

console.log(d.includes('"fin1"'));
console.log(d.includes('shortCQData'));
console.log(d.includes('fullCQData'));