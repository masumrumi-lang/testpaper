const fs = require('fs');

const code1 = fs.readFileSync('acc1_ch1_part1.js', 'utf8');
const code2 = fs.readFileSync('acc1_ch1_part2.js', 'utf8');
const code3 = fs.readFileSync('acc1_ch1_part3.js', 'utf8');

let acc1_ch1_part1;
let acc1_ch1_part2;
let acc1_ch1_part3;

eval(code1);
eval(code2);
eval(code3);

const fullArray = [...acc1_ch1_part1, ...acc1_ch1_part2, ...acc1_ch1_part3];

// Let's modify data.js
let dataJs = fs.readFileSync('data.js', 'utf8');

// Format the array elements nicely to fit the data.js style
const formattedArray = "[\n" + fullArray.map(q => {
    return `                {\n                    id: ${q.id},\n                    text: ${JSON.stringify(q.text)},\n                    meta: ${JSON.stringify(q.meta)},\n                    options: ${JSON.stringify(q.options)},\n                    correctAnswer: ${q.correctAnswer}\n                }`;
}).join(",\n") + "\n            ]";

const regex = /(chapterName:\s*"Chapter 1 : Introduction to Accounting",\s*mcqData:\s*)\[[\s\S]*?\],\s*(shortCQData:)/;
dataJs = dataJs.replace(regex, `$1${formattedArray},\n            $2`);

fs.writeFileSync('data.js', dataJs);
console.log("Successfully merged " + fullArray.length + " questions into data.js");
