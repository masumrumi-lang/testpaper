const fullCQ_part1 = [
    {
        id: "01",
        stem: "<p>On January 1, 2024, Mr. Parvez started a business with cash 80,000 Taka, furniture 40,000 Taka, and a loan of 50,000 Taka from Mita. The transactions for that month are as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 5: Goods purchased for cash including VAT 57,500 Taka.</li><li>Jan. 10: Goods sold to Rafiq for cash 60,000 Taka.</li><li>Jan. 12: Return inward (Sales return) 5,000 Taka.</li><li>Jan. 15: Commission received 7,000 Taka.</li><li>Jan. 20: Machinery purchased for cash 20,000 Taka.</li><li>Jan. 25: Goods purchased from Faruq 10,000 Taka.</li><li>Jan. 28: Rent paid 8,000 Taka.</li><li>Jan. 30: Paid to Faruq 9,000 Taka in full settlement.</li></ul>",
        meta: "Dhaka College · 2026",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of capital at the beginning of the business.", 
                answer: "<div class='space-y-2'><p><strong>Initial Capital Calculation:</strong></p><table class='w-full border-collapse border border-gray-300 dark:border-gray-600 text-sm'><tr><td class='border p-2'>Cash (Owner's own)</td><td class='border p-2'>80,000</td></tr><tr><td class='border p-2'>Furniture</td><td class='border p-2'>40,000</td></tr><tr class='font-bold bg-gray-50 dark:bg-gray-800'><td class='border p-2'>Total Initial Capital</td><td class='border p-2'>1,20,000 Taka</td></tr></table><p class='text-xs italic'>Note: Bank loan (50,000) is a liability and not part of the owner's initial capital.</p></div>" 
            },
            { 
                label: "b", 
                text: "Journalize the transactions of dates 5, 12, 15 and 30.", 
                answer: "<div class='space-y-2'><p><strong>Journal Entries:</strong></p><table class='w-full border-collapse border border-gray-300 dark:border-gray-600 text-xs text-left'><thead><tr class='bg-gray-100 dark:bg-gray-700 font-bold'><th>Date</th><th>Accounts & Explanation</th><th>Dr</th><th>Cr</th></tr></thead><tbody><tr><td>Jan 5</td><td>Purchase A/C Dr<br>VAT Current A/C Dr<br>&nbsp;&nbsp;Cash A/C Cr</td><td>50,000<br>7,500</td><td><br>57,500</td></tr><tr><td>Jan 12</td><td>Sales Return A/C Dr<br>&nbsp;&nbsp;Cash A/C Cr</td><td>5,000</td><td>5,000</td></tr><tr><td>Jan 15</td><td>Cash A/C Dr<br>&nbsp;&nbsp;Commission Income A/C Cr</td><td>7,000</td><td>7,000</td></tr><tr><td>Jan 30</td><td>Accounts Payable (Faruq) A/C Dr<br>&nbsp;&nbsp;Cash A/C Cr<br>&nbsp;&nbsp;Discount Received A/C Cr</td><td>10,000</td><td>9,000<br>1,000</td></tr></tbody></table></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the transactions of dates 10, 20, 25 and 28 on the accounting equation.", 
                answer: "<ul class='list-decimal ml-6 space-y-1 text-sm'><li><strong>Jan 10:</strong> Cash increased (A+) 60,000; Owner's Equity increased (OE+) 60,000.</li><li><strong>Jan 20:</strong> Machinery increased (A+) 20,000; Cash decreased (A-) 20,000.</li><li><strong>Jan 25:</strong> Inventory (Equity) decreased (OE-) 10,000; Accounts Payable increased (L+) 10,000.</li><li><strong>Jan 28:</strong> Cash decreased (A-) 8,000; Owner's Equity decreased (OE-) 8,000.</li></ul>" 
            }
        ]
    },
    {
        id: "02",
        stem: "<p>Mr. Shamim started a legal business on January 1, 2025, with cash 1,00,000 Taka and a computer worth 50,000 Taka. The other events of his business during that month were as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Appointed a manager at a monthly salary of 15,000 Taka.</li><li>Jan. 8: Furniture purchased on credit 30,000 Taka.</li><li>Jan. 12: Legal services provided to clients for cash 25,000 Taka.</li><li>Jan. 18: Legal services provided to clients on credit 30,000 Taka.</li><li>Jan. 20: Loan taken from bank for personal needs 50,000 Taka.</li><li>Jan. 30: Manager's salary for the current month was paid.</li><li>Jan. 30: Price of furniture purchased on credit was paid 10,000 Taka.</li><li>Jan. 31: Office rent for the month of January was paid 12,000 Taka.</li></ul>",
        meta: "Rajuk Uttara Model College, Dhaka · 2026",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Identify the events which are not business transactions and determine their total value.", 
                answer: "<div class='text-sm'><p><strong>Non-Business Events:</strong></p>1. Jan 2: Appointment of a manager (No financial change yet) - 15,000<br>2. Jan 20: Personal bank loan (Personal affair, not business) - 50,000<hr class='my-1'><strong>Total: 65,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine the amount of Mr. Shamim's owner's equity at the end of January 2025.", 
                answer: "<div class='text-sm space-y-1'><p><strong>Closing Owner's Equity Calculation:</strong></p><p>Initial Capital: 1,50,000</p><p>(+) Revenues: 25,000 (Cash) + 30,000 (Credit) = 55,000</p><p>(-) Expenses: 15,000 (Salary) + 12,000 (Rent) = 27,000</p><p><strong>Closing Equity = 1,78,000 Taka</strong></p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions on the accounting equation in a tabular format.", 
                answer: "<p class='text-sm italic'>Summary of Tabular Analysis:</p><ul class='list-disc ml-6 text-sm'><li>Jan 1: Cash +100k, Equipment +50k = Equity +150k</li><li>Jan 8: Furniture +30k = Accounts Payable +30k</li><li>Jan 12: Cash +25k = Equity +25k</li><li>Jan 18: Accounts Receivable +30k = Equity +30k</li><li>Jan 30: Cash -15k = Equity -15k</li><li>Jan 30: Cash -10k = Accounts Payable -10k</li><li>Jan 31: Cash -12k = Equity -12k</li></ul>" 
            }
        ]
    },
    {
        id: "03",
        stem: "<p>Mr. Nazrul started a business on January 1, 2025, with cash 50,000 Taka, furniture 60,000 Taka, and a cash loan of 30,000 Taka. The transactions of his organization for that month are as follows:</p><ul class='list-disc ml-6 mt-2'><li>June 2: Purchased machinery for 50,000 Taka, paid 30,000 Taka in cash, and issued a note for the remaining amount.</li><li>June 5: Goods purchased for cash including 15% VAT 34,500 Taka.</li><li>June 8: Goods sold for cash 15,000 Taka and on credit 10,000 Taka.</li><li>June 12: An account was opened in the bank with cash 5,000 Taka.</li><li>June 15: Commission received in cash 7,500 Taka.</li><li>June 25: Cash 4,800 Taka received in full settlement of a receivable of 5,000 Taka from a debtor.</li><li>June 30: Goods withdrawn by the owner for personal use at selling price 3,000 Taka.</li></ul>",
        meta: "Notre Dame College · 2026",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (50,000) + Furniture (60,000) = 1,10,000 Taka.</div><p class='text-xs'>Note: The 30,000 loan is a liability and does not increase capital.</p>" 
            },
            { 
                label: "b", 
                text: "Show the effect of the transactions of dates 1, 8, 12 and 30 on the accounting equation.", 
                answer: "<ul class='list-disc ml-6 text-sm'><li><strong>Jan 1:</strong> Cash +80k, Furniture +60k = Loan +30k, Equity +110k</li><li><strong>June 8:</strong> Cash +15k, Debtors +10k = Equity +25k</li><li><strong>June 12:</strong> Cash -5k, Bank +5k (No Equity effect)</li><li><strong>June 30:</strong> Inventory (Equity) -3k = Equity -3k (Drawings)</li></ul>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the transactions of dates 2, 5, 15 and 25. (Without explanation)", 
                answer: "<div class='text-xs space-y-2'><p>1. <strong>June 2:</strong> Machinery A/C Dr 50,000; Cash A/C Cr 30,000, Notes Payable A/C Cr 20,000</p><p>2. <strong>June 5:</strong> Purchase A/C Dr 30,000, VAT A/C Dr 4,500; Cash A/C Cr 34,500</p><p>3. <strong>June 15:</strong> Cash A/C Dr 7,500; Commission Income Cr 7,500</p><p>4. <strong>June 25:</strong> Cash A/C Dr 4,800, Discount Allowed Dr 200; Accounts Receivable Cr 5,000</p></div>" 
            }
        ]
    },
    {
        id: "04",
        stem: "<p>Mr. Samiron started a business on January 1, 2025, with cash 2,00,000 Taka and a loan of 1,60,000 Taka. The other transactions of his business were as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Goods purchased at 2% trade discount on 20,000 Taka.</li><li>Jan. 4: Owner's income tax paid 10,000 Taka.</li><li>Jan. 8: Bad debt was charged 1,000 Taka.</li><li>Jan. 10: Salary paid to office staff 20,000 Taka.</li><li>Jan. 12: A computer was purchased for the office 80,000 Taka.</li><li>Jan. 20: Goods withdrawn for personal use 10,000 Taka.</li><li>Jan. 25: A motor vehicle was purchased for business use 2,00,000 Taka.</li></ul>",
        meta: "Dhaka Commerce College · 2026",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of Mr. Samiron's drawings.", 
                answer: "<div class='text-sm'>Income Tax (Personal) + Goods Withdrawal = 10,000 + 10,000 = <strong>20,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare journal entries with the transactions of dates 2, 4, 8 and 25.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 2: Purchase Dr, Cash Cr (Net: 19,600)</p><p>Jan 4: Drawings Dr, Cash Cr (10,000)</p><p>Jan 8: Bad Debt Dr, Accounts Receivable Cr (1,000)</p><p>Jan 25: Motor Vehicle Dr, Cash Cr (2,00,000)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the transactions of dates 1, 10, 12 and 20 on the accounting equation.", 
                answer: "<div class='text-sm'>1. Jan 1: Cash +3.6L = Loan +1.6L, Equity +2L<br>2. Jan 10: Cash -20k = Equity -20k<br>3. Jan 12: Cash -80k, Equipment +80k (No Equity effect)<br>4. Jan 20: Equity -10k = Equity -10k (Drawings)</div>" 
            }
        ]
    },
    {
        id: "05",
        stem: "<p>Mr. Fahim Sarker started a business on July 1st, 2025, with cash 2,50,000 Taka; furniture 1,50,000 Taka and a loan of 75,000 Taka. The other transactions in his business in that month are as follows:</p><ul class='list-disc ml-6 mt-2'><li>July 2: Goods sold to Itu at 10% discount for 75,000 Taka.</li><li>July 8: Drawings by the owner 7,500 Taka.</li><li>July 12: Goods purchase of 80,000 Taka was paid in cash including 15% VAT.</li><li>July 15: 35,000 Taka of the loan was paid in cash.</li><li>July 28: Employees' salary paid 15,000 Taka.</li><li>July 30: Goods distributed free of cost 5,000 Taka.</li></ul>",
        meta: "Govt. Azizul Haque College, Bogra · 2026",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "What is the amount of initial capital?", 
                answer: "<div class='text-sm'>Capital = Cash (2,50,000) + Furniture (1,50,000) = <strong>4,00,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare a tabular sheet for the dates 1, 8, 15 and 28.", 
                answer: "<div class='text-sm'>July 1: Cash +3.25L, Furniture +1.5L = Loan +75k, Equity +400k<br>July 8: Cash -7.5k = Equity -7.5k<br>July 15: Cash -35k = Loan -35k<br>July 28: Cash -15k = Equity -15k</div>" 
            },
            { 
                label: "c", 
                text: "Journalize the transactions of dates 2, 8, 12 and 30 (without explanation).", 
                answer: "<div class='text-xs space-y-1'><p>July 2: Accounts Receivable Dr, Sales Cr (67,500)</p><p>July 8: Drawings Dr, Cash Cr (7,500)</p><p>July 12: Purchase Dr (69,565), VAT Dr (10,435), Cash Cr (80,000)</p><p>July 30: Advertisement Dr, Purchase Cr (5,000)</p></div>" 
            }
        ]
    },
    {
        id: "06",
        stem: "<p>The account balances of BSRM Steel on August 31, 2025, were as follows: Cash 67,000 Taka; Office equipment 2,00,000 Taka; Accounts receivable 25,000 Taka and Accounts payable 18,000 Taka. The events that occurred in its business in the month of September 2025 are as follows:</p><ul class='list-disc ml-6 mt-2'><li>Sept. 5: Loan taken from bank 50,000 Taka.</li><li>Sept. 6: 10 months' house rent was paid in advance 30,000 Taka.</li><li>Sept. 12: Insurance premium was paid 10,200 Taka.</li><li>Sept. 16: Goods were sold for 1,20,000 Taka (30% in cash, 70% on credit).</li><li>Sept. 18: Goods were withdrawn by the owner 5,000 Taka.</li><li>Sept. 20: 12,000 Taka was received from a debtor.</li><li>Sept. 22: Goods were sold through bills receivable 5,000 Taka.</li><li>Sept. 26: Paid for the owner's life insurance premium 10,000 Taka.</li></ul>",
        meta: "Cantonment College, Jessore · 2026",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm space-y-1'><p><strong>Initial Capital (Sept 1):</strong></p><p>Total Assets = Cash (67k) + Equipment (200k) + A/R (25k) = 2,92,000</p><p>Less Liability = A/P (18k)</p><p><strong>Capital = 2,74,000 Taka</strong></p></div>" 
            },
            { 
                label: "b", 
                text: "Considering the opening balances, show the effect of the transactions of dates 5, 6, 16, 26 on the accounting equation.", 
                answer: "<ul class='list-disc ml-6 text-sm'><li>Sept 5: Cash +50k = Loan +50k</li><li>Sept 6: Cash -30k, Prepaid Rent +30k (No Equity effect)</li><li>Sept 16: Cash +36k, A/R +84k = Equity +120k</li><li>Sept 26: Cash -10k = Equity -10k (Drawings)</li></ul>" 
            },
            { 
                label: "c", 
                text: "Journalize the transactions of dates 12, 18, 20, 22.", 
                answer: "<div class='text-xs space-y-1'><p>Sept 12: Insurance Expense Dr, Cash Cr (10,200)</p><p>Sept 18: Drawings Dr, Purchase Cr (5,000)</p><p>Sept 20: Cash Dr, Accounts Receivable Cr (12,000)</p><p>Sept 22: Bills Receivable Dr, Sales Cr (5,000)</p></div>" 
            }
        ]
    },
    {
        id: "07",
        stem: "<p>Mr. Umama Atif is a businessman. He started a business on June 1, 2020, with cash 2,00,000 Taka. The transactions completed in his business in the month of June are as follows:</p><ul class='list-disc ml-6 mt-2'><li>June 3: Goods purchased on credit from Salsabil Traders 80,000 Taka.</li><li>June 7: Goods sold for cash 60,000 Taka (cost price 40,000 Taka).</li><li>June 10: Sold on credit to Safin Enterprise 90,000 Taka (cost price 65,000 Taka).</li><li>June 20: Goods returned to Salsabil Traders 2,000 Taka.</li><li>June 25: Paid three-fourths to Salsabil Traders subject to a 3% discount.</li><li>June 30: Collected from Safin Enterprise after a 4% discount 19,200 Taka.</li><li>June 30: Amount of bad debts 1,000 Taka.</li></ul>",
        meta: "Govt. Commerce College, Chittagong · 2026",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of net purchases and net sales for Mr. Umama Atif in the month of June.", 
                answer: "<div class='text-sm'>Net Purchase = 80,000 - 2,000 = <strong>78,000 Taka</strong><br>Net Sales = 60,000 + 90,000 = <strong>1,50,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare a tabular summary of the transactions.", 
                answer: "<p class='text-sm italic'>Summary of Tabular Analysis:</p><ul class='list-disc ml-6 text-sm'><li>June 3: Inventory (Equity) -80k, A/P +80k</li><li>June 7: Cash +60k, Equity +60k; Inventory (Equity) -40k, Inventory +40k</li><li>June 25: Cash -56,745, A/P -58,500, Equity (Discount) +1,755</li></ul>" 
            },
            { 
                label: "c", 
                text: "Prepare an income statement for Mr. Umama Atif at the end of June.", 
                answer: "<div class='text-sm space-y-1'><p>Sales: 1,50,000</p><p>(-) COGS: 40,000 + 65,000 = (1,05,000)</p><p>Gross Profit: 45,000</p><p>(+) Discount Received: 1,755</p><p>(-) Expenses (Bad debt 1k + Disc allowed 800): (1,800)</p><p><strong>Net Profit = 44,955 Taka</strong></p></div>" 
            }
        ]
    },
    {
        id: "08",
        stem: "<p>Mr. Farhad Azam started a computer repair shop named 'Azam Computer Servicing' on June 1, 2025. The transactions that occurred in the business during that month are as follows:</p><ul class='list-disc ml-6 mt-2'><li>June 1: Farhad invested 40,000 Taka to start the computer repair shop.</li><li>June 5: Office equipment worth 20,000 Taka was purchased from Akmal Enterprise.</li><li>June 11: Income from computer repair 29,000 Taka and cash receipt 20,200 Taka.</li><li>June 15: Cash withdrawn by Farhad for personal use 4,000 Taka and income tax paid 2,400 Taka.</li><li>June 20: Salary paid to part-time employee 6,000 Taka.</li><li>June 25: Life insurance premium paid 2,500 Taka.</li></ul>",
        meta: "Ananda Mohan College, Mymensingh · 2026",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the total amount of drawings.", 
                answer: "<div class='text-sm'>Cash Withdrawal (4k) + Income Tax (2.4k) + Life Insurance (2.5k) = <strong>8,900 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Classify the accounts related to the transactions from dates 1 to 15. (In equation method)", 
                answer: "<div class='text-xs space-y-1'><p>June 1: Cash (A), Capital (OE)</p><p>June 5: Equipment (A), Accounts Payable (L)</p><p>June 11: Cash (A), A/R (A), Service Revenue (OE)</p><p>June 15: Drawings (OE), Cash (A)</p></div>" 
            },
            { 
                label: "c", 
                text: "Analyze the effect of the transactions of the month of June on the accounting equation.", 
                answer: "<p class='text-sm italic'>Tabular Analysis Results:</p><p class='text-sm'>Total Assets = Total Liabilities + Equity = <strong>60,100 Taka</strong></p>" 
            }
        ]
    },
    {
        id: "09",
        stem: "<p>Mr. Niloy started a business on January 1, 2024, with a bank loan of 1,60,000 Taka and 54% of his personally used computer equipment (total value 2,50,000 Taka). His other transactions in that month were as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Computer purchased 80,000 Taka.</li><li>Jan. 5: Program purchased on credit 1,00,000 Taka (fixed asset).</li><li>Jan. 9: Order received for website creation 55,000 Taka.</li><li>Jan. 14: Internet connection installation cost 30,000 Taka (fixed asset).</li><li>Jan. 20: Income from website creation 2,00,000 Taka.</li><li>Jan. 27: Monthly mobile and internet expenses 50,000 Taka.</li><li>Jan. 30: Insurance premium paid in advance 45,000 Taka.</li><li>Jan. 31: Advertising 20,000 Taka.</li></ul>",
        meta: "Azam Khan Govt. Commerce College, Khulna · 2026",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "What is the amount of Mr. Niloy's initial capital?", 
                answer: "<div class='text-sm'>Initial Capital = 2,50,000 * 54% = <strong>1,35,000 Taka</strong>.<br><span class='text-xs'>Note: Bank loan is a liability.</span></div>" 
            },
            { 
                label: "b", 
                text: "Prepare an income statement for the month of January.", 
                answer: "<div class='text-sm'>Revenue: 2,00,000<br>(-) Expenses: 50,000 + 20,000 = (70,000)<br><strong>Net Income = 1,30,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions on the accounting equation in a tabular format.", 
                answer: "<div class='text-sm'>Total of Equation = <strong>5,25,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "10",
        stem: "<p>On January 1, 2025, Mr. Kamrul started a business with cash 80,000 Taka, furniture 40,000 Taka and a loan of 90,000 Taka from the bank. The transactions of his business in the first month were as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Purchased a delivery van worth 90,000 Taka, paid 40,000 Taka in cash, and issued a note for the remaining amount.</li><li>Jan. 5: Goods purchased for cash including VAT 57,500 Taka.</li><li>Jan. 10: Goods sold to Mr. Rafiq at a 10% discount for 50,000 Taka and received 25,000 Taka in cash.</li><li>Jan. 12: Return inward 5,000 Taka.</li><li>Jan. 15: Supplies for the office purchased for 7,000 Taka and paid 2,000 Taka in cash.</li><li>Jan. 17: Appointed a manager at a salary of 20,000 Taka.</li><li>Jan. 20: Commission received 7,000 Taka.</li><li>Jan. 30: Advertisement bill received from a national daily for 5,000 Taka.</li></ul>",
        meta: "Azam Khan Govt. Commerce College, Khulna · 2026",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Identify the events that are not transactions.", 
                answer: "<div class='text-sm'>Jan 17: Appointment of a manager - 20,000 Taka</div>" 
            },
            { 
                label: "b", 
                text: "Determine the accounts with their classification for the transactions of dates 2, 5, 10 and 12.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 2: Van (A), Cash (A), Note Payable (L)</p><p>Jan 5: Purchase (OE), VAT (A), Cash (A)</p><p>Jan 10: Cash (A), A/R (A), Sales (OE)</p><p>Jan 12: Sales Return (OE), A/R (A)</p></div>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the transactions of dates 1, 15, 20 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 1: Cash Dr 1.7L, Furniture Dr 40k; Loan Cr 90k, Capital Cr 1.2L</p><p>Jan 15: Supplies Dr 7k; Cash Cr 2k, A/P Cr 5k</p><p>Jan 20: Cash Dr 7k; Commission Cr 7k</p><p>Jan 30: Advertising Dr 5k; A/P Cr 5k</p></div>" 
            }
        ]
    },
    {
        id: "11",
        stem: "<p>The account balances of Raj Traders on June 30, 2023, were as follows: Cash 25,000 Taka, Accounts Receivable 40,000 Taka, Machinery 40,000 Taka, Furniture 25,000 Taka, and Accounts Payable 20,000 Taka. The transactions for July are as follows:</p><ul class='list-disc ml-6 mt-2'><li>July 5: Goods purchased for cash 20,000 Taka and on credit 50,000 Taka.</li><li>July 6: One year insurance premium paid in advance 24,000 Taka.</li><li>July 10: Goods sold for cash 50,000 Taka and through bills receivable 20,000 Taka.</li><li>July 14: Collected half of the initial accounts receivable subject to a 2% discount.</li><li>July 20: Goods used from the business for advertising 5,000 Taka.</li><li>July 31: One month of insurance has expired.</li></ul>",
        meta: "Dhaka Residential Model College · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Provide the opening journal entry.", 
                answer: "<div class='text-xs space-y-1'><p>Cash A/C Dr 25,000</p><p>Accounts Receivable A/C Dr 40,000</p><p>Machinery A/C Dr 40,000</p><p>Furniture A/C Dr 25,000</p><p>&nbsp;&nbsp;Accounts Payable A/C Cr 20,000</p><p>&nbsp;&nbsp;Capital A/C Cr 1,10,000</p></div>" 
            },
            { 
                label: "b", 
                text: "Determine the classification of accounts for the transactions from July 5 to 31.", 
                answer: "<ul class='list-disc ml-6 text-sm'><li>July 5: Purchase (OE), Cash (A), A/P (L)</li><li>July 6: Prepaid Insurance (A), Cash (A)</li><li>July 10: Cash (A), B/R (A), Sales (OE)</li><li>July 14: Cash (A), Discount Allowed (OE), A/R (A)</li><li>July 20: Advertising (OE), Purchase (OE)</li><li>July 31: Insurance Expense (OE), Prepaid Insurance (A)</li></ul>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the transactions on the accounting equation.", 
                answer: "<div class='text-sm'>Total of Accounting Equation (A = L + OE) = <strong>1,54,600 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "12",
        stem: "<p>The ledger balances of Salim Traders on December 31, 2023, were: Cash 1,00,000 Taka, Office Equipment 1,50,000 Taka, Accounts Receivable 50,000 Taka, and Accounts Payable 40,000 Taka. The transactions for January 2024 were as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 5: Loan taken from bank 50,000 Taka through a 10% note payable.</li><li>Jan. 8: Goods purchased for cash 30,000 Taka and on credit 90,000 Taka.</li><li>Jan. 10: Three months' rent paid in advance 15,000 Taka.</li><li>Jan. 12: Paid miscellaneous expenses 1,200 Taka.</li><li>Jan. 16: Goods sold at 3% trade discount for 1,20,000 Taka (60% in cash, 40% on credit).</li><li>Jan. 25: 30,000 Taka received from a customer.</li><li>Jan. 28: One month of the prepaid rent has expired.</li></ul>",
        meta: "Dhaka Residential Model College · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Provide the opening journal entry.", 
                answer: "<div class='text-xs space-y-1'><p>Cash Dr 1,00,000</p><p>Office Equipment Dr 1,50,000</p><p>Accounts Receivable Dr 50,000</p><p>&nbsp;&nbsp;Accounts Payable Cr 40,000</p><p>&nbsp;&nbsp;Capital Cr 2,60,000</p></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of transactions on the accounting equation using a tabular format.", 
                answer: "<div class='text-sm'>Analysis shows Cash balance: 1,73,640; A/R: 66,560; Equipment: 1,50,000; Prepaid Rent: 10,000.<br>Total Assets = <strong>4,00,200 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Prepare an income statement for the month ended January 31.", 
                answer: "<div class='text-sm space-y-1'><p>Net Sales: 1,16,400</p><p>(-) Purchase: (1,20,000)</p><p>(-) Rent Expense: (5,000)</p><p>(-) Misc Expense: (1,200)</p><p><strong>Net Loss = (9,800) Taka</strong></p></div>" 
            }
        ]
    },
    {
        id: "13",
        stem: "<p>Mr. Ratan Sarkar started a business on June 1, 2023, with cash 2,00,000 Taka, furniture 1,50,000 Taka, and a bank loan of 75,000 Taka. The other transactions for the month were as follows:</p><ul class='list-disc ml-6 mt-2'><li>June 2: Goods sold to Israt at 10% discount for 1,05,000 Taka.</li><li>June 8: Goods withdrawn by the owner 7,500 Taka.</li><li>June 12: Goods purchased for 1,80,000 Taka, of which 45% was paid in cash.</li><li>June 15: 35% of the bank loan was paid in cash.</li><li>June 28: Employees' salary paid 15,000 Taka.</li><li>June 30: Bank charges 500 Taka.</li></ul>",
        meta: "Govt. Azizul Haque College, Bogra · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "What is the amount of initial capital?", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (2,00,000) + Furniture (1,50,000) = <strong>3,50,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare a tabular sheet for the dates 1, 8, 15 and 28.", 
                answer: "<div class='text-sm'>June 1: Cash +2.75L, Furniture +1.5L = Loan +75k, Equity +350k<br>June 8: Purchase/Equity -7.5k = Equity -7.5k (Drawings)<br>June 15: Cash -26,250 = Loan -26,250<br>June 28: Cash -15,000 = Equity -15,000</div>" 
            },
            { 
                label: "c", 
                text: "Journalize the transactions of dates 2, 8, 12 and 30 (without explanation).", 
                answer: "<div class='text-xs space-y-1'><p>June 2: A/R (Israt) Dr, Sales Cr (94,500)</p><p>June 8: Drawings Dr, Purchase Cr (7,500)</p><p>June 12: Purchase Dr 1.8L; Cash Cr 81k, A/P Cr 99k</p><p>June 30: Bank Charge Dr 500, Cash Cr 500</p></div>" 
            }
        ]
    },
    {
        id: "14",
        stem: "<p>Mr. Rahman started a business on January 1, 2023, with cash 5,00,000 Taka, bank balance 1,00,000 Taka, and a loan of 2,00,000 Taka. The transactions for the month were as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 1: Received advance shop rent from a tenant 12,000 Taka (for 12 months).</li><li>Jan. 3: Purchased through check 50,000 Taka.</li><li>Jan. 6: Goods sold on credit 70,000 Taka.</li><li>Jan. 10: Bank withdrawal for personal needs 10,000 Taka.</li><li>Jan. 25: Bank interest allowed 1,200 Taka and charges deducted 1,000 Taka.</li><li>Jan. 30: Free distribution of goods to consumers 5,000 Taka.</li></ul>",
        meta: "Govt. City College, Chittagong · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "What is Mr. Rahman's initial capital?", 
                answer: "<div class='text-sm'>Initial Capital = Cash (500k) + Bank (100k) = <strong>6,00,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the classification of accounts for the transactions.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 1: Cash (A), Unearned Rent (L)</p><p>Jan 3: Purchase (OE), Bank (A)</p><p>Jan 6: A/R (A), Sales (OE)</p><p>Jan 10: Drawings (OE), Bank (A)</p><p>Jan 25: Bank (A), Interest (OE); Bank Charge (OE), Bank (A)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions on the accounting equation in a tabular format.", 
                answer: "<div class='text-sm'>Equation Total (A = L + OE) = <strong>8,12,200 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "15",
        stem: "<p>The transactions for Nadim Service Center for March 2023 were as follows:</p><ul class='list-disc ml-6 mt-2'><li>March 1: Invested cash 50,000 Taka, equipment 25,000 Taka, and a personal loan of 5,000 Taka into the business.</li><li>March 7: Purchased supplies on credit 2,000 Taka.</li><li>March 12: Provided services to customers; received cash 17,000 Taka and billed 6,000 Taka.</li><li>March 20: Received a utility bill of 800 Taka.</li><li>March 25: Paid 8,000 Taka for a 2-year insurance policy.</li><li>March 28: Paid rent for the month of April 7,000 Taka.</li><li>March 30: 50% of the amount due from accounts receivable was received in cash.</li><li>March 31: Life insurance premium paid 2,000 Taka.</li></ul>",
        meta: "Dhaka College · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of net accounts receivable at the end of the month.", 
                answer: "<div class='text-sm'>Receivable from service (March 12) = 6,000<br>(-) Collected 50% (March 30) = (3,000)<br><strong>Net Accounts Receivable = 3,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of the transactions of March 1, 7, 25 and 31 on the accounting equation.", 
                answer: "<div class='text-sm'>March 1: Cash +55k, Equipment +25k = Loan +5k, Equity +75k<br>March 7: Supplies +2k = A/P +2k<br>March 25: Cash -8k, Prepaid Insurance +8k<br>March 31: Cash -2k = Equity -2k</div>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the transactions of March 12, 20, 28 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>March 12: Cash Dr 17k, A/R Dr 6k; Service Rev Cr 23k</p><p>March 20: Utility Expense Dr 800; A/P Cr 800</p><p>March 28: Prepaid Rent Dr 7k; Cash Cr 7k</p><p>March 30: Cash Dr 3k; A/R Cr 3k</p></div>" 
            }
        ]
    },
    {
        id: "16",
        stem: "<p>The account balances of Pathshiri Traders on January 1, 2025, were: Cash 1,00,000 Taka; Furniture 30,000 Taka; Accounts Receivable 40,000 Taka; Accounts Payable 20,000 Taka and Bank Loan 50,000 Taka. The other transactions for the month were as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 5: Goods purchased on credit at a 5% trade discount on 30,000 Taka.</li><li>Jan. 10: An almirah purchased for the office for 12,000 Taka.</li><li>Jan. 14: Goods sold on credit for 50,000 Taka.</li><li>Jan. 19: Partial repayment of the bank loan 25,000 Taka.</li><li>Jan. 26: Half of the amount due from the credit sale on January 14 was collected at a 4% discount.</li><li>Jan. 30: Office staff salaries paid 20,000 Taka.</li></ul>",
        meta: "Shahid Syed Nazrul Islam College · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial liabilities.", 
                answer: "<div class='text-sm'>Accounts Payable (20,000) + Bank Loan (50,000) = <strong>70,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Identify the accounts and classify them for the transactions of Jan 5, 10, 19, and 26.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 5: Purchase (OE), A/P (L)</p><p>Jan 10: Furniture (A), Cash (A)</p><p>Jan 19: Bank Loan (L), Cash (A)</p><p>Jan 26: Cash (A), Discount Allowed (OE), A/R (A)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the transactions of Jan 1, 10, 14, and 19 on the accounting equation.", 
                answer: "<div class='text-sm'>Equation Balance (A = L + OE):<br>Assets: 1,95,000 = Liabilities: 45,000 + Equity: 1,50,000</div>" 
            }
        ]
    },
    {
        id: "17",
        stem: "<p>The transactions of 'Alif Repair Shop' for March 2024 were as follows:</p><ul class='list-disc ml-6 mt-2'><li>March 1: Invested cash 70,000 Taka and equipment 20,000 Taka into the business.</li><li>March 7: Purchased supplies on credit 5,000 Taka.</li><li>March 12: Provided services; received 17,000 Taka in cash and billed 6,000 Taka to clients.</li><li>March 20: Received a utility bill of 1,400 Taka to be paid next month.</li><li>March 25: Paid 12,000 Taka for a 2-year insurance policy.</li><li>March 28: Paid rent for the month of March 4,000 Taka.</li><li>March 30: 40% of the amount due from clients was received in cash.</li><li>March 31: Owner's drawings for the month were 4,000 Taka.</li></ul>",
        meta: "Dinajpur Govt. College · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of net accounts receivable at the end of the month.", 
                answer: "<div class='text-sm'>Billed amount (March 12) = 6,000<br>(-) Collection 40% (March 30) = (2,400)<br><strong>Net A/R = 3,600 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of the transactions of March 1, 7, 25, and 31 on the accounting equation.", 
                answer: "<div class='text-sm'>March 1: Cash +70k, Equip +20k = Equity +90k<br>March 7: Supplies +5k = A/P +5k<br>March 25: Cash -12k, Prepaid Ins +12k<br>March 31: Cash -4k = Equity -4k</div>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the transactions of March 12, 20, 28, and 30.", 
                answer: "<div class='text-xs space-y-1'><p>March 12: Cash Dr 17k, A/R Dr 6k; Service Rev Cr 23k</p><p>March 20: Utility Expense Dr 1,400; A/P Cr 1,400</p><p>March 28: Rent Expense Dr 4,000; Cash Cr 4,000</p><p>March 30: Cash Dr 2,400; A/R Cr 2,400</p></div>" 
            }
        ]
    },
    {
        id: "18",
        stem: "<p>The following transactions were completed in Mr. Nazrul's business:</p><ol class='list-decimal ml-6 mt-2'><li>Started business with cash 5,00,000 Taka and bank deposit 2,00,000 Taka.</li><li>Goods purchased through check 50,000 Taka.</li><li>Goods sold on credit 20,000 Taka.</li><li>Free distribution of goods 8,000 Taka.</li><li>Withdrawal from bank 10,000 Taka.</li><li>Bank allowed interest 800 Taka.</li></ol>",
        meta: "Govt. Haji Muhammad Mohsin College, Chittagong · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "What is the amount of Mr. Nazrul's cash balance?", 
                answer: "<div class='text-sm'>Initial Cash (5,00,000) + Bank Withdrawal (10,000) = <strong>5,10,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Classify the above transactions using the modern method.", 
                answer: "<ul class='list-disc ml-6 text-xs'><li>1. Cash (A), Bank (A), Capital (OE)</li><li>2. Purchase (OE), Bank (A)</li><li>3. A/R (A), Sales (OE)</li><li>4. Advertisement (OE), Purchase (OE)</li><li>5. Cash (A), Bank (A)</li><li>6. Bank (A), Interest Income (OE)</li></ul>" 
            },
            { 
                label: "c", 
                text: "Determine the amount of owner's equity using the transactions.", 
                answer: "<div class='text-sm'>Initial Capital (7,00,000) - Purchase (50,000) + Sales (20,000) + Bank Interest (800) = <strong>6,70,800 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "19",
        stem: "<p>Mr. Kabir is a lawyer at the Chittagong Bar. He opened an account with 10,000 Taka on January 1, 2023. Other transactions for the month were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 1: Appointed an assistant with a monthly salary of 7,000 Taka.</li><li>Jan. 3: Purchased law books for 2,000 Taka and paid by check.</li><li>Jan. 7: Received a consultant fee of 5,000 Taka via check from a client.</li><li>Jan. 12: Deposited 7,000 Taka into the bank.</li><li>Jan. 14: Placed an order for 10,000 Taka worth of books.</li><li>Jan. 15: Deposited the check received on the 7th into the bank.</li><li>Jan. 20: Purchased furniture for 2,000 Taka and paid by check.</li><li>Jan. 25: A client deposited 3,000 Taka directly into Mr. Kabir's bank account.</li><li>Jan. 27: The check deposited on the 15th was rejected by the bank.</li><li>Jan. 30: Mr. Kabir withdrew 6,000 Taka from the bank for personal use.</li></ul>",
        meta: "Govt. Haji Muhammad Mohsin College, Chittagong · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Identify the events that are not transactions and determine their total value.", 
                answer: "<div class='text-sm'>Jan 1: Assistant appointment (7,000) + Jan 14: Book order (10,000) = <strong>17,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine Mr. Kabir's total income for the month.", 
                answer: "<div class='text-sm font-medium'>Total Income = Consultant Fee (5,000) + Service Fee (3,000) = <strong>8,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the transactions.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 3: Books Dr 2k; Bank Cr 2k</p><p>Jan 7: Cash/Check Dr 5k; Fee Income Cr 5k</p><p>Jan 12: Bank Dr 7k; Cash Cr 7k</p><p>Jan 20: Furniture Dr 2k; Bank Cr 2k</p><p>Jan 27: Accounts Receivable Dr 5k; Bank Cr 5k (Bounced check)</p><p>Jan 30: Drawings Dr 6k; Bank Cr 6k</p></div>" 
            }
        ]
    },
    {
        id: "20",
        stem: "<p>On January 1, 2023, Mr. Riaz started a business with cash 80,000 Taka, furniture 40,000 Taka, and a loan of 50,000 Taka from Mita. The transactions for that month were as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 5: Goods purchased for cash including VAT 57,500 Taka.</li><li>Jan. 10: Goods sold to Rafiq for cash 60,000 Taka.</li><li>Jan. 12: Sales return 5,000 Taka.</li><li>Jan. 15: Commission received 7,000 Taka.</li><li>Jan. 20: Machinery purchased for cash 20,000 Taka.</li><li>Jan. 25: Goods purchased from Faruq on credit 10,000 Taka.</li><li>Jan. 28: Rent paid 8,000 Taka.</li><li>Jan. 30: Paid to Faruq 9,000 Taka in full settlement.</li></ul>",
        meta: "Govt. Haji Muhammad Mohsin College, Chittagong · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of capital at the beginning of the business.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (80,000) + Furniture (40,000) = <strong>1,20,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Journalize the transactions of dates 5, 12, 15 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 5: Purchase Dr 50k, VAT Dr 7.5k; Cash Cr 57.5k</p><p>Jan 12: Sales Return Dr 5k; Cash Cr 5k</p><p>Jan 15: Cash Dr 7k; Commission Cr 7k</p><p>Jan 30: A/P (Faruq) Dr 10k; Cash Cr 9k, Disc Rec Cr 1k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the transactions of dates 10, 12, 15 and 25 on the accounting equation.", 
                answer: "<div class='text-sm'>1. Jan 10: Cash +60k = Equity +60k<br>2. Jan 12: Cash -5k = Equity -5k<br>3. Jan 15: Cash +7k = Equity +7k<br>4. Jan 25: A/P +10k = Equity -10k</div>" 
            }
        ]
    },
    {
        id: "21",
        stem: "<p>Mr. Safin is a businessman in Khatunganj, Chittagong. He started a business on April 1, 2024, with cash 1,00,000 Taka. The transactions completed in his business in the month of April are as follows:</p><ul class='list-disc ml-6 mt-2'><li>April 3: Goods purchased on credit from Tariza Traders 80,000 Taka.</li><li>April 6: Goods sold on credit to Rauf Enterprise 60,000 Taka.</li><li>April 10: Goods sold for cash 40,000 Taka.</li><li>April 14: Goods returned to Tariza Traders 5,000 Taka.</li><li>April 20: Rauf Enterprise returned goods worth 6,000 Taka due to poor quality.</li><li>April 25: Half of the payable amount to Tariza Traders was paid subject to a 3% discount.</li><li>April 31: Goods withdrawn for personal use 3,500 Taka.</li></ul>",
        meta: "Govt. Haji Muhammad Mohsin College, Chittagong · 2026",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of net purchases and net sales for Mr. Safin in the month of April.", 
                answer: "<div class='text-sm'>Net Purchase = 80,000 - 2,000 = <strong>75,000 Taka</strong><br>Net Sales = 60,000 + 40,000 - 6,000 = <strong>94,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare a tabular summary of the transactions.", 
                answer: "<div class='text-sm'>Total Assets = Total Liabilities + Equity = <strong>1,64,375 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the transactions of dates 6, 14, 20 and 25 of April.", 
                answer: "<div class='text-xs space-y-1'><p>April 6: A/R (Rauf) Dr, Sales Cr (60,000)</p><p>April 14: A/P (Tariza) Dr, Purchase Return Cr (5,000)</p><p>April 20: Sales Return Dr, A/R (Rauf) Cr (6,000)</p><p>April 25: A/P (Tariza) Dr 37,500; Cash Cr 36,375, Disc Rec Cr 1,125</p></div>" 
            }
        ]
    },
    {
        id: "22",
        stem: "<p>The business transactions of Mr. Wasik for the month of January 2024 are as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 1: Business was started with cash 5,00,000 Taka, an almirah worth 2,00,000 Taka, and a bank loan of 2,00,000 Taka.</li><li>Jan. 8: Services provided to customers 80,000 Taka and cheque received 20,000 Taka.</li><li>Jan. 15: Wall clock purchased 5,000 Taka.</li><li>Jan. 25: Bank loan paid from the owner's personal fund 1,00,000 Taka.</li><li>Jan. 31: Supplies used 3,000 Taka.</li></ul>",
        meta: "Rajuk Uttara Model College, Dhaka · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (5,00,000) + Almirah (2,00,000) = <strong>7,00,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the classification of accounts from the above transactions.", 
                answer: "<ul class='list-disc ml-6 text-xs text-left'><li>Jan 1: Cash (A), Furniture (A), Loan (L), Capital (OE)</li><li>Jan 8: Bank (A), A/R (A), Service Revenue (OE)</li><li>Jan 15: Furniture/Equip (A), Cash (A)</li><li>Jan 25: Loan (L), Capital (OE)</li><li>Jan 31: Supplies Exp (OE), Supplies (A)</li></ul>" 
            },
            { 
                label: "c", 
                text: "Show it on the accounting equation with the help of a tabular format.", 
                answer: "<div class='text-sm'>Equation Total = <strong>8,77,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "23",
        stem: "<p>Mr. Ahsan started a business on January 1, 2024, with cash 1,00,000 Taka. The following transactions were completed in his business in that month:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 3: Goods purchased for cash 20,000 Taka.</li><li>Jan. 7: Purchased on credit from Rahim 30,000 Taka.</li><li>Jan. 10: Goods sold on credit 80,000 Taka.</li><li>Jan. 14: Goods withdrawn for the owner's personal needs 4,000 Taka.</li><li>Jan. 18: Stationery purchased 5,000 Taka.</li><li>Jan. 30: Furniture purchased for office use 30,000 Taka. (80% on credit)</li></ul>",
        meta: "Ideal School and College, Motijheel · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of cash involved in the purchase of furniture.", 
                answer: "<div class='text-sm'>Furniture Cash = 30,000 * 20% = <strong>6,00,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine the amount of owner's equity at the end of the month.", 
                answer: "<div class='text-sm'>Initial (100k) - Purchases (50k) + Sales (80k) - Drawings (4k) - Stationery (5k) = <strong>1,21,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the transactions of dates 1, 3, 10 and 30 on the accounting equation.", 
                answer: "<div class='text-sm'>1. Jan 1: Cash +100k = Equity +100k<br>2. Jan 3: Cash -20k = Equity -20k<br>3. Jan 10: A/R +80k = Equity +80k<br>4. Jan 30: Furniture +30k, Cash -6k, A/P +24k</div>" 
            }
        ]
    },
    {
        id: "24",
        stem: "<p>The account balances of Akram Traders on June 30, 2024, are as follows: Cash 40,000 Taka, office equipment 50,000 Taka; Accounts receivable 30,000 Taka, Accounts payable 20,000 Taka. The transactions completed in his business in the month of July are as follows:</p><ul class='list-disc ml-6 mt-2'><li>July 2: The owner invested cash 50,000 Taka and office equipment worth 25,000 Taka in the business.</li><li>July 5: Goods purchased 50,000 Taka (60% in cash and 40% on credit).</li><li>July 10: Salary paid 20,000 Taka.</li><li>July 15: The amount for the credit purchase of date 5 was paid.</li><li>July 20: Goods sold 1,00,000 Taka (80% in cash and 20% on credit).</li><li>July 30: Rent paid 25,000 Taka.</li></ul>",
        meta: "Chittagong Cantonment Public College · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Provide the opening journal entry for Akram Traders.", 
                answer: "<div class='text-xs space-y-1'><p>Cash Dr 40,000</p><p>Office Equip Dr 50,000</p><p>A/R Dr 30,000</p><p>&nbsp;&nbsp;A/P Cr 20,000</p><p>&nbsp;&nbsp;Capital Cr 1,00,000</p></div>" 
            },
            { 
                label: "b", 
                text: "Provide the journal entries for the transactions of dates 2, 5, 15 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>July 2: Cash Dr 50k, Equip Dr 25k; Capital Cr 75k</p><p>July 5: Purchase Dr 50k; Cash Cr 30k, A/P Cr 20k</p><p>July 15: A/P Dr 20k; Cash Cr 20k</p><p>July 30: Rent Dr 25k; Cash Cr 25k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect on the accounting equation in a tabular format.", 
                answer: "<div class='text-sm'>Equation Total (Assets = Liabilities + Equity) = <strong>2,30,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "25",
        stem: "<p>On January 1, 2021, Mr. Akib started a business with cash 2,00,000 Taka and furniture worth 50,000 Taka. The other transactions of that month are as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 4: Cash sales 40,000 Taka.</li><li>Jan. 7: Credit purchases 20,000 Taka.</li><li>Jan. 10: Deposited into the bank 10,000 Taka.</li><li>Jan. 15: Purchase of machinery 25,000 Taka.</li><li>Jan. 18: Rent paid 5,000 Taka.</li><li>Jan. 22: Credit sales 24,000 Taka.</li><li>Jan. 27: Withdrawn from the bank for personal needs 7,000 Taka.</li><li>Jan. 30: Received from accounts receivable 10,000 Taka.</li></ul>",
        meta: "Comilla Govt. College, Comilla · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm'>Capital = Cash (2,00,000) + Furniture (50,000) = <strong>2,50,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for the transactions of dates 4, 10, 18 and 27.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 4: Cash Dr 40k, Sales Cr 40k</p><p>Jan 10: Bank Dr 10k, Cash Cr 10k</p><p>Jan 18: Rent Dr 5k, Cash Cr 5k</p><p>Jan 27: Drawings Dr 7k, Bank Cr 7k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the transactions of dates 7, 15, 22 and 30 on the accounting equation.", 
                answer: "<div class='text-sm'>1. Jan 7: A/P +20k, Equity -20k<br>2. Jan 15: Machinery +25k, Cash -25k<br>3. Jan 22: A/R +24k, Equity +24k<br>4. Jan 30: Cash +10k, A/R -10k</div>" 
            }
        ]
    },
    {
        id: "26",
        stem: "<p>The following transactions and events were taken from Mr. Karim's books in June 2024:</p><ul class='list-disc ml-6 mt-2'><li>June 1: Mr. Karim started a business with cash 80,000 Taka, machinery 70,000 Taka, and a bank loan of 60,000 Taka.</li><li>June 5: Appointed an office assistant with a monthly salary of 12,000 Taka.</li><li>June 9: Provided services to a client worth 40,000 Taka and received 20,000 Taka.</li><li>June 12: Purchased supplies on credit for 5,000 Taka.</li><li>June 17: Received 9,000 Taka in advance from a client for future legal services.</li><li>June 25: Supplies used 3,000 Taka.</li><li>June 30: Paid the office assistant's salary.</li></ul>",
        meta: "Dhaka Commerce College · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (80,000) + Machinery (70,000) = <strong>1,50,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide the journal entries for the transactions (without explanation).", 
                answer: "<div class='text-xs space-y-1'><p>June 1: Cash Dr 140k, Machinery Dr 70k; Loan Cr 60k, Cap Cr 150k</p><p>June 9: Cash Dr 20k, A/R Dr 20k; Service Rev Cr 40k</p><p>June 12: Supplies Dr 5k; A/P Cr 5k</p><p>June 17: Cash Dr 9k; Unearned Rev Cr 9k</p><p>June 25: Supplies Exp Dr 3k; Supplies Cr 3k</p><p>June 30: Salary Exp Dr 12k; Cash Cr 12k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the transactions on the accounting equation in a tabular format.", 
                answer: "<div class='text-sm'>Total Assets = Liabilities + Equity = <strong>2,29,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "27",
        stem: "<p>The transactions of Mr. Bashir's business for January 2024 are as follows:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 1: Business was started with cash 6,00,000 Taka, an almirah worth 3,00,000 Taka, and a bank loan of 2,50,000 Taka.</li><li>Jan. 8: Provided services to customers worth 70,000 Taka and received 30,000 Taka.</li><li>Jan. 15: Calculator purchased 5,000 Taka.</li><li>Jan. 25: Bank loan paid 1,00,000 Taka.</li><li>Jan. 31: Supplies used 2,000 Taka.</li></ul>",
        meta: "Ispahani Public School ও College, Chittagong · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (6,00,000) + Almirah (3,00,000) = <strong>9,00,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the classification of accounts involved in the above transactions.", 
                answer: "<ul class='list-disc ml-6 text-xs text-left'><li>Jan 1: Cash (A), Furniture (A), Loan (L), Capital (OE)</li><li>Jan 8: Cash (A), A/R (A), Service Revenue (OE)</li><li>Jan 15: Furniture/Equip (A), Cash (A)</li><li>Jan 25: Loan (L), Cash (A)</li><li>Jan 31: Supplies Exp (OE), Supplies (A)</li></ul>" 
            },
            { 
                label: "c", 
                text: "Show the effect on the accounting equation using a tabular format.", 
                answer: "<div class='text-sm'>Equation Total (A = L + OE) = <strong>1,09,800 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "28",
        stem: "<p>Mr. Mushfiq started a business on January 1, 2017, with cash 50,000 Taka, goods 20,000 Taka, and a loan of 30,000 Taka. Other transactions for the month were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 5: Cash sales to Tamim 40,000 Taka.</li><li>Jan. 8: Cash purchase of furniture 10,000 Taka.</li><li>Jan. 12: Cash purchase including VAT 34,500 Taka.</li><li>Jan. 15: Purchase returns 7,000 Taka.</li><li>Jan. 20: Commission received 5,000 Taka.</li><li>Jan. 23: Goods purchased from Rubel on credit 15,000 Taka.</li><li>Jan. 27: Rent paid 12,000 Taka.</li><li>Jan. 30: Paid to Rubel 11,500 Taka in full settlement of his claim.</li></ul>",
        meta: "Comilla Commerce College · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of Mr. Mushfiq's initial capital with calculations.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (50,000) + Inventory (20,000) = <strong>70,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for the transactions of dates 12, 15, 20 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 12: Purchase Dr 30k, VAT Dr 4.5k; Cash Cr 34.5k</p><p>Jan 15: A/P Dr 7k; Purchase Return Cr 7k</p><p>Jan 20: Cash Dr 5k; Commission Cr 5k</p><p>Jan 30: A/P (Rubel) Dr 15k; Cash Cr 11.5k, Disc Rec Cr 3.5k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect on the accounting equation in a tabular format for the transactions of dates 5, 8, 23 and 27.", 
                answer: "<div class='text-sm'>1. Jan 5: Cash +40k = Equity +40k<br>2. Jan 8: Furniture +10k, Cash -10k<br>3. Jan 23: A/P +15k, Equity -15k<br>4. Jan 27: Cash -12k, Equity -12k</div>" 
            }
        ]
    },
    {
        id: "29",
        stem: "<p>Mr. Hossain started a business on May 1, 2024, with cash 1,00,000 Taka, machinery 20,000 Taka, and a bank loan of 15,000 Taka. The following transactions were completed:</p><ul class='list-disc ml-6 mt-2'><li>May 2: Cash purchase at a 10% discount on 40,000 Taka.</li><li>May 5: Goods sold on credit 30,000 Taka.</li><li>May 9: Machinery purchased through a bill for 20,000 Taka.</li><li>May 16: Sales returns 2,000 Taka.</li><li>May 19: Goods withdrawn by the owner 4,000 Taka.</li><li>May 22: Additional capital brought in 8,000 Taka.</li><li>May 25: Deposited 5,000 Taka into the bank for loan repayment.</li></ul>",
        meta: "Viqarunnisa Noon School ও College · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "What is the amount of initial capital?", 
                answer: "<div class='text-sm'>Initial Capital = Cash (1,00,000) + Machinery (20,000) = <strong>1,20,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Present the effect of transactions on the accounting equation in a table.", 
                answer: "<div class='text-sm'>Equation Total (A = L + OE) = <strong>1,62,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the transactions of dates 2, 9, 19 and 22.", 
                answer: "<div class='text-xs space-y-1'><p>May 2: Purchase Dr 36k, Cash Cr 36k</p><p>May 9: Machinery Dr 20k, Notes Payable Cr 20k</p><p>May 19: Drawings Dr 4k, Purchase Cr 4k</p><p>May 22: Cash Dr 8k, Capital Cr 8k</p></div>" 
            }
        ]
    },
    {
        id: "30",
        stem: "<p>The transactions of Eastern Repair Shop for March 2023 were as follows:</p><ul class='list-disc ml-6 mt-2'><li>March 1: Cash 72,000 Taka and equipment 25,000 Taka were invested in the business.</li><li>March 7: Purchased supplies on credit 2,000 Taka.</li><li>March 12: Provided services; received 17,000 Taka in cash and billed 6,000 Taka to clients.</li><li>March 20: Received a utility bill of 1,400 Taka to be paid next month.</li><li>March 25: Paid 12,000 Taka in advance for a 2-year insurance policy.</li><li>March 28: Paid rent for March to the landlord 4,000 Taka.</li><li>March 30: 40% of the amount due from clients was received in cash.</li><li>March 31: Owner's drawings for March were 5,000 Taka.</li></ul>",
        meta: "Dhaka Residential Model College · 2025",
        type: "college",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of net accounts receivable at the end of the month.", 
                answer: "<div class='text-sm'>Billed amount (March 12) = 6,000<br>(-) Collected 40% (March 30) = (2,400)<br><strong>Net A/R = 3,600 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of the transactions of March 1, 7, 25 and 31 on the accounting equation.", 
                answer: "<div class='text-sm'>March 1: Cash +72k, Equip +25k = Equity +97k<br>March 7: Supplies +2k = A/P +2k<br>March 25: Cash -12k, Prepaid Ins +12k<br>March 31: Cash -5k = Equity -5k</div>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the transactions of March 12, 20, 28 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>March 12: Cash Dr 17k, A/R Dr 6k; Service Rev Cr 23k</p><p>March 20: Utility Expense Dr 1,400; A/P Cr 1,400</p><p>March 28: Rent Expense Dr 4,000; Cash Cr 4,000</p><p>March 30: Cash Dr 2,400; A/R Cr 2,400</p></div>" 
            }
        ]
    }
];
