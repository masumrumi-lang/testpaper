const fs = require('fs');

try {
    let content = fs.readFileSync('data.js', 'utf-8');

    // Replace the declaration so we can eval it
    let scriptContent = content.replace(/const\s+testDatabase\s*=/, 'global.testDatabase =');
    eval(scriptContent);

    let db = global.testDatabase;

    for (let subject of ['bus1', 'bus2']) {
        if (!db[subject]) continue;
        for (let chapId in db[subject]) {
            let chap = db[subject][chapId];
            if (chap.fullCQData && Array.isArray(chap.fullCQData)) {
                // Initialize/clear existing shortCQData
                chap.shortCQData = [];
                let shortId = 1;
                for (let cq of chap.fullCQData) {
                    if (cq.questions && Array.isArray(cq.questions)) {
                        for (let q of cq.questions) {
                            if (q.label === 'a' || q.label === 'b') {
                                chap.shortCQData.push({
                                    id: shortId++,
                                    text: q.text,
                                    meta: cq.meta || '',
                                    type: cq.type || 'college',
                                    answer: q.answer || ''
                                });
                            }
                        }
                    }
                }
            }
        }
    }

    let output = 'const testDatabase = ' + JSON.stringify(db, null, 4) + ';\n';
    fs.writeFileSync('data_test.js', output, 'utf-8');
    console.log("Success! Wrote to data_test.js");
} catch (e) {
    console.error(e);
}
