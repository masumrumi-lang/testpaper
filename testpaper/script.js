/**
 * Antigravity HSC Question Bank - Core Script
 * Handles dynamic data loading from CSV files via fetch API.
 */

const DataLoader = {
    cache: null,
    csvUrl: 'hsc_mcq_bank_WEB_READY.csv',

    async loadData() {
        if (this.cache) return this.cache;
        
        try {
            const response = await fetch(this.csvUrl);
            if (!response.ok) throw new Error('Failed to fetch CSV data');
            const text = await response.text();
            this.cache = this.parseCSV(text);
            return this.cache;
        } catch (error) {
            console.error('DataLoader Error:', error);
            return [];
        }
    },

    parseCSV(text) {
        const lines = text.split(/\r?\n/);
        if (lines.length === 0) return [];
        
        const headers = lines[0].split(',').map(h => h.trim());
        const results = [];
        
        for (let i = 1; i < lines.length; i++) {
            if (!lines[i].trim()) continue;
            
            const row = [];
            let inQuotes = false;
            let currentValue = '';
            
            for (let char of lines[i]) {
                if (char === '"') {
                    inQuotes = !inQuotes;
                } else if (char === ',' && !inQuotes) {
                    row.push(currentValue.trim());
                    currentValue = '';
                } else {
                    currentValue += char;
                }
            }
            row.push(currentValue.trim());
            
            const item = {};
            headers.forEach((header, index) => {
                let val = row[index] || '';
                // Remove surrounding quotes if they exist
                if (val.startsWith('"') && val.endsWith('"')) {
                    val = val.substring(1, val.length - 1);
                }
                item[header] = val;
            });
            results.push(item);
        }
        return results;
    },

    async getQuestions(subjectId, chapterId) {
        const data = await this.loadData();
        // The CSV Subject might be "Accounting 1st", "Business 1st", etc.
        // subjectId from URL might be "acc1", "bus1", etc.
        // We need a mapping or fuzzy matching.
        
        const subjectMap = {
            'acc1': 'Accounting 1st',
            'acc2': 'Accounting 2nd',
            'bus1': 'Business Organization', // Based on chapters-bus1.html
            'bus2': 'Business 2nd',
            'fin1': 'Finance 1st',
            'fin2': 'Finance 2nd',
            'agr1': 'Agriculture 1st',
            'agr2': 'Agriculture 2nd',
            'ict': 'ICT'
        };

        const targetSubject = subjectMap[subjectId] || subjectId;
        const targetChapter = chapterId.startsWith('Chapter') ? chapterId : `Chapter ${chapterId}`;

        return data.filter(item => {
            const itemSubj = item.Subject ? item.Subject.toLowerCase() : '';
            const targetSubj = targetSubject.toLowerCase();
            const itemChap = item.Chapter ? item.Chapter.toLowerCase() : '';
            const targetChap = targetChapter.toLowerCase();
            
            return itemSubj.includes(targetSubj) && itemChap === targetChap;
        }).map(item => {
            // Transform CSV format to the one expected by mcq.html
            // CSV: Question, Options, Answer, Explanation, Meta
            // Options is "a) ... b) ... c) ... d) ..."
            
            const rawOptions = item.Options || '';
            const options = this.parseOptions(rawOptions);
            const correctAnswer = this.mapAnswerToIndex(item.Answer);

            return {
                text: item.Question,
                options: options,
                correctAnswer: correctAnswer,
                meta: `${item.Level} | ${item.Category}`,
                explanation: item.Explanation,
                html: item.HTML_Code
            };
        });
    },

    parseOptions(optionString) {
        // Split options like "a) ... b) ... c) ... d) ..."
        const parts = optionString.split(/[a-d]\)\s*/).filter(p => p.trim());
        if (parts.length === 4) return parts.map(p => p.trim());
        
        // Fallback for different formats
        return optionString.split('|').map(o => o.trim());
    },

    mapAnswerToIndex(answer) {
        if (!answer) return 0;
        const a = answer.toLowerCase().trim();
        if (a === 'a' || a === '১') return 0;
        if (a === 'b' || a === '২') return 1;
        if (a === 'c' || a === '৩') return 2;
        if (a === 'd' || a === '৪') return 3;
        return 0;
    }
};

// Export for use in HTML
window.DataLoader = DataLoader;
