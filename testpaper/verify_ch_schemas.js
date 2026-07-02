const fs = require('fs');
const d = JSON.parse(fs.readFileSync('static-data/fin1.json', 'utf8'));
console.log('Chapter 1 fullCQ keys:', Object.keys(d['1'].fullCQData[0]));
console.log('Chapter 2 fullCQ keys:', Object.keys(d['2'].fullCQData[0]));
console.log('Sample Chapter 1 fullCQ:', d['1'].fullCQData[0]);
console.log('Sample Chapter 2 fullCQ:', d['2'].fullCQData[0]);
