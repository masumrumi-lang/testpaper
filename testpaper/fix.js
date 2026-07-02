const fs = require('./static-data/fin1.json');
const file = require('fs');

Object.keys(fs).forEach(ch => {
  const c = fs[ch];

  fs[ch].shortCQData = (c.shortCQData || []).map(q => ({
    id: q.id,
    text: q.text || q.question,
    answer: q.answer,
    meta: q.meta,
    type: q.type
  }));

  fs[ch].fullCQData = (c.fullCQData || []).map(q => ({
    id: q.id,
    text: q.text || q.question,
    answer: q.answer,
    meta: q.meta,
    type: q.type
  }));
});

file.writeFileSync(
  './static-data/fin1.normalized.json',
  JSON.stringify(fs, null, 2)
);

console.log("Normalized file created");