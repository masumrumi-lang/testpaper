const fullCQ_board_part1 = [
    {
        id: "b1",
        stem: "<p>Mr. Abir started a repair business on April 1, 2024, with cash 20,800 Taka and machinery worth 10,200 Taka. The following transactions were completed:</p><ul class='list-disc ml-6 mt-2'><li>April 2: Paid two months' rent 6,000 Taka.</li><li>April 3: Provided repair services: Cash 19,800 Taka; on credit 2,400 Taka.</li><li>April 6: Purchased supplies on credit 1,500 Taka.</li><li>April 9: Billed for repair services 2,000 Taka.</li><li>April 15: Owner withdrew 2,000 Taka from the business for personal use.</li><li>April 22: Received 1,500 Taka from accounts receivable.</li><li>April 25: Paid 300 Taka for entertainment expenses.</li><li>April 30: Supplies used 800 Taka.</li></ul>",
        meta: "Rajshahi · 2025",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of accounts receivable at the end of the month.", 
                answer: "<div class='text-sm font-medium'>A/R = 2,400 (April 3) + 2,000 (April 9) - 1,500 (April 22) = <strong>2,900 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the classification of accounts for the transactions of dates 2, 6, 15 and 30 using the modern method.", 
                answer: "<div class='text-xs space-y-1'><p>April 2: Prepaid Rent (Asset), Cash (Asset)</p><p>April 6: Supplies (Asset), A/P (Liability)</p><p>April 15: Drawings (Equity), Cash (Asset)</p><p>April 30: Supplies Expense (Equity), Supplies (Asset)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions on the accounting equation for dates 1, 2, 3, 22 and 25.", 
                answer: "<div class='text-sm'>Total Assets = Total Liabilities + Equity = <strong>46,900 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b2",
        stem: "<p>Mr. Jewel is a barrister. On January 1, 2024, he sold his personal savings certificate for 5,00,000 Taka and invested 3,00,000 Taka from it to start a law practice. His transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 1: Rented an office for 20,000 Taka per month and paid two months' rent in advance.</li><li>Jan. 2: Appointed an office assistant at a monthly salary of 10,000 Taka.</li><li>Jan. 6: Provided legal services to a client worth 75,000 Taka and received 50,000 Taka in cash.</li><li>Jan. 20: Received 20,000 Taka in advance from another client for a legal service contract.</li><li>Jan. 25: Provided 10,000 Taka worth of service against the advance received.</li><li>Jan. 31: Paid January salary to the assistant and recorded one month's rent as an expense.</li></ul>",
        meta: "Chittagong · 2025",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the total amount of service revenue for Mr. Jewel in January.", 
                answer: "<div class='text-sm font-medium'>Revenue = 75,000 (Jan 6) + 10,000 (Jan 25) = <strong>85,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of the above transactions on the accounting equation in a tabular format.", 
                answer: "<div class='text-sm'>Total Equation (A = L + OE) = <strong>3,55,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Prepare an income statement for Mr. Jewel for the month of January.", 
                answer: "<div class='text-sm space-y-1'><p>Service Income: 85,000</p><p>(-) Salary Exp: (10,000)</p><p>(-) Rent Exp: (20,000)</p><p><strong>Net Profit = 55,000 Taka</strong></p></div>" 
            }
        ]
    },
    {
        id: "b3",
        stem: "<p>Mr. Shawkat started a service business on January 1, 2024, with cash 2,00,000 Taka and office equipment worth 1,50,000 Taka. His transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Appointed a manager at a monthly salary of 20,000 Taka.</li><li>Jan. 8: Purchased furniture on credit for 20,000 Taka.</li><li>Jan. 10: Services provided for 30,000 Taka (40% on credit).</li><li>Jan. 15: Took a personal loan of 40,000 Taka from Prime Bank.</li><li>Jan. 20: Paid the full amount for the furniture purchased on credit.</li><li>Jan. 22: Paid office rent 15,000 Taka.</li><li>Jan. 30: Paid the manager's salary for the month of January.</li></ul>",
        meta: "Barisal · 2025",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Identify the events that are not business transactions and determine their total value.", 
                answer: "<div class='text-sm font-medium'>Manager Appointment (20,000) + Personal Loan (40,000) = <strong>60,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine the amount of Mr. Shawkat's owner's equity at the end of January 2024.", 
                answer: "<div class='text-sm font-medium'>Equity = Initial (3,50,000) + Revenue (30,000) - Rent (15,000) - Salary (20,000) = <strong>3,45,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 1, 8, 10 and 22 on the accounting equation.", 
                answer: "<div class='text-sm'>Total Assets = <strong>3,85,000 Taka</strong>; Liabilities = 20,000; Equity = 3,65,000</div>" 
            }
        ]
    },
    {
        id: "b4",
        stem: "<p>The account balances of Mr. Didarul Alam's sole proprietorship on June 30, 2024, were: Cash 70,000 Taka; Inventory 1,20,000 Taka; Accounts Receivable 60,000 Taka; Supplies 5,000 Taka and Accounts Payable 40,000 Taka. His transactions for July were:</p><ul class='list-disc ml-6 mt-2'><li>July 1: Credit sales 60,000 Taka (Cost of goods sold 45,000 Taka).</li><li>July 7: Three months' salary paid in advance to employees 15,000 Taka.</li><li>July 15: Cash collected from debtors after allowing a 3% discount, amounting to 87,300 Taka.</li><li>July 31: Adjust one month of the prepaid salary.</li></ul>",
        meta: "Dinajpur · 2025",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of capital for Mr. Didarul Alam on July 1, 2024.", 
                answer: "<div class='text-sm font-medium'>Capital = Assets (70k+120k+60k+5k) - Liabilities (40k) = <strong>2,15,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of the transactions on the accounting equation, considering the opening balances.", 
                answer: "<div class='text-sm font-medium'>Equation Balance (A = L + OE) = <strong>2,22,300 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Provide the opening journal entry and prepare an income statement for July.", 
                answer: "<div class='text-sm space-y-1'><p>Net Profit = Sales (60k) - COGS (45k) - Salary (5k) - Disc Allowed (2.7k) = <strong>7,300 Taka</strong></p></div>" 
            }
        ]
    },
    {
        id: "b5",
        stem: "<p>Mr. Jamal started a business on January 1, 2024, with cash 70,000 Taka; computer 60,000 Taka, and a bank loan of 50,000 Taka. Other transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Goods purchased from Mizan 35,000 Taka.</li><li>Jan. 5: Advance salary paid to an office worker 15,000 Taka.</li><li>Jan. 10: Paid income tax 5,000 Taka.</li><li>Jan. 15: Laptop purchased for the office 55,000 Taka.</li><li>Jan. 20: Goods withdrawn by the owner 3,000 Taka.</li><li>Jan. 25: Goods sold on credit 30,000 Taka.</li><li>Jan. 30: Paid to Mizan with a 2% discount.</li></ul>",
        meta: "Mymensingh · 2025",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of office equipment.", 
                answer: "<div class='text-sm font-medium'>Office Equipment = Computer (60,000) + Laptop (55,000) = <strong>1,15,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Identify the accounts and classify them for the transactions of Jan 2, 5, 10 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 2: Purchase (OE), A/P (L)</p><p>Jan 5: Prepaid Salary (A), Cash (A)</p><p>Jan 10: Drawings (OE), Cash (A)</p><p>Jan 30: A/P (L), Cash (A), Disc Rec (OE)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 1, 2, 15, 20, 25 and 30 on the accounting equation in a table.", 
                answer: "<div class='text-sm font-medium'>Total Equation (A = L + OE) = <strong>1,57,700 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b6",
        stem: "<p>Hakim Brothers started a business on April 1, 2024, with cash 70,000 Taka, furniture 30,000 Taka, and a bank loan of 40,000 Taka. The transactions were:</p><ul class='list-disc ml-6 mt-2'><li>April 3: Purchased goods from Rahim 20,000 Taka.</li><li>April 6: Goods sold for cash 30,000 Taka.</li><li>April 15: Salary paid to employees 8,000 Taka.</li><li>April 28: Sold old newspapers 250 Taka.</li><li>April 30: Repaid 10,000 Taka of the bank loan.</li></ul>",
        meta: "Comilla · 2025",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (70,000) + Furniture (30,000) = <strong>1,00,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine the debit and credit for the transactions of dates 1, 3, 6 and 30 using the modern method.", 
                answer: "<div class='text-xs space-y-1'><p>April 1: Cash Dr 110k; Loan Cr 40k, Capital Cr 70k</p><p>April 3: Purchase Dr 20k; A/P (Rahim) Cr 20k</p><p>April 6: Cash Dr 30k; Sales Cr 30k</p><p>April 30: Bank Loan Dr 10k; Cash Cr 10k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the above transactions on the accounting equation using a tabular format.", 
                answer: "<div class='text-sm font-medium'>Total Assets = Total Liabilities + Equity = <strong>1,42,250 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b7",
        stem: "<p>Roman started a business in Dhaka on August 1. On August 31, his balance sheet showed: Cash 9,000 Taka, A/R 1,700 Taka, Equipment 6,000 Taka, and A/P 3,600 Taka. September transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Sept. 2: Took a 10,000 Taka loan from Capital Bank by issuing a 9% note payable.</li><li>Sept. 5: Paid 2,900 Taka for accounts payable.</li><li>Sept. 10: Collected 1,300 Taka from accounts receivable.</li><li>Sept. 16: Purchased additional equipment for 2,100 Taka (800 in cash, balance on credit).</li><li>Sept. 18: Earned revenue 7,800 Taka (2,500 in cash, balance to be received in Oct).</li><li>Sept. 20: Withdrew 1,100 Taka cash for personal use.</li><li>Sept. 28: Paid salary 1,700 Taka and rent 900 Taka.</li><li>Sept. 30: Utility bill for the current month is due 470 Taka.</li><li>Sept. 30: Paid one month's interest on the note payable.</li></ul>",
        meta: "Rajshahi · 2024",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of owner's equity on August 31, 2023.", 
                answer: "<div class='text-sm font-medium'>Equity = Assets (9,000+1,700+6,000) - Liabilities (3,600) = <strong>13,100 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of transactions of Sept 2, 5, 10 and 16 on the accounting equation, starting with Aug 31 balances.", 
                answer: "<div class='text-sm font-medium'>Equation Balance (A = L + OE) = <strong>25,700 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Prepare an owner's equity statement as of Sept 30, after determining net income.", 
                answer: "<div class='text-sm font-medium'>Net Income = 4,655; Closing Equity = <strong>16,655 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b8",
        stem: "<p>Mr. Fahad started a business on January 1, 2023, with cash 1,30,000 Taka and machinery worth 80,000 Taka. His transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Paid 9,000 Taka for three months' rent.</li><li>Jan. 3: Appointed an employee at a monthly salary of 8,000 Taka.</li><li>Jan. 5: Credit sales 28,000 Taka.</li><li>Jan. 15: Purchased a piece of machinery for 25,000 Taka.</li><li>Jan. 25: 10% bad debt charged on credit sales.</li><li>Jan. 26: Owner paid 3,000 Taka income tax from his personal fund.</li><li>Jan. 27: Depreciation on machinery was charged at 2,700 Taka.</li><li>Jan. 28: Credit purchase 12,000 Taka.</li><li>Jan. 31: Paid 1,500 Taka for advertising.</li></ul>",
        meta: "Barisal · 2024",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Identify the events that are not transactions.", 
                answer: "<div class='text-sm font-medium'>Employee appointment with salary 8,000 Taka.</div>" 
            },
            { 
                label: "b", 
                text: "Classify the transactions of Jan 2, 5, 25 and 27 using the modern method.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 2: Prepaid Rent (A), Cash (A)</p><p>Jan 5: A/R (A), Sales (OE)</p><p>Jan 25: Bad Debt (OE), A/R (A)</p><p>Jan 27: Depreciation (OE), Accum. Depr (Contra-A)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 1, 15, 28 and 31 on the accounting equation.", 
                answer: "<div class='text-sm font-medium'>Total Assets = <strong>2,45,500 Taka</strong>; Liabilities = 12,000; Equity = 2,33,500</div>" 
            }
        ]
    },
    {
        id: "b9",
        stem: "<p>Mr. Hriday is a lawyer. His transactions for January 2024 were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 1: Invested 50,000 Taka into the law practice.</li><li>Jan. 1: Appointed a law assistant at a monthly salary of 10,000 Taka.</li><li>Jan. 3: Received 10,000 Taka cash for providing legal services.</li><li>Jan. 7: Purchased office equipment on credit for 25,000 Taka.</li><li>Jan. 10: Paid daughter's school fees 4,000 Taka from personal fund.</li><li>Jan. 15: Paid rent for January 7,000 Taka.</li><li>Jan. 22: Paid 10,000 Taka against the Jan 7 purchase.</li><li>Jan. 31: Paid the law assistant's salary.</li></ul>",
        meta: "Dinajpur · 2024",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Identify events that are not transactions.", 
                answer: "<div class='text-sm font-medium'>Assistant appointment (10,000) + Daughter's fees (4,000) = <strong>14,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of transactions from Jan 1 to Jan 15 on accounting equation elements.", 
                answer: "<div class='text-sm font-medium'>Total Assets = <strong>78,000 Taka</strong>; Liabilities = 25,000; Equity = 53,000</div>" 
            },
            { 
                label: "c", 
                text: "Mention the related accounts and classification for each transaction.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 1: Cash (A), Capital (OE)</p><p>Jan 3: Cash (A), Service Fee (OE)</p><p>Jan 7: Office Equip (A), A/P (L)</p><p>Jan 15: Rent Exp (OE), Cash (A)</p></div>" 
            }
        ]
    },
    {
        id: "b10",
        stem: "<p>Mr. Mamun started a business on January 1, 2022, with cash 80,000 Taka and machinery worth 40,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Opened a bank account with 30,000 Taka.</li><li>Jan. 5: Placed an order for goods worth 5,000 Taka.</li><li>Jan. 8: Appointed an accountant at a salary of 8,000 Taka.</li><li>Jan. 10: Purchased supplies on credit for 5,000 Taka.</li><li>Jan. 12: Paid rent in cash 800 Taka.</li><li>Jan. 20: Purchased goods on credit for 10,000 Taka.</li><li>Jan. 25: Withdrew 500 Taka in cash for personal use.</li><li>Jan. 31: Sold goods for 8,000 Taka.</li></ul>",
        meta: "Rajshahi · 2023",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Identify events that are not transactions.", 
                answer: "<div class='text-sm font-medium'>Order placement (5,000) + Accountant appointment = <strong>5,000+ Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Mention accounts involved from Jan 1 to 12 and their normal balances.", 
                answer: "<div class='text-xs space-y-1'><p>Cash (Debit), Machinery (Debit), Capital (Credit)</p><p>Bank (Debit), Supplies (Debit), A/P (Credit)</p><p>Rent Expense (Debit)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the above transactions on the accounting equation using a table.", 
                answer: "<div class='text-sm font-medium'>Equation Balance (A = L + OE) = <strong>1,36,700 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b11",
        stem: "<p>Mr. Shakil started a business on June 1, 2022, with cash 80,000 Taka, office equipment 70,000 Taka, and a bank loan of 40,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>June 2: Goods purchased for cash 10,000 Taka.</li><li>June 4: Paid income tax 2,000 Taka.</li><li>June 6: Salary paid to office staff 8,000 Taka.</li><li>June 10: Laptop purchased for office 30,000 Taka.</li><li>June 15: Goods withdrawn for personal use 3,000 Taka.</li><li>June 28: Goods sold for cash 20,000 Taka.</li></ul>",
        meta: "Jessore · 2023",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the total amount of drawings for Mr. Shakil.", 
                answer: "<div class='text-sm font-medium'>Total Drawings = Income Tax (2,000) + Goods Withdrawal (3,000) = <strong>5,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Identify the accounts and classify them for the transactions of June 2, 4, 10 and 28.", 
                answer: "<div class='text-xs space-y-1'><p>June 2: Purchase (Equity), Cash (Asset)</p><p>June 4: Drawings (Equity), Cash (Asset)</p><p>June 10: Office Equipment (Asset), Cash (Asset)</p><p>June 28: Cash (Asset), Sales (Equity)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 1, 6, 10 and 28 on the accounting equation in a table.", 
                answer: "<table class='w-full text-xs border mt-2'><tr><th class='border p-1'>Date</th><th class='border p-1'>Assets</th><th class='border p-1'>=</th><th class='border p-1'>Liab.</th><th class='border p-1'>+</th><th class='border p-1'>Equity</th></tr><tr><td class='border p-1'>June 1</td><td class='border p-1'>1,90,000</td><td class='border p-1'>=</td><td class='border p-1'>40,000</td><td class='border p-1'>+</td><td class='border p-1'>1,50,000</td></tr><tr><td class='border p-1'>June 6</td><td class='border p-1'>(8,000)</td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1'>(8,000)</td></tr><tr><td class='border p-1'>June 10</td><td class='border p-1'>+30k/-30k</td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1'></td></tr><tr><td class='border p-1'>June 28</td><td class='border p-1'>20,000</td><td class='border p-1'>=</td><td class='border p-1'></td><td class='border p-1'>+</td><td class='border p-1'>20,000</td></tr></table><div class='mt-1 font-bold'>Final Total: 2,02,000 Taka</div>" 
            }
        ]
    },
    {
        id: "b12",
        stem: "<p>Mr. Mannan started a business on January 1, 2022, with cash 1,00,000 Taka. Transactions for the month were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 3: Cash purchase 20,000 Taka.</li><li>Jan. 7: Credit purchase from Rahim 30,000 Taka.</li><li>Jan. 10: Credit sales 80,000 Taka.</li><li>Jan. 14: Goods withdrawn for personal use 4,000 Taka.</li><li>Jan. 18: Stationery purchase 5,000 Taka.</li><li>Jan. 30: Furniture purchased for office use 30,000 Taka (80% on credit).</li></ul>",
        meta: "Sylhet · 2023",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of cash paid for the furniture purchase.", 
                answer: "<div class='text-sm font-medium'>Furniture Cash Portion (20%) = 30,000 × 0.20 = <strong>6,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine the amount of owner's equity at the end of the month.", 
                answer: "<div class='text-sm font-medium'>Equity = 1,00,000 (Initial) + 80,000 (Sales) - 20,000 (Purchase) - 30,000 (Credit Purchase) - 5,000 (Stationery) - 4,000 (Drawings) = <strong>1,21,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 1, 3, 10 and 30 on the accounting equation in a table.", 
                answer: "<div class='text-sm font-bold'>Total Assets = Total Liabilities + Equity = <strong>2,04,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b13",
        stem: "<p>Mr. Rahman started a business on June 1, 2022, with bank balance 20,000 Taka, cash 30,000 Taka, accounts payable 14,000 Taka, and furniture 15,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>June 3: Bank loan taken 10,000 Taka.</li><li>June 8: Cash purchase of machinery 5,000 Taka.</li><li>June 13: Goods sold for 20,000 Taka (12,000 received in cash).</li><li>June 17: Salary paid 6,000 Taka.</li><li>June 22: Cash purchase 4,000 Taka.</li><li>June 30: Invested 20,000 Taka at 10% interest.</li></ul>",
        meta: "Dhaka · 2023",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "What is the amount of Mr. Rahman's liability in this month?", 
                answer: "<div class='text-sm font-medium'>Liability = Accounts Payable (14,000) + Bank Loan (10,000) = <strong>24,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of transactions of dates 1, 17, 22 and 30 on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Total Equation (A = L + OE) = <strong>75,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Determine the amount of Mr. Rahman's owner's equity at the end of the month.", 
                answer: "<div class='text-sm font-medium'>Equity = Opening (51,000) + Revenue (20,000) - Salary (6,000) - Purchase (4,000) = <strong>61,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b14",
        stem: "<p>Mr. Jasim started a business on July 1, 2022, with cash 50,000 Taka and a computer worth 30,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>July 3: Cash purchase 25,000 Taka.</li><li>July 7: Office equipment purchase 15,000 Taka.</li><li>July 9: Cash sales 50,000 Taka.</li><li>July 16: Purchase from Shahin 35,000 Taka.</li><li>July 18: Sales to Fahim 45,000 Taka.</li><li>July 27: Paid to creditor 30,000 Taka.</li><li>July 28: Collected from accounts receivable 25,000 Taka.</li><li>July 30: Salary paid to employees 10,500 Taka.</li></ul>",
        meta: "Barisal · 2023",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (50,000) + Computer (30,000) = <strong>80,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of the above transactions on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Equation Total (A = L + OE) = <strong>1,09,500 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Prepare an income statement for the month of July.", 
                answer: "<table class='w-full text-xs border mt-2'><tr><td class='border p-1'>Sales (50,000 + 45,000)</td><td class='border p-1'>95,000</td></tr><tr><td class='border p-1'>(-) Purchases (25,000 + 35,000)</td><td class='border p-1'>(60,000)</td></tr><tr><td class='border p-1'>(-) Salary Expense</td><td class='border p-1'>(10,500)</td></tr><tr><td class='border p-1 font-bold'>Net Profit</td><td class='border p-1 font-bold'>24,500 Taka</td></tr></table>" 
            }
        ]
    },
    {
        id: "b15",
        stem: "<p>Saberi Rahman started a business on June 1, 2022, with cash 25,000 Taka, furniture 20,000 Taka, and goods worth 7,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>June 2: Purchased chairs and tables for business 20,000 Taka.</li><li>June 4: Purchased goods from Zakir 7,000 Taka.</li><li>June 7: Sold goods to Rabbi 22,000 Taka.</li><li>June 12: Gave a loan to Suma 15,000 Taka.</li><li>June 25: Received 2,000 Taka from Rabbi.</li><li>June 27: Recovered 5,000 Taka of the loan from Suma.</li><li>June 30: Paid salary to employee Kamal 3,000 Taka.</li></ul>",
        meta: "Chittagong · 2023",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (25,000) + Furniture (20,000) + Inventory (7,000) = <strong>52,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Classify and determine Debit/Credit for transactions of June 1, 4, 12 and 30 using the modern method.", 
                answer: "<div class='text-xs space-y-1'><p>June 1: Cash Dr, Furniture Dr, Inventory Dr; Capital Cr</p><p>June 4: Purchase Dr; A/P (Zakir) Cr</p><p>June 12: Loan Given Dr; Cash Cr</p><p>June 30: Salary Exp Dr; Cash Cr</p></div>" 
            },
            { 
                label: "c", 
                text: "Present the effect of the above transactions on the accounting equation in a table.", 
                answer: "<div class='text-sm font-bold'>Total Assets = Total Liabilities + Equity = <strong>71,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b16",
        stem: "<p>Mr. Russell started a business on July 1, 2022, with cash 1,20,000 Taka and furniture worth 10,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>July 2: Purchased furniture for cash 10,000 Taka.</li><li>July 4: Purchased goods from Raihan on credit 5,000 Taka.</li><li>July 5: Rented a house for the office at a monthly rent of 30,000 Taka.</li><li>July 6: Sold goods to Arif on credit 6,000 Taka.</li><li>July 7: Appointed an accountant at a monthly salary of 40,000 Taka.</li><li>July 10: Took a loan of 12,000 Taka from Jamal.</li><li>July 25: 2,000 Taka due from Arif will no longer be collected.</li><li>July 28: Paid salary to employee Rafiq 4,000 Taka.</li><li>July 30: Paid 5,000 Taka to Jamal against the loan.</li></ul>",
        meta: "Dinajpur · 2023",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the total amount of events that are not transactions.", 
                answer: "<div class='text-sm font-medium'>House Rental (30,000) + Accountant Appointment (40,000) = <strong>70,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Identify the accounts and classify them for the transactions of July 10, 25, 28 and 30 using the modern method.", 
                answer: "<div class='text-xs space-y-1'><p>July 10: Cash (Asset), Jamal's Loan (Liability)</p><p>July 25: Bad Debt (Equity), A/R (Asset)</p><p>July 28: Salary Expense (Equity), Cash (Asset)</p><p>July 30: Jamal's Loan (Liability), Cash (Asset)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of July 1, 2, 4 and 6 on the accounting equation using a statement table.", 
                answer: "<div class='text-sm font-bold'>Total Assets = Total Liabilities + Equity = <strong>1,36,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b17",
        stem: "<p>Sonali Traders started a business on January 1, 2021, with cash 1,50,000 Taka, furniture 30,000 Taka, and a loan of 70,000 Taka. Other transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 5: Purchased goods for 48,000 Taka.</li><li>Jan. 12: Sold goods on credit for 35,000 Taka.</li><li>Jan. 19: Owner's drawings 6,000 Taka.</li><li>Jan. 25: Paid rent 15,000 Taka.</li><li>Jan. 30: Received commission 3,000 Taka.</li></ul>",
        meta: "Dhaka · 2022",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital for Sonali Traders.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (1,50,000) + Furniture (30,000) = <strong>1,80,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine Debit and Credit for transactions of January 1, 12, 19 and 30 with reasons.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 1: Cash Dr 220k, Furn Dr 30k; Loan Cr 70k, Cap Cr 180k</p><p>Jan 12: A/R Dr 35k; Sales Cr 35k</p><p>Jan 19: Drawings Dr 6k; Cash Cr 6k</p><p>Jan 30: Cash Dr 3k; Commission Cr 3k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of Jan 1, 5, 12 and 19 on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Equation Total (A = L + OE) = <strong>2,31,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b18",
        stem: "<p>Mr. Zahed Iqbal started a business on Jan 1, 2021, with cash 30,000 Taka and furniture worth 20,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Purchased goods for 25,000 Taka (10,000 in cash, balance on credit).</li><li>Jan. 10: Paid carriage inwards 700 Taka.</li><li>Jan. 15: Purchase returns 1,000 Taka.</li><li>Jan. 20: Sold goods on credit for 22,000 Taka.</li><li>Jan. 30: Paid salary 2,000 Taka.</li></ul>",
        meta: "Rajshahi · 2022",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of net purchase.", 
                answer: "<div class='text-sm font-medium'>Net Purchase = Purchase (25,000) + Carriage (700) - Returns (1,000) = <strong>24,700 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare journal entries for the transactions of Jan 2, 10, 20 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 2: Purchase Dr 25k; Cash Cr 10k, A/P Cr 15k</p><p>Jan 10: Carriage Dr 700; Cash Cr 700</p><p>Jan 20: A/R Dr 22k; Sales Cr 22k</p><p>Jan 30: Salary Dr 2k; Cash Cr 2k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions on the accounting equation in a tabular format.", 
                answer: "<div class='text-sm font-bold'>Equation Balance (A = L + OE) = <strong>64,300 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b19",
        stem: "<p>Mr. Kamal started a business on Jan 1, 2021, with cash 50,000 Taka, goods 20,000 Taka, and a loan of 30,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 5: Cash sales to Tamim 40,000 Taka.</li><li>Jan. 8: Cash purchase of furniture 10,000 Taka.</li><li>Jan. 12: Cash purchase with VAT 34,500 Taka.</li><li>Jan. 15: Purchase returns (Outward) 7,000 Taka.</li><li>Jan. 20: Received commission 5,000 Taka.</li><li>Jan. 23: Goods purchased from Rubel on credit 15,000 Taka.</li><li>Jan. 27: Paid rent 12,000 Taka.</li><li>Jan. 30: Paid to Rubel 11,500 Taka in full settlement of his claim.</li></ul>",
        meta: "Jessore · 2022",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine Mr. Kamal's initial capital with calculations.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (50,000) + Inventory (20,000) = <strong>70,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for the transactions of dates 12, 15, 20 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 12: Purchase Dr 30k, VAT Dr 4.5k; Cash Cr 34.5k</p><p>Jan 15: A/P Dr 7k; Purchase Return Cr 7k</p><p>Jan 20: Cash Dr 5k; Commission Cr 5k</p><p>Jan 30: A/P (Rubel) Dr 15k; Cash Cr 11.5k, Disc Rec Cr 3.5k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 5, 8, 23 and 27 on the accounting equation using a table.", 
                answer: "<div class='text-sm font-bold'>Final Equation Total = <strong>1,13,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b20",
        stem: "<p>The account balances of Shatabdi Traders on June 30, 2021, were: Cash 40,000 Taka; Office Equipment 50,000 Taka; Accounts Receivable 30,000 Taka; Accounts Payable 20,000 Taka. July transactions were:</p><ul class='list-disc ml-6 mt-2'><li>July 2: Owner invested cash 50,000 Taka and office equipment worth 25,000 Taka.</li><li>July 5: Purchased goods for 50,000 Taka (60% cash, 40% on credit).</li><li>July 10: Paid salary 20,000 Taka.</li><li>July 15: Paid for the credit purchase made on July 5.</li><li>July 20: Sold goods for 1,00,000 Taka (80% cash, 20% on credit).</li><li>July 30: Paid rent 25,000 Taka.</li></ul>",
        meta: "Comilla · 2022",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Provide the opening journal entry for Shatabdi Traders.", 
                answer: "<div class='text-xs space-y-1'><p>Cash Dr 40,000, Office Equip Dr 50,000, A/R Dr 30,000</p><p>Accounts Payable Cr 20,000, Capital Cr 1,00,000</p></div>" 
            },
            { 
                label: "b", 
                text: "Prepare journal entries for the transactions of July 2, 5, 15 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>July 2: Cash Dr 50k, Office Equip Dr 25k; Capital Cr 75k</p><p>July 5: Purchase Dr 50k; Cash Cr 30k, A/P Cr 20k</p><p>July 15: A/P Dr 20k; Cash Cr 20k</p><p>July 30: Rent Dr 25k; Cash Cr 25k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of all the above transactions on the accounting equation using a table.", 
                answer: "<div class='text-sm font-bold'>Total Assets = Total Liabilities + Equity = <strong>2,30,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b21",
        stem: "<p>Miss Ahona started a business on March 1, 2022, with cash 70,000 Taka, machinery 30,000 Taka, and a loan of 40,000 Taka from Rima. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>March 2: Cash purchase with 15% VAT, total 69,000 Taka.</li><li>March 7: Cash sales to Rajib 70,000 Taka.</li><li>March 10: Purchase returns (Outward) 6,000 Taka.</li><li>March 18: Purchased a laptop for 30,000 Taka.</li><li>March 20: Sold goods to Arif on credit 20,000 Taka.</li><li>March 26: Paid rent 10,000 Taka.</li><li>March 31: Received 19,000 Taka from Arif in full settlement of his claim.</li></ul>",
        meta: "Barisal · 2022",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the initial capital of Miss Ahona's business.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (70,000) + Machinery (30,000) = <strong>1,00,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for transactions of dates 2, 10, 20 and 31 (without explanation).", 
                answer: "<div class='text-xs space-y-1'><p>March 2: Purchase Dr 60k, VAT Dr 9k; Cash Cr 69k</p><p>March 10: A/P Dr 6k; Purchase Return Cr 6k</p><p>March 20: A/R Dr 20k; Sales Cr 20k</p><p>March 31: Cash Dr 19k, Disc Allowed Dr 1k; A/R Cr 20k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 1, 7, 18 and 26 on the accounting equation using a table.", 
                answer: "<div class='text-sm font-bold'>Final Equation Total (A = L + OE) = <strong>1,60,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b22",
        stem: "<p>Mr. Hasib started a business on January 1, 2020, with cash 50,000 Taka, machinery 70,000 Taka, and furniture 30,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 3: Cash purchase 20,000 Taka.</li><li>Jan. 6: Opened a current account in Sonali Bank with 5,000 Taka.</li><li>Jan. 8: Sold goods to Tanzila for 50,000 Taka; 50% received in cash and 50% by check.</li><li>Jan. 14: Paid life insurance premium 2,000 Taka.</li><li>Jan. 18: Deposited Tanzila's check into the bank.</li><li>Jan. 23: Withdrew 2,000 Taka from the bank.</li><li>Jan. 31: Bank allowed interest 1,500 Taka.</li></ul>",
        meta: "Mymensingh · 2022",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "What is the amount of initial capital?", 
                answer: "<div class='text-sm font-medium'>Initial Capital = 50,000 + 70,000 + 30,000 = <strong>1,50,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine Debit and Credit for transactions of January 1, 8, 14 and 18.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 1: Cash/Machinery/Furn Dr; Capital Cr</p><p>Jan 8: Cash/Check Dr; Sales Cr</p><p>Jan 14: Drawings Dr; Cash Cr</p><p>Jan 18: Bank Dr; Check Cr</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 1, 6, 8, 23 and 31 on the accounting equation in a table.", 
                answer: "<div class='text-sm font-bold'>Total Assets = Total Liabilities + Equity = <strong>2,01,500 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b23",
        stem: "<p>Mintu Brothers started a business on January 1, 2021, with cash 1,80,000 Taka, furniture 70,000 Taka, and a loan of 60,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Purchased goods from Ashik 25,000 Taka.</li><li>Jan. 7: Opened a current account in Sonali Bank with 50,000 Taka.</li><li>Jan. 10: Purchased a new almirah on credit for 45,000 Taka.</li><li>Jan. 15: Sold goods to Tuhin for cash 12,000 Taka.</li><li>Jan. 18: Paid 24,000 Taka to Ashik in full settlement of his claim.</li><li>Jan. 30: Received interest on investment 6,000 Taka.</li></ul>",
        meta: "Chittagong · 2022",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital for Mintu Brothers.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (1,80,000) + Furniture (70,000) = <strong>2,50,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare journal entries for transactions of January 1, 2, 15 and 18.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 1: Cash Dr 240k, Furn Dr 70k; Loan Cr 60k, Cap Cr 250k</p><p>Jan 2: Purchase Dr 25k; A/P Cr 25k</p><p>Jan 15: Cash Dr 12k; Sales Cr 12k</p><p>Jan 18: A/P Dr 25k; Cash Cr 24k, Disc Rec Cr 1k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of Jan 1, 7, 10 and 30 on the accounting equation in a table.", 
                answer: "<div class='text-sm font-bold'>Equation Balance (A = L + OE) = <strong>3,61,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b24",
        stem: "<p>The transactions of Rohan Traders for January 2021 were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 1: Started business with bank balance 65,000 Taka, cash 70,000 Taka, and a loan of 40,000 Taka.</li><li>Jan. 5: Purchased goods from Kabir on credit 25,000 Taka.</li><li>Jan. 7: Sold goods to Monir for 35,000 Taka.</li><li>Jan. 9: Cash sales 30,000 Taka.</li><li>Jan. 17: Received a check from Kabir 10,000 Taka.</li><li>Jan. 19: Distributed goods for free 4,000 Taka.</li><li>Jan. 31: Bank allowed interest 2,000 Taka.</li></ul>",
        meta: "Sylhet · 2022",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the net purchase amount for Rohan Traders.", 
                answer: "<div class='text-sm font-medium'>Net Purchase = Purchase (25,000) - Free distribution (4,000) = <strong>21,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Identify the accounts involved in transactions of January 1, 17, 19 and 31.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 1: Cash, Bank, Loan, Capital</p><p>Jan 17: Bank, A/R (Kabir)</p><p>Jan 19: Advertising, Purchase</p><p>Jan 31: Bank, Bank Interest</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the above transactions on the accounting equation using a statement table.", 
                answer: "<div class='text-sm font-bold'>Total Assets = Total Liabilities + Equity = <strong>2,02,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b25",
        stem: "<p>Mr. Khokon started a 'Mobile Servicing Center' on January 1, 2021, with cash 40,000 Taka and spare parts worth 10,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Paid shop rent 4,000 Taka in cash.</li><li>Jan. 10: Purchased a machine for 50,000 Taka; paid 20,000 Taka in cash and issued a note payable for the balance.</li><li>Jan. 15: Paid one year's insurance premium 2,400 Taka.</li><li>Jan. 18: Newspaper advertisement 2,000 Taka (not yet paid).</li><li>Jan. 31: Received 24,000 Taka for mobile services provided this month.</li></ul>",
        meta: "Dinajpur · 2022",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial assets.", 
                answer: "<div class='text-sm font-medium'>Initial Assets = Cash (40,000) + Spare Parts (10,000) = <strong>50,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the classification of accounts for Jan 2, 10, 15 and 18 using the modern method.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 2: Rent Exp (Equity), Cash (Asset)</p><p>Jan 10: Machinery (Asset), Cash (Asset), Notes Payable (Liability)</p><p>Jan 15: Prepaid Insurance (Asset), Cash (Asset)</p><p>Jan 18: Advertising Exp (Equity), A/P (Liability)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of Jan 1, 2, 10 and 31 on the accounting equation using a table.", 
                answer: "<div class='text-sm font-bold'>Equation Total (A = L + OE) = <strong>1,00,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b26",
        stem: "<p>The transactions of Eastern Repair Shop for March 2021 were:</p><ul class='list-disc ml-6 mt-2'><li>March 1: Invested cash 72,000 Taka and equipment 25,000 Taka.</li><li>March 7: Purchased supplies on credit 2,000 Taka.</li><li>March 12: Received 17,000 Taka for services and billed customers for 6,000 Taka.</li><li>March 20: Received utility bill 1,400 Taka (to be paid next month).</li><li>March 25: Paid 12,000 Taka for 2-year insurance premium in advance.</li><li>March 28: Paid rent 4,000 Taka to the landlord.</li><li>March 30: Received 40% of the amount due from customers in cash.</li><li>March 31: Owner's drawings 5,000 Taka.</li></ul>",
        meta: "Rajshahi · 2021",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of net accounts receivable at the end of the month.", 
                answer: "<div class='text-sm font-medium'>Net A/R = Billed (6,000) - Collected (40% of 6,000 = 2,400) = <strong>3,600 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of transactions of March 1, 7, 25 and 31 on the accounting equation in a table.", 
                answer: "<div class='text-sm font-bold'>Equation Balance (A = L + OE) = <strong>94,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the transactions of March 12, 20, 28 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>March 12: Cash Dr 17k, A/R Dr 6k; Service Rev Cr 23k</p><p>March 20: Utility Exp Dr 1.4k; A/P Cr 1.4k</p><p>March 28: Rent Exp Dr 4k; Cash Cr 4k</p><p>March 30: Cash Dr 2.4k; A/R Cr 2.4k</p></div>" 
            }
        ]
    },
    {
        id: "b27",
        stem: "<p>Mr. Monirul owns a shop. On May 1, 2020, his account balances were: Cash 40,000 Taka; Accounts Receivable 70,000 Taka; Inventory 60,000 Taka; Accounts Payable 30,000 Taka. May transactions were:</p><ul class='list-disc ml-6 mt-2'><li>May 3: Purchased goods: Cash 30,000 Taka, Credit 25,000 Taka.</li><li>May 13: Sold goods: Cash 30,000 Taka, Credit 20,000 Taka.</li><li>May 20: Appointed a salesman at a monthly salary of 10,000 Taka.</li><li>May 31: Paid rent 5,000 Taka.</li></ul>",
        meta: "Comilla · 2021",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the capital on May 1, 2020.", 
                answer: "<div class='text-sm font-medium'>Capital = Assets (40k+70k+60k) - Liabilities (30k) = <strong>1,40,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of transactions on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Final Equation Balance = <strong>1,30,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the above transactions.", 
                answer: "<div class='text-xs space-y-1'><p>May 3: Purchase Dr 55k; Cash Cr 30k, A/P Cr 25k</p><p>May 13: Cash Dr 30k, A/R Dr 20k; Sales Cr 50k</p><p>May 31: Rent Exp Dr 5k; Cash Cr 5k</p></div>" 
            }
        ]
    },
    {
        id: "b28",
        stem: "<p>Mr. Dulal is a Civil Engineer. On Jan 1, 2020, he started a service firm with cash 1,50,000 Taka, furniture worth 20,000 Taka, and a loan of 10,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Services provided on credit 25,000 Taka.</li><li>Jan. 5: Purchased supplies on credit 2,000 Taka.</li><li>Jan. 16: Paid rent 5,000 Taka.</li><li>Jan. 31: Repaid 5,000 Taka of the loan.</li></ul>",
        meta: "Jessore · 2021",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (1,50,000) + Furniture (20,000) = <strong>1,70,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare journal entries for the transactions.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 1: Cash Dr 160k, Furn Dr 20k; Loan Cr 10k, Cap Cr 170k</p><p>Jan 2: A/R Dr 25k; Service Rev Cr 25k</p><p>Jan 5: Supplies Dr 2k; A/P Cr 2k</p><p>Jan 16: Rent Dr 5k; Cash Cr 5k</p><p>Jan 31: Loan Dr 5k; Cash Cr 5k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions on the accounting equation through tabular analysis.", 
                answer: "<div class='text-sm font-bold'>Equation Balance (A = L + OE) = <strong>1,92,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b29",
        stem: "<p>Mr. Masud started a business on Jan 1, 2020, with cash 1,00,000 Taka and furniture worth 70,000 Taka. Jan transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 3: Cash sales 30,000 Taka.</li><li>Jan. 5: Purchased goods from Mr. Rahim 1,500 Taka.</li><li>Jan. 10: Deposited 12,000 Taka into the bank.</li><li>Jan. 12: Purchased furniture for 17,000 Taka.</li><li>Jan. 19: Paid for advertising 5,000 Taka.</li><li>Jan. 28: Sold old furniture for 1,000 Taka.</li><li>Jan. 31: Withdrew 25,000 Taka from the bank.</li></ul>",
        meta: "Chittagong · 2021",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "What is the amount of initial capital?", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (1,00,000) + Furniture (70,000) = <strong>1,70,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for Jan 3, 10, 19 and 28 (without explanation).", 
                answer: "<div class='text-xs space-y-1'><p>Jan 3: Cash Dr 30k; Sales Cr 30k</p><p>Jan 10: Bank Dr 12k; Cash Cr 12k</p><p>Jan 19: Advertising Dr 5k; Cash Cr 5k</p><p>Jan 28: Cash Dr 1k; Furniture Cr 1k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 1, 5, 12 and 31 on the accounting equation using a table.", 
                answer: "<div class='text-sm font-bold'>Equation Total (A = L + OE) = <strong>1,70,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b30",
        stem: "<p>Mr. Azraf started a business on June 1, 2020, with cash 40,000 Taka, goods worth 12,000 Taka, and a bank balance of 30,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>June 4: Sold goods to Babul for cash 25,000 Taka.</li><li>June 7: Purchased office equipment for cash 10,000 Taka.</li><li>June 10: Cash purchase 30,000 Taka.</li><li>June 14: Purchase returns 6,000 Taka.</li><li>June 18: Received commission 5,000 Taka.</li><li>June 28: Purchased goods from Sumi on credit 12,000 Taka.</li><li>June 29: Paid rent in cash 10,000 Taka.</li><li>June 30: Paid 10,500 Taka to Sumi in full settlement of her claim.</li></ul>",
        meta: "Barisal · 2021",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the initial capital for Mr. Azraf.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (40k) + Inventory (12k) + Bank (30k) = <strong>82,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for transactions of dates 10, 14, 18 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>June 10: Purchase Dr 30k; Cash Cr 30k</p><p>June 14: Cash Dr 6k; Purchase Return Cr 6k</p><p>June 18: Cash Dr 5k; Commission Cr 5k</p><p>June 30: A/P (Sumi) Dr 12k; Cash Cr 10.5k, Disc Rec Cr 1.5k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 4, 7, 28 and 29 on the accounting equation in a table.", 
                answer: "<div class='text-sm font-bold'>Equation Balance (A = L + OE) = <strong>1,09,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b31",
        stem: "<p>Mr. Bashir started a business on January 1, 2020, with cash 40,000 Taka, furniture 30,000 Taka, and a bank loan of 20,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan 2: Purchased goods on credit 50,000 Taka.</li><li>Jan 5: Cash sales 80,000 Taka.</li><li>Jan 7: Paid shop rent 10,000 Taka.</li><li>Jan 10: Sold goods on credit 30,000 Taka.</li><li>Jan 12: Purchased furniture for cash 5,000 Taka.</li><li>Jan 31: Paid salary to employees 15,000 Taka.</li></ul>",
        meta: "Sylhet · 2021",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine Mr. Bashir's initial capital on January 1, 2020.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (40,000) + Furniture (30,000) = <strong>70,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for the transactions of Jan 2, 7, 10 and 12.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 2: Purchase Dr 50k; A/P Cr 50k</p><p>Jan 7: Rent Exp Dr 10k; Cash Cr 10k</p><p>Jan 10: A/R Dr 30k; Sales Cr 30k</p><p>Jan 12: Furniture Dr 5k; Cash Cr 5k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 1, 2, 10 and 31 on the accounting equation using a table.", 
                answer: "<div class='text-sm font-bold'>Final Equation Balance (A = L + OE) = <strong>1,25,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b32",
        stem: "<p>Mr. Milton started a service business on January 1, 2021, with cash 1,50,000 Taka and office equipment worth 40,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 3: Paid four months' rent 8,000 Taka.</li><li>Jan. 5: Service provided for cash 25,000 Taka and on credit 15,000 Taka.</li><li>Jan. 7: Purchased office supplies on credit 4,000 Taka.</li><li>Jan. 8: Appointed a manager at a monthly salary of 20,000 Taka.</li><li>Jan. 10: Paid insurance premium 2,000 Taka.</li><li>Jan. 15: Paid the amount due from the Jan 7 transaction.</li><li>Jan. 20: Paid 5,000 Taka for advertising.</li><li>Jan. 31: Depreciation on office equipment 500 Taka.</li></ul>",
        meta: "Dinajpur · 2021",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Identify the non-cash transactions.", 
                answer: "<div class='text-sm font-medium'>Non-cash Transaction: Depreciation on Office Equipment = <strong>500 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of transactions of Jan 1, 5, 7 and 15 on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Total Assets = Total Liabilities + Equity = <strong>2,34,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Journalize the transactions of January 3, 7, 15 and 31.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 3: Prepaid Rent Dr 8k; Cash Cr 8k</p><p>Jan 7: Office Supplies Dr 4k; A/P Cr 4k</p><p>Jan 15: A/P Dr 4k; Cash Cr 4k</p><p>Jan 31: Depreciation Exp Dr 500; Acc. Depreciation Cr 500</p></div>" 
            }
        ]
    },
    {
        id: "b33",
        stem: "<p>Rahim Brothers started a business on Jan 1, 2020, with cash 50,000 Taka, furniture 30,000 Taka, and bank balance 20,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan 2: Purchased goods from Rabbi for 15,000 Taka.</li><li>Jan 8: Sold goods for 20,000 Taka.</li><li>Jan 10: Paid salary 5,000 Taka.</li><li>Jan 20: Bank charged 300 Taka for services.</li></ul>",
        meta: "Mymensingh · 2021",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (50k) + Furniture (30k) + Bank (20k) = <strong>1,00,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for the transactions of Jan 2, 8, 10 and 20.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 2: Purchase Dr 15k; A/P (Rabbi) Cr 15k</p><p>Jan 8: Cash Dr 20k; Sales Cr 20k</p><p>Jan 10: Salary Dr 5k; Cash Cr 5k</p><p>Jan 20: Bank Charges Dr 300; Bank Cr 300</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of Jan 1, 2, 8 and 10 on the accounting equation using a table.", 
                answer: "<div class='text-sm font-bold'>Equation Balance (A = L + OE) = <strong>1,30,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b34",
        stem: "<p>Mr. Kamal started a business in January 2018 with cash 1,00,000 Taka and furniture worth 50,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 3: Deposited 20,000 Taka into Sonali Bank.</li><li>Jan. 5: Paid income tax 10,000 Taka.</li><li>Jan. 10: Purchase 60,000 Taka (60% cash, 40% on credit).</li><li>Jan. 12: Credit sales 25,000 Taka (Terms 2/10, n/30).</li><li>Jan. 15: Paid life insurance premium 5,000 Taka.</li><li>Jan. 22: Received the amount due from Jan 12 credit sales.</li><li>Jan. 25: Paid the liability from Jan 10 purchase.</li></ul>",
        meta: "Chittagong · 2019",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital for Mr. Kamal.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (1,00,000) + Furniture (50,000) = <strong>1,50,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries with explanation for Jan 5, 12, 15 and 22.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 5: Drawings Dr 10k; Cash Cr 10k (Tax paid)</p><p>Jan 12: A/R Dr 25k; Sales Cr 25k (Credit sales)</p><p>Jan 15: Drawings Dr 5k; Cash Cr 5k (Insurance paid)</p><p>Jan 22: Cash Dr 24,500, Disc Allowed Dr 500; A/R Cr 25k (Discount given)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of Jan 1, 3, 10 and 25 on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Equation Balance (A = L + OE) = <strong>1,14,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b35",
        stem: "<p>Ledger balances of Salim Traders on Dec 31, 2017: Cash 1,00,000 Taka; Office Equip 1,50,000 Taka; A/R 50,000 Taka; A/P 40,000 Taka. Jan 2018 transactions:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 5: Loan taken from bank via 10% note payable 50,000 Taka.</li><li>Jan. 8: Purchase 1,20,000 Taka (30,000 cash, 90,000 credit).</li><li>Jan. 10: Paid three months' rent in advance 15,000 Taka.</li><li>Jan. 12: Paid misc expenses 1,200 Taka.</li><li>Jan. 16: Sold goods for 1,20,000 Taka with 3% trade discount (60% cash, 40% credit).</li><li>Jan. 25: Received 30,000 Taka from a customer.</li><li>Jan. 28: One month of prepaid rent has expired.</li></ul>",
        meta: "Dhaka · 2019",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Provide the opening journal entry.", 
                answer: "<div class='text-xs space-y-1'><p>Cash Dr 1,00,000, Office Equip Dr 1,50,000, A/R Dr 50,000</p><p>Accounts Payable Cr 40,000, Capital Cr 2,60,000</p></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of transactions on the accounting equation using a table.", 
                answer: "<div class='text-sm font-bold'>Total Assets = Total Liabilities + Equity = <strong>3,00,200 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Prepare an income statement for the month of Jan 2018.", 
                answer: "<table class='w-full text-xs border mt-2'><tr><td class='border p-1'>Sales (120k - 3%)</td><td class='border p-1'>1,16,400</td></tr><tr><td class='border p-1'>(-) Purchases</td><td class='border p-1'>(1,20,000)</td></tr><tr><td class='border p-1'>(-) Rent Exp (15k/3)</td><td class='border p-1'>(5,000)</td></tr><tr><td class='border p-1'>(-) Misc Expense</td><td class='border p-1'>(1,200)</td></tr><tr><td class='border p-1 font-bold'>Net Loss</td><td class='border p-1 font-bold'>(9,800) Taka</td></tr></table>" 
            }
        ]
    },
    {
        id: "b36",
        stem: "<p>The transactions of Asim Traders for March 2018 were:</p><ul class='list-disc ml-6 mt-2'><li>March 1: Started business with cash 50,000 Taka, bank balance 45,000 Taka, and a loan of 40,000 Taka.</li><li>March 5: Sold goods to Anita for 35,000 Taka.</li><li>March 7: Purchased goods from Monir on credit for 25,000 Taka.</li><li>March 9: Cash sales 29,000 Taka.</li><li>March 18: Received a crossed check for 10,000 Taka from Anita.</li><li>March 18: Received a crossed check for 10,000 Taka from Anita.</li><li>March 19: Distributed goods for free 4,000 Taka.</li><li>March 31: Bank allowed interest 1,000 Taka.</li></ul>",
        meta: "Rajshahi · 2019",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of net purchase for Asim Traders.", 
                answer: "<div class='text-sm font-medium'>Net Purchase = Credit Purchase (25,000) - Free Distribution (4,000) = <strong>21,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Identify the accounts involved in the above transactions with their classification.", 
                answer: "<div class='text-xs space-y-1'><p>March 1: Cash (A), Bank (A), Loan (L), Capital (OE)</p><p>March 5: A/R (A), Sales (OE)</p><p>March 7: Purchase (OE), A/P (L)</p><p>March 19: Advertising (OE), Purchase (OE)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions on the accounting equation using a statement table.", 
                answer: "<div class='text-sm font-bold'>Final Equation Balance (A = L + OE) = <strong>1,61,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b37",
        stem: "<p>Mr. Nazrul started a business with cash 5,00,000 Taka, goods 2,00,000 Taka, and a bank balance of 1,00,000 Taka. First month transactions:</p><ul class='list-disc ml-6 mt-2'><li>(1) Purchased goods by check 50,000 Taka.</li><li>(2) Sold goods on credit 70,000 Taka.</li><li>(3) Distributed goods for free to customers 5,000 Taka.</li><li>(4) Withdrew 10,000 Taka from bank for personal use.</li><li>(5) Bank allowed interest 1,200 Taka.</li></ul>",
        meta: "Comilla · 2019",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the initial capital for Mr. Nazrul.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (500k) + Inventory (200k) + Bank (100k) = <strong>8,00,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the classification of transactions 1 to 4 using the modern method.", 
                answer: "<div class='text-xs space-y-1'><p>1: Purchase (Equity), Bank (Asset)</p><p>2: A/R (Asset), Sales (Equity)</p><p>3: Advertising (Equity), Purchase (Equity)</p><p>4: Drawings (Equity), Bank (Asset)</p></div>" 
            },
            { 
                label: "c", 
                text: "Determine the amount of owner's equity at the end of the month.", 
                answer: "<div class='text-sm font-medium'>Equity = Opening (800k) + Sales (70k) - Purchase (50k) - Drawings (10k) + Bank Interest (1.2k) = <strong>8,11,200 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b38",
        stem: "<p>Mr. Hafiz started a business on Dec 1, 2018, with cash 30,000 Taka and office equipment worth 40,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Dec. 2: Cash purchase 20,000 Taka.</li><li>Dec. 6: Purchased office equipment for cash 10,000 Taka.</li><li>Dec. 9: Cash sales 45,000 Taka.</li><li>Dec. 15: Credit purchase 30,000 Taka.</li><li>Dec. 20: Credit sales 40,000 Taka.</li><li>Dec. 26: Paid to creditor 25,000 Taka.</li><li>Dec. 28: Collected from accounts receivable 20,000 Taka.</li><li>Dec. 30: Paid employees' salary 10,000 Taka.</li></ul>",
        meta: "Jessore · 2019",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (30,000) + Office Equip (40,000) = <strong>70,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine the amount of owner's equity at the end of the month.", 
                answer: "<div class='text-sm font-medium'>Equity = 70k (Initial) + 85k (Total Sales) - 50k (Total Purchases) - 10k (Salary) = <strong>95,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of the above transactions on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Final Total (A = L + OE) = <strong>1,00,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b39",
        stem: "<p>On Jan 1, 2018, Mr. Shamim started a business with cash 80,000 Taka, furniture worth 40,000 Taka, and a bank loan of 50,000 Taka. Jan transactions:</p><ul class='list-disc ml-6 mt-2'><li>Jan. 2: Purchased a delivery van for 70,000 Taka; paid 20,000 in cash and issued a note for the balance.</li><li>Jan. 5: Cash purchase with 15% VAT, total 57,500 Taka.</li><li>Jan. 10: Sold goods of 60,000 Taka to Mr. Rafiq at 10% discount; received 30,000 in cash.</li><li>Jan. 12: Sales return 5,000 Taka.</li><li>Jan. 15: Purchased office supplies for 7,000 Taka (2,000 in cash, balance on credit).</li><li>Jan. 20: Received commission 7,000 Taka.</li><li>Jan. 30: Received advertising bill from a daily newspaper for 5,000 Taka.</li></ul>",
        meta: "Barisal · 2019",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of Mr. Shamim's initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (80,000) + Furniture (40,000) = <strong>1,20,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Journalize the transactions of January 2, 5, 10 and 12 (without explanation).", 
                answer: "<div class='text-xs space-y-1'><p>Jan 2: Van Dr 70k; Cash Cr 20k, Notes Payable Cr 50k</p><p>Jan 5: Purchase Dr 50k, VAT Dr 7.5k; Cash Cr 57.5k</p><p>Jan 10: Cash Dr 30k, A/R Dr 24k; Sales Cr 54k</p><p>Jan 12: Sales Return Dr 5k; A/R Cr 5k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of Jan 1, 15, 20 and 30 on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Total Assets = Total Liabilities + Equity = <strong>1,82,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b40",
        stem: "<p>Mr. Azraf started a business on June 1, 2018, with cash 50,000 Taka, goods 15,000 Taka, and bank balance 20,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>June 5: Sold goods to Ershad for 20,000 Taka (60% cash).</li><li>June 10: Paid four months' rent in advance 12,000 Taka.</li><li>June 20: Purchased goods from Nasrin for 10,000 Taka (40% cash).</li><li>June 25: Purchased supplies on credit for 5,000 Taka.</li><li>June 27: Electricity bill received 3,000 Taka.</li><li>June 30: Paid salary by check 5,000 Taka.</li></ul>",
        meta: "Sylhet · 2019",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the total amount of accounts payable at the end of June.", 
                answer: "<div class='text-sm font-medium'>A/P = Nasrin (6,000) + Supplies Payable (5,000) + Elec. Bill (3,000) = <strong>14,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for the transactions of June 1, 5, 10 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>June 1: Cash/Inv/Bank Dr; Cap Cr</p><p>June 5: Cash/AR Dr; Sales Cr</p><p>June 10: Prepaid Rent Dr; Cash Cr</p><p>June 30: Salary Exp Dr; Bank Cr</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of June 5, 20, 25 and 27 on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Equation Total (A = L + OE) = <strong>1,10,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b41",
        stem: "<p>Mr. Altaf Mahmud started a business on May 1, 2018, with machinery 90,000 Taka, furniture 80,000 Taka, cash 70,000 Taka, and a bank loan of 35,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>May 2: Purchased goods: Cash 25,000 Taka and Credit 40,000 Taka.</li><li>May 4: Sold goods: Cash 55,000 Taka and Credit 90,000 Taka.</li><li>May 8: Purchased furniture on credit for 56,000 Taka.</li><li>May 12: Purchased supplies for 7,000 Taka.</li><li>May 15: Paid salaries to employees 40,000 Taka.</li><li>May 20: Paid for newspaper advertisement 15,000 Taka.</li><li>May 25: Withdrew 8,000 Taka from the business for personal use.</li><li>March 31: Paid 20,000 Taka to creditors.</li></ul>",
        meta: "Dinajpur · 2019",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the initial capital of Mr. Altaf Mahmud.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Machinery (90k) + Furniture (80k) + Cash (70k) = <strong>2,40,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the classification of accounts for the transactions of May 2, 4, 20 and 25 using the modern method.", 
                answer: "<div class='text-xs space-y-1'><p>May 2: Purchase (OE), Cash (A), A/P (L)</p><p>May 4: Cash (A), A/R (A), Sales (OE)</p><p>May 20: Advertising (OE), Cash (A)</p><p>May 25: Drawings (OE), Cash (A)</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 1, 8, 12 and 31 on the accounting equation using a table.", 
                answer: "<div class='text-sm font-bold'>Final Equation Total = <strong>3,48,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b42",
        stem: "<p class='mb-2'>The following trial balance was prepared from the books of Tonu Brothers as of December 31, 2017:</p><table class='w-full text-[10px] border-collapse border mb-4'><thead><tr class='bg-gray-100'><th class='border p-1 text-left'>Account Name</th><th class='border p-1 text-right'>Debit (Tk)</th><th class='border p-1 text-left'>Account Name</th><th class='border p-1 text-right'>Credit (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>Opening Inventory</td><td class='border p-1 text-right'>50,000</td><td class='border p-1'>Tonu's Capital</td><td class='border p-1 text-right'>65,000</td></tr><tr><td class='border p-1'>Furniture</td><td class='border p-1 text-right'>80,000</td><td class='border p-1'>Sales</td><td class='border p-1 text-right'>5,20,000</td></tr><tr><td class='border p-1'>Bank Balance</td><td class='border p-1 text-right'>24,000</td><td class='border p-1'>Accounts Payable</td><td class='border p-1 text-right'>29,000</td></tr><tr><td class='border p-1'>Cash in Hand</td><td class='border p-1 text-right'>36,000</td><td class='border p-1'>Discount Received</td><td class='border p-1 text-right'>1,000</td></tr><tr><td class='border p-1'>Purchase</td><td class='border p-1 text-right'>3,25,600</td><td class='border p-1'>6% Loan (01-01-17)</td><td class='border p-1 text-right'>80,000</td></tr><tr><td class='border p-1'>Accounts Receivable</td><td class='border p-1 text-right'>85,000</td><td class='border p-1'>Purchase Return</td><td class='border p-1 text-right'>20,000</td></tr><tr><td class='border p-1'>Carriage Inwards</td><td class='border p-1 text-right'>8,800</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Wages</td><td class='border p-1 text-right'>5,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Sales Return</td><td class='border p-1 text-right'>20,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Salary</td><td class='border p-1 text-right'>51,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Discount Allowed</td><td class='border p-1 text-right'>4,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Rent</td><td class='border p-1 text-right'>25,600</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr></tbody><tfoot><tr class='font-bold bg-gray-50'><td class='border p-1 text-left'>Total</td><td class='border p-1 text-right'>7,15,000</td><td class='border p-1 text-left'>Total</td><td class='border p-1 text-right'>7,15,000</td></tr></tfoot></table><p class='mt-2'>Adjustments: 1. Closing Inventory 45,000 Taka. 2. Prepaid Rent 5,600 Taka. 3. Accrued Salary 7,000 Taka and Accrued Wages 9,000 Taka. 4. Depreciation on Furniture 10%. 5. Bad debt provision 5%.</p>",
        meta: "Dhaka · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the total amount of direct expenses.", 
                answer: "<div class='text-sm font-medium'>Direct Expenses = Wages (5,000 + 9,000) + Carriage Inwards (8,800) = <strong>22,800 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine the total operating expenses.", 
                answer: "<div class='text-sm font-medium'>Operating Exp = Salary (58k) + Rent (20k) + Disc Allowed (4k) + Dep on Furn (8k) + Bad Debt Prov (4,250) = <strong>94,250 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Assuming net income is 34,950 Taka, prepare a statement of financial position.", 
                answer: "<div class='text-sm font-bold'>Total Assets = Total Liabilities + Equity = <strong>2,48,950 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b43",
        stem: "<p class='mb-2'>The following trial balance was prepared from the ledger balances of Toma Company on December 31, 2017:</p><table class='w-full text-[10px] border-collapse border mb-4'><thead><tr class='bg-gray-100'><th class='border p-1 text-left'>Account Name</th><th class='border p-1 text-right'>Debit (Tk)</th><th class='border p-1 text-left'>Account Name</th><th class='border p-1 text-right'>Credit (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>Cash in Hand</td><td class='border p-1 text-right'>37,000</td><td class='border p-1'>Sales</td><td class='border p-1 text-right'>5,20,000</td></tr><tr><td class='border p-1'>Rent (10 months)</td><td class='border p-1 text-right'>30,000</td><td class='border p-1'>Bank Overdraft</td><td class='border p-1 text-right'>85,000</td></tr><tr><td class='border p-1'>Salary (9 months)</td><td class='border p-1 text-right'>36,000</td><td class='border p-1'>10% Bank Loan</td><td class='border p-1 text-right'>1,80,000</td></tr><tr><td class='border p-1'>Opening Inventory</td><td class='border p-1 text-right'>55,000</td><td class='border p-1'>Accounts Payable</td><td class='border p-1 text-right'>85,000</td></tr><tr><td class='border p-1'>Purchase</td><td class='border p-1 text-right'>3,55,000</td><td class='border p-1'>Capital</td><td class='border p-1 text-right'>2,25,000</td></tr><tr><td class='border p-1'>Wages</td><td class='border p-1 text-right'>22,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Consignment Goods</td><td class='border p-1 text-right'>10,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Building</td><td class='border p-1 text-right'>2,90,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>12% Investment</td><td class='border p-1 text-right'>1,22,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Office Equipment</td><td class='border p-1 text-right'>31,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Accounts Receivable</td><td class='border p-1 text-right'>85,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Office Expenses</td><td class='border p-1 text-right'>22,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr></tbody><tfoot><tr class='font-bold bg-gray-50'><td class='border p-1 text-left'>Total</td><td class='border p-1 text-right'>10,95,000</td><td class='border p-1 text-left'>Total</td><td class='border p-1 text-right'>10,95,000</td></tr></tfoot></table><p class='mt-2'>Adjustments: 1. Closing Inventory 1,00,000 Taka. 2. Cash snatched 3,500 Taka. 3. Bad debt provision 5%. 4. Dep: Building 10%, Office Equipment 5%.</p>",
        meta: "Dhaka · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of non-operating income and expenses.", 
                answer: "<div class='text-xs space-y-1'><p>Income: Int. on Investment (14,640 Taka)</p><p>Expenses: Cash Snatched (3,500 Taka) + Int. on Bank Loan (18,000 Taka)</p></div>" 
            },
            { 
                label: "b", 
                text: "Determine the gross profit of Toma Company.", 
                answer: "<div class='text-sm font-medium'>Gross Profit = Sales (520k) - COGS (55k + 355k + 22k - 100k) = <strong>1,88,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Show the total assets of Toma Company at year-end.", 
                answer: "<div class='text-sm font-bold'>Total Assets (Fixed + Current) = <strong>5,45,790 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b44",
        stem: "<p>Mr. Sajedur Rahman started a business on Nov 1, 2017, with cash 40,000 Taka, goods 60,000 Taka, and a loan of 50,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Nov 2: Opened a current account in the bank with 20,000 Taka.</li><li>Nov 6: Purchased furniture for resale 35,000 Taka.</li><li>Nov 8: Sold goods to Riju for 30,000 Taka; charged 15% VAT.</li><li>Nov 10: Purchased goods from Samih for 45,000 Taka; charged 15% VAT.</li><li>Nov 13: Borrowed 10,000 Taka from Tonu.</li><li>Nov 15: Repaid Tonu's loan by check.</li><li>Nov 17: Sold furniture by check 5,000 Taka.</li><li>Nov 20: Bank charged 500 Taka.</li><li>Nov 24: Paid income tax 3,000 Taka.</li><li>Nov 26: Purchased savings certificate 20,000 Taka.</li><li>Nov 30: Withdrew 7,000 Taka for personal use.</li></ul>",
        meta: "Dhaka · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "What is the total amount of VAT?", 
                answer: "<div class='text-sm font-medium'>Total VAT = VAT on Sales (4,500) + VAT on Purchase (6,750) = <strong>11,250 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the classification of accounts for the transactions of dates 17, 24, 26 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>Nov 17: Bank (A), Furniture/Sales (A/E)</p><p>Nov 24: Drawings (Equity), Cash (A)</p><p>Nov 26: Investment (Asset), Cash (A)</p><p>Nov 30: Drawings (Equity), Cash (A)</p></div>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the transactions of dates 10, 13, 15 and 20.", 
                answer: "<div class='text-xs space-y-1'><p>Nov 10: Purchase Dr 45k, VAT Dr 6.75k; A/P Cr 51.75k</p><p>Nov 13: Cash Dr 10k; Loan from Tonu Cr 10k</p><p>Nov 15: Loan from Tonu Dr 10k; Bank Cr 10k</p><p>Nov 20: Bank Charges Dr 500; Bank Cr 500</p></div>" 
            }
        ]
    },
    {
        id: "b45",
        stem: "<p>The transactions of Sabina & Sons for April 2017 were:</p><ul class='list-disc ml-6 mt-2'><li>April 1: Opening cash 20,000 Taka and bank balance 80,000 Taka.</li><li>April 5: Cash purchase 4,000 Taka; Cash sales 12,000 Taka.</li><li>April 7: Purchased furniture for 20,000 Taka (10,000 in cash, 10,000 by check).</li><li>April 8: Credit sales 5,000 Taka.</li><li>April 10: Paid salary 8,800 Taka in cash and insurance 2,400 Taka by check.</li><li>April 13: Received 16,000 Taka in cash from Mokles Traders.</li><li>April 15: Withdrew 12,000 Taka from bank for personal use.</li><li>April 18: Sold old furniture for 6,000 Taka.</li><li>April 24: Paid life insurance premium 9,000 Taka.</li><li>April 28: Withdrew 3,200 Taka from bank for office use.</li></ul>",
        meta: "Dhaka · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "What is the total amount of bank withdrawals?", 
                answer: "<div class='text-sm font-medium'>Total Bank Withdrawal = Furniture (10k) + Insurance (2.4k) + Personal (12k) + Office (3.2k) = <strong>27,600 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare a double column cash book for the month.", 
                answer: "<div class='text-sm font-bold'>Cash Balance: 20,200 Taka | Bank Balance: 52,400 Taka</div>" 
            },
            { 
                label: "c", 
                text: "Prepare the Sales account and Drawings account.", 
                answer: "<div class='text-xs space-y-1'><p>Sales Account (Cr): 17,000 Taka</p><p>Drawings Account (Dr): 21,000 Taka</p></div>" 
            }
        ]
    },
    {
        id: "b46",
        stem: "<p>Lipi & Co. purchased the following goods on credit in June 2017:</p><ul class='list-disc ml-6 mt-2'><li>June 2: From Nipa Biponi: 200 pairs of Tant Sarees @ 500 Taka/pair. Trade discount 10%. Transport 1,000 Taka, Insurance 300 Taka. (Terms 3/10, n/20).</li><li>June 28: From Bodhua Cloth Stores: 50 Jamdani Sarees @ 5,000 Taka; 15 Banarasi Sarees @ 7,000 Taka; 200 Handkerchiefs @ 50 Taka. Trade discount 15%. Packing 1,000 Taka, Carriage 2,000 Taka. (Terms 3/15, n/30).</li></ul>",
        meta: "Dhaka · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the total amount of trade discount.", 
                answer: "<div class='text-sm font-medium'>Total Discount = June 2 (10,000) + June 28 (54,750) = <strong>64,750 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare the Purchase Journal.", 
                answer: "<div class='text-sm font-bold'>Purchase Journal Total = <strong>4,04,550 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Prepare the necessary ledger accounts.", 
                answer: "<div class='text-xs space-y-1'><p>Purchase Account (Dr): 3,91,250 Taka</p><p>Nipa Biponi (Cr): 91,300 Taka</p><p>Bodhua Cloth (Cr): 3,13,250 Taka</p></div>" 
            }
        ]
    },
    {
        id: "b47",
        stem: "<p>Bank information for Samih Rahman as of March 31, 2017:</p><ul class='list-disc ml-6 mt-2'><li>1. Bank balance as per pass book 44,400 Taka.</li><li>2. A 3,000 Taka bill discounted for 2,400 Taka was dishonored (no entry in cash book).</li><li>3. Personal withdrawal of 3,000 Taka not recorded in cash book.</li><li>4. Unpresented checks 11,400 Taka.</li><li>5. Bank collected 6,000 Taka for a 6,600 Taka bill (full 6,600 recorded in cash book).</li><li>6. Bank interest 1,000 Taka and Bank charges 1,000 Taka.</li><li>7. Bank paid a creditor 6,000 Taka (not in cash book).</li><li>8. Dividend collected 6,600 Taka (not in cash book).</li></ul>",
        meta: "Dhaka · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "How much was the total expense for bill collection and discounting?", 
                answer: "<div class='text-sm font-medium'>Total Expense = Discounting Loss (600) + Collection Loss (600) = <strong>1,200 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare a Bank Reconciliation Statement.", 
                answer: "<div class='text-sm font-bold'>Bank Balance as per Cash Book = <strong>35,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Prepare BRS starting with a Cash Book balance of 35,000 Taka.", 
                answer: "<div class='text-sm font-bold'>Bank Balance as per Pass Book = <strong>44,400 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b48",
        stem: "<p class='mb-2'>Information for Ruma Enterprise:</p><table class='w-full text-xs border mb-4'><thead><tr class='bg-gray-100'><th class='border p-1'>Particulars</th><th class='border p-1 text-right'>Dec 31, 2016</th><th class='border p-1 text-right'>Dec 31, 2017</th></tr></thead><tbody><tr><td class='border p-1'>Bad Debt Provision (01-01)</td><td class='border p-1 text-right'>12,000</td><td class='border p-1 text-right'>-</td></tr><tr><td class='border p-1'>Bad Debt (Written off)</td><td class='border p-1 text-right'>10,500</td><td class='border p-1 text-right'>5,400</td></tr><tr><td class='border p-1'>Provision Rate</td><td class='border p-1 text-right'>2.5%</td><td class='border p-1 text-right'>5%</td></tr><tr><td class='border p-1'>Accounts Receivable</td><td class='border p-1 text-right'>2,26,500</td><td class='border p-1 text-right'>1,55,400</td></tr></tbody></table>",
        meta: "Dhaka · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of bad debt for 2017.", 
                answer: "<div class='text-sm font-medium'>Bad Debt (2017) = <strong>5,400 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare the Bad Debt Provision Account for 2017.", 
                answer: "<div class='text-xs space-y-1'><p>Opening Balance: 5,400 Taka</p><p>New Provision (5% of 150k): 7,500 Taka</p><p>Bad Debt Exp: 7,500 Taka</p></div>" 
            },
            { 
                label: "c", 
                text: "Prepare the Bad Debt Account.", 
                answer: "<div class='text-sm font-bold'>Total Bad Debt Expense = <strong>7,500 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b49",
        stem: "<p class='mb-2'>Ledger balances for Rahman Brothers as of Dec 31, 2017:</p><table class='w-full text-xs border mb-4'><tbody><tr><td class='border p-1'>Service Revenue</td><td class='border p-1 text-right'>3,48,000</td><td class='border p-1'>Law Books</td><td class='border p-1 text-right'>20,000</td></tr><tr><td class='border p-1'>Supplies Purchase</td><td class='border p-1 text-right'>20,000</td><td class='border p-1'>Drawings</td><td class='border p-1 text-right'>1,00,000</td></tr><tr><td class='border p-1'>Bank Overdraft</td><td class='border p-1 text-right'>75,000</td><td class='border p-1'>Closing Supplies</td><td class='border p-1 text-right'>16,000</td></tr><tr><td class='border p-1'>Office Equipment</td><td class='border p-1 text-right'>1,00,000</td><td class='border p-1'>Capital</td><td class='border p-1 text-right'>2,00,000</td></tr><tr><td class='border p-1'>Accounts Receivable</td><td class='border p-1 text-right'>50,000</td><td class='border p-1'>Furniture</td><td class='border p-1 text-right'>60,000</td></tr><tr><td class='border p-1'>Fire Loss</td><td class='border p-1 text-right'>16,000</td><td class='border p-1'>A/P</td><td class='border p-1 text-right'>80,000</td></tr><tr><td class='border p-1'>Opening Supplies</td><td class='border p-1 text-right'>8,000</td><td class='border p-1'>Salary</td><td class='border p-1 text-right'>60,000</td></tr></tbody></table>",
        meta: "Dhaka · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "What is the amount of supplies expense?", 
                answer: "<div class='text-sm font-medium'>Expense = Opening (8k) + Purchase (20k) - Closing (16k) = <strong>12,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine fixed assets and current liabilities.", 
                answer: "<div class='text-xs space-y-1'><p>Fixed Assets: 100k+60k+20k = 1,80,000 Taka</p><p>Current Liab: 75k+80k = 1,55,000 Taka</p></div>" 
            },
            { 
                label: "c", 
                text: "Prepare a Trial Balance.", 
                answer: "<div class='text-sm font-bold'>Trial Balance Total = <strong>7,03,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b50",
        stem: "<p>Priyanti Rahman Mfg Co. purchased machinery for 6,35,000 Taka on Jan 1, 2017 and paid 20,000 Taka for transport. Useful life is 8 years, salvage value 35,000 Taka. The company uses the Reducing Balance Method.</p>",
        meta: "Dhaka · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the depreciation rate and 1st year depreciation.", 
                answer: "<div class='text-xs space-y-1'><p>Rate = (100%/8) * 2 = 25%</p><p>1st Year Dep = 6,55,000 * 25% = 1,63,750 Taka</p></div>" 
            },
            { 
                label: "b", 
                text: "Prepare the Depreciation Expense Account.", 
                answer: "<div class='text-sm font-bold'>Year 1 Balance: 1,63,750 Taka</div>" 
            },
            { 
                label: "c", 
                text: "Prepare the Machinery Account for the first year.", 
                answer: "<div class='text-sm font-bold'>Balance c/d: 6,55,000 Taka (Depreciation is recorded in Acc. Dep)</div>" 
            }
        ]
    },
    {
        id: "b51",
        stem: "<p class='mb-2'>Trial Balance for Tisha Servicing Institution as of Dec 31, 2017:</p><table class='w-full text-[10px] border-collapse border mb-4'><thead><tr class='bg-gray-100'><th class='border p-1 text-left'>Account Name</th><th class='border p-1 text-right'>Debit (Tk)</th><th class='border p-1 text-right'>Credit (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>Cash</td><td class='border p-1 text-right'>20,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Accounts Receivable</td><td class='border p-1 text-right'>22,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Prepaid Insurance</td><td class='border p-1 text-right'>15,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Building</td><td class='border p-1 text-right'>2,00,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Rent</td><td class='border p-1 text-right'>5,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Service Revenue</td><td class='border p-1 text-right'></td><td class='border p-1 text-right'>1,07,000</td></tr><tr><td class='border p-1'>Salary</td><td class='border p-1 text-right'>15,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Capital</td><td class='border p-1 text-right'></td><td class='border p-1 text-right'>2,50,000</td></tr><tr><td class='border p-1'>Furniture</td><td class='border p-1 text-right'>1,00,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Accounts Payable</td><td class='border p-1 text-right'></td><td class='border p-1 text-right'>20,000</td></tr></tbody><tfoot><tr class='font-bold bg-gray-50'><td class='border p-1'>Total</td><td class='border p-1 text-right'>3,77,000</td><td class='border p-1 text-right'>3,77,000</td></tr></tfoot></table><p class='mt-2'>Adjustments: 1. Dep on Building 2.5%. 2. Accrued Salary 3,500 Taka. 3. Prepaid Insurance expired 10,000 Taka. 4. Dep on Furniture 5%.</p>",
        meta: "Dhaka · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the depreciation on furniture and net furniture value.", 
                answer: "<div class='text-sm font-medium'>Dep = 1,00,000 * 5% = 5,000 Taka. Net Value = <strong>95,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide adjusting journal entries.", 
                answer: "<div class='text-xs space-y-1'><p>Salary Dr 3,500; Accrued Salary Cr 3,500</p><p>Insurance Exp Dr 10,000; Prepaid Ins Cr 10,000</p><p>Dep Exp Dr 10,000; Acc. Dep Cr 10,000</p></div>" 
            },
            { 
                label: "c", 
                text: "Prepare a 10-column worksheet.", 
                answer: "<div class='text-sm font-bold'>Net Income = <strong>70,000 Taka</strong> | Total Assets = <strong>3,23,500 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b52",
        stem: "<p class='mb-2'>Abdus Sobur maintains accounts using the single entry system. His status in 2017 was:</p><table class='w-full text-xs border mb-4'><thead><tr class='bg-gray-100'><th class='border p-1'>Account Name</th><th class='border p-1 text-right'>Jan 1, 2017</th><th class='border p-1 text-right'>Dec 31, 2017</th></tr></thead><tbody><tr><td class='border p-1'>Accounts Receivable</td><td class='border p-1 text-right'>12,000</td><td class='border p-1 text-right'>20,000</td></tr><tr><td class='border p-1'>Plant & Machinery</td><td class='border p-1 text-right'>80,000</td><td class='border p-1 text-right'>80,000</td></tr><tr><td class='border p-1'>12% Investment</td><td class='border p-1 text-right'>20,000</td><td class='border p-1 text-right'>20,000</td></tr><tr><td class='border p-1'>Accounts Payable</td><td class='border p-1 text-right'>8,000</td><td class='border p-1 text-right'>15,500</td></tr><tr><td class='border p-1'>Inventory</td><td class='border p-1 text-right'>7,000</td><td class='border p-1 text-right'>12,000</td></tr><tr><td class='border p-1'>Furniture</td><td class='border p-1 text-right'>-</td><td class='border p-1 text-right'>10,000</td></tr><tr><td class='border p-1'>Bank Loan (15%)</td><td class='border p-1 text-right'>20,000</td><td class='border p-1 text-right'>-</td></tr><tr><td class='border p-1'>Cash Balance</td><td class='border p-1 text-right'>4,000</td><td class='border p-1 text-right'>10,000</td></tr></tbody></table><p class='mt-2'>Adjustments: Monthly drawings (2k cash + 13k goods). Provision on A/P 2%. Dep on Furn 10%. Bad debt prov 5%. Int on Capital 2.5%.</p>",
        meta: "Dhaka · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine interest on investment and bank loan.", 
                answer: "<div class='text-sm font-medium'>Int on Inv (Sep-Dec) = 800 Taka. Int on Loan (Jan-May) = <strong>1,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine opening and closing capital.", 
                answer: "<div class='text-xs space-y-1'><p>Opening Capital = 1,28,000 - 28,000 = 1,00,000 Taka</p><p>Closing Capital = 1,56,000 - 15,500 = 1,40,500 Taka</p></div>" 
            },
            { 
                label: "c", 
                text: "Assuming net income is 53,310 Taka, prepare the Statement of Affairs.", 
                answer: "<div class='text-sm font-bold'>Statement Total = <strong>1,55,100 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b53",
        stem: "<p class='mb-2'>Trial Balance for Quality Traders as of Dec 31, 2017:</p><table class='w-full text-[10px] border-collapse border mb-4'><tbody><tr><td class='border p-1'>Office Equipment</td><td class='border p-1 text-right'>1,40,000</td><td class='border p-1'>Capital</td><td class='border p-1 text-right'>2,00,000</td></tr><tr><td class='border p-1'>Supplies</td><td class='border p-1 text-right'>7,000</td><td class='border p-1'>Unearned Service Rev</td><td class='border p-1 text-right'>15,000</td></tr><tr><td class='border p-1'>Rent</td><td class='border p-1 text-right'>36,000</td><td class='border p-1'>Service Revenue</td><td class='border p-1 text-right'>80,000</td></tr><tr><td class='border p-1'>Cash</td><td class='border p-1 text-right'>45,000</td><td class='border p-1'>Acc. Dep - Office Eq.</td><td class='border p-1 text-right'>25,000</td></tr><tr><td class='border p-1'>Accounts Receivable</td><td class='border p-1 text-right'>80,000</td><td class='border p-1'>Commission Revenue</td><td class='border p-1 text-right'>20,000</td></tr></tbody><tfoot><tr class='font-bold bg-gray-50'><td class='border p-1'>Total</td><td class='border p-1 text-right'>3,40,000</td><td class='border p-1 text-right'>3,40,000</td></tr></tfoot></table><p class='mt-2'>Adjustments: 1. Accrued Service Rev 15k. 2. Rent for 3 years. 3. Earned 3k from Unearned Rev. 4. Unused supplies 2k.</p>",
        meta: "Rajshahi · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Calculate total service revenue.", 
                answer: "<div class='text-sm font-medium'>Total Service Rev = 80k + 15k + 3k = <strong>98,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare the Comprehensive Income Statement.", 
                answer: "<div class='text-sm font-bold'>Net Income = <strong>73,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Prepare the Statement of Financial Position.", 
                answer: "<div class='text-sm font-bold'>Total Assets = <strong>2,73,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b54",
        stem: "<p class='mb-2'>Trial Balance for Chowdhury Trading as of Dec 31, 2017:</p><table class='w-full text-[10px] border-collapse border mb-4'><tbody><tr><td class='border p-1'>Purchase & Sales</td><td class='border p-1 text-right'>1,42,000</td><td class='border p-1 text-right'>2,10,000</td></tr><tr><td class='border p-1'>Return</td><td class='border p-1 text-right'>5,000</td><td class='border p-1 text-right'>-</td></tr><tr><td class='border p-1'>Accounts Receivable/Payable</td><td class='border p-1 text-right'>60,000</td><td class='border p-1 text-right'>42,000</td></tr><tr><td class='border p-1'>Wages</td><td class='border p-1 text-right'>8,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Salary (10 months)</td><td class='border p-1 text-right'>20,000</td><td class='border p-1 text-right'></td></tr></tbody></table><p class='mt-2'>Adjustments: 1. Closing Inv 50,000 (includes 3.5k sold goods). 2. Owner took 3k goods (not recorded). 3. Returned 2k goods to supplier (not recorded).</p>",
        meta: "Rajshahi · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine net purchases and net sales.", 
                answer: "<div class='text-xs space-y-1'><p>Net Purchase = 142k - 3k - 2k = 1,37,000 Taka</p><p>Net Sales = 210k - 5k = <strong>2,05,000 Taka</strong></p></div>" 
            },
            { 
                label: "b", 
                text: "Prepare the Income Statement.", 
                answer: "<div class='text-sm font-bold'>Gross Profit = 66,500 Taka | Net Profit = <strong>37,500 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Determine owner's equity and total liabilities.", 
                answer: "<div class='text-xs space-y-1'><p>Owner's Equity = 2,24,500 Taka</p><p>Total Liabilities = 44,000 Taka</p></div>" 
            }
        ]
    },
    {
        id: "b55",
        stem: "<p>Mr. Rahim Mia started a business on Jan 1, 2017 with cash 1,00,000 Taka and furniture 50,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan 3: Appointed an employee at 12,000 Taka/month.</li><li>Jan 8: Cash purchase 30,000 Taka.</li><li>Jan 15: Credit purchase 10,000 Taka.</li><li>Jan 20: Credit sales to Alam 40,000 Taka.</li><li>Jan 25: Paid personal life insurance premium 500 Taka from personal fund.</li><li>Jan 30: Paid salary 12,000 Taka.</li></ul>",
        meta: "Rajshahi · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Identify events that are not transactions and calculate their total.", 
                answer: "<div class='text-sm font-medium'>Non-transactions = Jan 3 (Appointing) + Jan 25 (Personal Pay) = <strong>12,500 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide ledger entries for Cash and Capital accounts using running balance.", 
                answer: "<div class='text-sm font-bold'>Cash Bal: 58,000 Taka | Capital Bal: 1,50,000 Taka</div>" 
            },
            { 
                label: "c", 
                text: "Show the effects of transactions on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Equation Total (A = L + OE) = <strong>1,88,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b56",
        stem: "<p>Mr. Mushfiq started a business on Jan 1, 2017 with cash 50,000 Taka, goods 20,000 Taka, and a loan of 30,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan 5: Cash sales to Tamim 40,000 Taka.</li><li>Jan 8: Purchased furniture for cash 10,000 Taka.</li><li>Jan 12: Cash purchase inclusive of VAT 34,500 Taka.</li><li>Jan 15: Purchase return (External) 7,000 Taka.</li><li>Jan 20: Commission received 5,000 Taka.</li><li>Jan 23: Purchased goods from Rubel 15,000 Taka.</li><li>Jan 27: Rent paid 12,000 Taka.</li><li>Jan 30: Paid 11,500 Taka to Rubel in full settlement.</li></ul>",
        meta: "Rajshahi · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the initial capital of Mr. Mushfiq.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (50k) + Goods (20k) = <strong>70,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for the transactions of dates 12, 15, 20 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 12: Purchase Dr 30k, VAT Dr 4.5k; Cash Cr 34.5k</p><p>Jan 15: A/P Dr 7k; Purchase Return Cr 7k</p><p>Jan 20: Cash Dr 5k; Commission Cr 5k</p><p>Jan 30: A/P Dr 15k; Cash Cr 11.5k, Disc Cr 3.5k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 5, 8, 23 and 27 on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Final Equation Total = <strong>1,13,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b57",
        stem: "<p class='mb-2'>Ledger balances for Milon Traders as of Dec 31, 2017:</p><table class='w-full text-[10px] border-collapse border mb-4'><tbody><tr><td class='border p-1'>Capital</td><td class='border p-1 text-right'>1,00,000</td><td class='border p-1'>Purchase</td><td class='border p-1 text-right'>60,000</td></tr><tr><td class='border p-1'>Drawings</td><td class='border p-1 text-right'>5,000</td><td class='border p-1'>Salary</td><td class='border p-1 text-right'>2,00,000</td></tr><tr><td class='border p-1'>Opening Inventory</td><td class='border p-1 text-right'>25,000</td><td class='border p-1'>Rent</td><td class='border p-1 text-right'>3,000</td></tr><tr><td class='border p-1'>Closing Inventory</td><td class='border p-1 text-right'>20,000</td><td class='border p-1'>Sales</td><td class='border p-1 text-right'>90,000</td></tr><tr><td class='border p-1'>Accounts Receivable</td><td class='border p-1 text-right'>8,000</td><td class='border p-1'>Bank Overdraft</td><td class='border p-1 text-right'>3,000</td></tr></tbody></table>",
        meta: "Rajshahi · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Calculate the amount of adjusted purchases.", 
                answer: "<div class='text-sm font-medium'>Adjusted Purchase = Opening (25k) + Purchase (60k) - Closing (20k) = <strong>65,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine revenue expenditure and current liabilities.", 
                answer: "<div class='text-xs space-y-1'><p>Revenue Exp (COGS + Admin): 65k + 2k + 3k = 70,000 Taka</p><p>Current Liab (Bank OD + A/P): 3k + 5k = 8,000 Taka</p></div>" 
            },
            { 
                label: "c", 
                text: "Prepare a Trial Balance including adjusted purchases.", 
                answer: "<div class='text-sm font-bold'>Trial Balance Total = <strong>1,98,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b58",
        stem: "<p>Transactions of Paragon Traders for March 2017:</p><ul class='list-disc ml-6 mt-2'><li>March 1: Cash 30,000 Taka and Bank Overdraft 20,000 Taka.</li><li>March 5: Deposited 30,000 Taka into the bank.</li><li>March 8: Paid Emdad 9,500 Taka by check after 5% discount.</li><li>March 10: Cash withdrawal 2,000 Taka; Goods withdrawal 500 Taka.</li><li>March 15: Depreciation on furniture 1,500 Taka.</li><li>March 20: Purchased computer for cash 40,000 Taka.</li><li>March 25: Cash purchase 10,000 Taka.</li><li>March 30: Paid school fee for owner's son 200 Taka from business.</li></ul>",
        meta: "Rajshahi · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Provide journals for transactions not included in the cash book.", 
                answer: "<div class='text-xs space-y-1'><p>Drawings Dr 500; Purchase Cr 500</p><p>Dep Exp Dr 1,500; Acc. Dep Cr 1,500</p></div>" 
            },
            { 
                label: "b", 
                text: "Prepare a three-column cash book for March 1-15.", 
                answer: "<div class='text-sm font-bold'>Cash Bal: 18,000 Taka | Bank Bal: 500 Taka</div>" 
            },
            { 
                label: "c", 
                text: "Prepare a Cash Payment Journal for March 20-30.", 
                answer: "<div class='text-sm font-bold'>Total Payments = <strong>50,200 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b59",
        stem: "<p>Bad debt info for Salda Traders: Opening provision (Jan 1) 8,000 Taka; Written off bad debt 5,000 Taka; Accounts Receivable (Dec 31) 75,000 Taka; Unrecorded bad debt 4,000 Taka. Maintain a 10% provision.</p>",
        meta: "Rajshahi · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Calculate the new bad debt provision.", 
                answer: "<div class='text-sm font-medium'>New Prov = (75,000 - 4,000) * 10% = <strong>7,100 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide the necessary journal entries.", 
                answer: "<div class='text-xs space-y-1'><p>Bad Debt Dr 4,000; A/R Cr 4,000</p><p>Provision Dr 8,100; Income Summary Cr 8,100</p></div>" 
            },
            { 
                label: "c", 
                text: "Prepare the Bad Debt and Bad Debt Provision accounts.", 
                answer: "<div class='text-sm font-bold'>Total Bad Debt Expense = <strong>8,100 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b60",
        stem: "<p>Shanto Enterprise purchased a machine for 5,00,000 Taka on Jan 1, 2017. Transport cost 10,000 Taka and installation 30,000 Taka. Life 10 years, salvage 50,000 Taka. Straight Line Method is used.</p>",
        meta: "Rajshahi · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the depreciation for 2017.", 
                answer: "<div class='text-sm font-medium'>Dep = (5,40,000 - 50,000) / 10 = <strong>49,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for 2017.", 
                answer: "<div class='text-xs space-y-1'><p>Machinery Dr 5.4L; Cash Cr 5.4L</p><p>Dep Exp Dr 49k; Acc. Dep Cr 49k</p></div>" 
            },
            { 
                label: "c", 
                text: "Prepare the Machine and Accumulated Depreciation accounts for 2 years.", 
                answer: "<div class='text-sm font-bold'>Machine Bal: 5,40,000 Taka | Acc. Dep Bal: 98,000 Taka</div>" 
            }
        ]
    },
    {
        id: "b61",
        stem: "<p>The following information was taken from Mr. Tasnim's books on Dec 31, 2017:</p><ul class='list-disc ml-6 mt-2'><li>1. Bank balance as per Cash Book 50,000 Taka.</li><li>2. An issued check of 15,000 Taka has not yet been presented to the bank.</li><li>3. A check for 20,000 Taka was deposited but not yet collected by the bank.</li><li>4. Dividend collected by bank 5,000 Taka (not in cash book).</li><li>5. Bank paid 10,000 Taka to a creditor (not in cash book).</li><li>6. Bank collected 2,500 Taka from a debtor directly (not in cash book).</li><li>7. Bank charges 500 Taka (not in cash book).</li></ul>",
        meta: "Rajshahi · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "What is the total amount of transactions not yet recorded in the bank statement?", 
                answer: "<div class='text-sm font-medium'>Total = Unpresented Check (15k) + Outstanding Deposit (20k) = <strong>35,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for the transactions recorded by the bank.", 
                answer: "<div class='text-xs space-y-1'><p>Bank Dr 7.5k; Dividend Cr 5k, A/R Cr 2.5k</p><p>A/P Dr 10k; Bank Cr 10k</p><p>Bank Charges Dr 500; Bank Cr 500</p></div>" 
            },
            { 
                label: "c", 
                text: "Prepare a Bank Reconciliation Statement.", 
                answer: "<div class='text-sm font-bold'>Bank Balance as per Pass Book = <strong>42,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b62",
        stem: "<p class='mb-2'>Trial Balance for Shimu Traders as of Dec 31, 2017:</p><table class='w-full text-[10px] border-collapse border mb-4'><tbody><tr><td class='border p-1'>Capital</td><td class='border p-1 text-right'>1,50,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Service Revenue</td><td class='border p-1 text-right'></td><td class='border p-1 text-right'>3,00,000</td></tr><tr><td class='border p-1'>Furniture</td><td class='border p-1 text-right'>1,40,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Cash</td><td class='border p-1 text-right'>2,50,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Prepaid Insurance</td><td class='border p-1 text-right'>36,000</td><td class='border p-1 text-right'></td></tr><tr><td class='border p-1'>Rent</td><td class='border p-1 text-right'>80,000</td><td class='border p-1 text-right'></td></tr></tbody></table><p class='mt-2'>Adjustments: 1. Unearned revenue 10k included in service revenue. 2. Two months' rent accrued. 3. Insurance prepaid for 1 year till March 31, 2018. 4. Dep on Furniture 10%.</p>",
        meta: "Rajshahi · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Calculate the insurance and rent expense for 2017.", 
                answer: "<div class='text-sm font-medium'>Ins. Exp = 27,000 Taka. Rent Exp = 80k + 16k = <strong>96,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide adjusting journal entries.", 
                answer: "<div class='text-xs space-y-1'><p>Rent Dr 16k; Accrued Rent Cr 16k</p><p>Service Rev Dr 10k; Unearned Rev Cr 10k</p><p>Dep Exp Dr 14k; Acc. Dep Cr 14k</p></div>" 
            },
            { 
                label: "c", 
                text: "Prepare a 10-column worksheet.", 
                answer: "<div class='text-sm font-bold'>Net Income = <strong>1,43,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b63",
        stem: "<p class='mb-2'>Mr. Ibrahim Mia's business status on Dec 31, 2017:</p><table class='w-full text-xs border mb-4'><tbody><tr><td class='border p-1'>Inventory</td><td class='border p-1 text-right'>20,000</td><td class='border p-1'>Accounts Payable</td><td class='border p-1 text-right'>20,000</td></tr><tr><td class='border p-1'>Cash Balance</td><td class='border p-1 text-right'>80,000</td><td class='border p-1'>5% Bank Loan</td><td class='border p-1 text-right'>30,000</td></tr><tr><td class='border p-1'>Accounts Receivable</td><td class='border p-1 text-right'>20,000</td><td class='border p-1'>10% Investment</td><td class='border p-1 text-right'>50,000</td></tr><tr><td class='border p-1'>Furniture</td><td class='border p-1 text-right'>60,000</td><td class='border p-1'></td><td class='border p-1 text-right'></td></tr></tbody></table><p class='mt-2'>Additional Info: Purchased computer for 50k from personal funds. Bad debt 2,000. Monthly cash drawing 250, goods drawing 1,500.</p>",
        meta: "Rajshahi · 2018",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the closing capital.", 
                answer: "<div class='text-sm font-medium'>Closing Capital = 2,30,000 - 50,000 = <strong>1,80,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Prepare a Statement of Profit or Loss.", 
                answer: "<div class='text-sm font-bold'>Net Profit = <strong>32,500 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Prepare the Statement of Affairs.", 
                answer: "<div class='text-sm font-bold'>Statement Total = <strong>2,30,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b64",
        stem: "<p>Mr. Karim started a business on Jan 1, 2016 with cash 1,00,000 Taka and a bank loan of 80,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan 2: Cash purchase 10,000 Taka at 2% discount.</li><li>Jan 4: Paid life insurance premium 5,000 Taka.</li><li>Jan 10: Paid office staff salary 10,000 Taka.</li><li>Jan 12: Purchased computer for office 40,000 Taka.</li><li>Jan 20: Personal withdrawal of goods 5,000 Taka.</li><li>Jan 25: Purchased delivery van for 1,00,000 Taka.</li></ul>",
        meta: "Dhaka · 2017",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the total amount of drawings.", 
                answer: "<div class='text-sm font-medium'>Total Drawings = Life Ins (5k) + Goods (5k) = <strong>10,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for the transactions of dates 2, 4, 12 and 25.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 2: Purchase Dr 9.8k; Cash Cr 9.8k</p><p>Jan 4: Drawings Dr 5k; Cash Cr 5k</p><p>Jan 12: Computer (Asset) Dr 40k; Cash Cr 40k</p><p>Jan 25: Delivery Van Dr 1L; Cash Cr 1L</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions on the accounting equation in tabular form.", 
                answer: "<div class='text-sm font-bold'>Equation Total (A = L + OE) = <strong>1,69,700 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b65",
        stem: "<p>Mr. Sobuj started a business on Jan 1, 2016 with cash 2,00,000 Taka and furniture 50,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Jan 4: Cash sales 40,000 Taka.</li><li>Jan 7: Credit purchase 20,000 Taka.</li><li>Jan 10: Deposited 10,000 Taka into the bank.</li><li>Jan 15: Purchased machine for 25,000 Taka.</li><li>Jan 18: Paid rent 5,000 Taka.</li><li>Jan 27: Personal bank withdrawal 7,000 Taka.</li><li>Jan 30: Received 10,000 Taka from a debtor.</li></ul>",
        meta: "Rajshahi · 2017",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (2L) + Furniture (50k) = <strong>2,50,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for the transactions of dates 4, 10, 18 and 27.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 4: Cash Dr 40k; Sales Cr 40k</p><p>Jan 10: Bank Dr 10k; Cash Cr 10k</p><p>Jan 18: Rent Dr 5k; Cash Cr 5k</p><p>Jan 27: Drawings Dr 7k; Bank Cr 7k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect of transactions of dates 7, 15, 22 and 30 on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Equation Total (A = L + OE) = <strong>3,02,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b66",
        stem: "<p>Mr. Sojib started a business on March 1, 2016 with cash 50,000 Taka and furniture 30,000 Taka. Transactions were:</p><ul class='list-disc ml-6 mt-2'><li>Mar 2: Purchased furniture for cash 8,000 Taka.</li><li>Mar 5: Credit purchase of supplies 7,000 Taka.</li><li>Mar 10: Service provided 16,000 Taka (6k cash, 10k on account).</li><li>Mar 15: Advertising expense paid 5,500 Taka.</li><li>Mar 20: Paid for the supplies purchased on the 5th.</li><li>Mar 25: Interest on investment received 4,000 Taka.</li><li>Mar 30: Supplies used 4,500 Taka.</li></ul>",
        meta: "Dinajpur · 2017",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (50k) + Furniture (30k) = <strong>80,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of transactions of dates 1, 2, 5 and 10 on the accounting equation in tabular form.", 
                answer: "<div class='text-sm font-bold'>Tabular Total = <strong>1,03,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Provide journal entries for the transactions of dates 15, 20, 25 and 30.", 
                answer: "<div class='text-xs space-y-1'><p>Mar 15: Advertising Dr 5.5k; Cash Cr 5.5k</p><p>Mar 20: A/P Dr 7k; Cash Cr 7k</p><p>Mar 25: Cash Dr 4k; Interest Rev Cr 4k</p><p>Mar 30: Supplies Exp Dr 4.5k; Supplies Cr 4.5k</p></div>" 
            }
        ]
    },
    {
        id: "b67",
        stem: "<p>Rashed Traders' balances on June 30, 2016: Cash 25k, A/R 40k, Machinery 40k, Furniture 25k, A/P 20k. Transactions for July:</p><ul class='list-disc ml-6 mt-2'><li>July 5: Purchase 20,000 cash, 50,000 credit.</li><li>July 6: 1-year prepaid insurance 24,000 Taka.</li><li>July 10: Sales 50,000 cash, 20,000 via receivable bill.</li><li>July 14: Collected half of initial A/R at 2% discount.</li><li>July 20: Used goods for advertising 5,000 Taka.</li><li>July 31: 1 month of insurance expired.</li></ul>",
        meta: "Comilla · 2017",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Provide the opening journal entry.", 
                answer: "<div class='text-xs space-y-1'><p>Assets (Cash 25k, A/R 40k, Mach 40k, Furn 25k) Dr 1.3L</p><p>A/P Cr 20k; Capital Cr 1.1L</p></div>" 
            },
            { 
                label: "b", 
                text: "Show the effect of transactions from July 5 to 14 on the accounting equation.", 
                answer: "<div class='text-sm font-bold'>Equation Balance (July 14) = <strong>1,61,600 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Determine the owner's equity on July 31.", 
                answer: "<div class='text-sm font-medium'>OE = 1.1L + 70k (Sales) - 70k (Purch) - 5k (Adv) - 2k (Ins) - 400 (Disc) = <strong>1,02,600 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b68",
        stem: "<p>Dilruba Jahan started with 1,00,000 Taka cash on Jan 1, 2016. January transactions:</p><ul class='list-disc ml-6 mt-2'><li>Jan 3: Credit purchase 60,000 Taka.</li><li>Jan 7: Cash sales 40,000 Taka (Cost 25,000).</li><li>Jan 10: Credit sales 40,000 Taka (Cost 20,000).</li><li>Jan 20: Purchase return 2,000 Taka.</li><li>Jan 25: Paid 3/4th of Jan 3 debt at 3% discount.</li><li>Jan 30: Collected 20,000 from Jan 10 sales at 4% discount.</li><li>Jan 31: Bad debt 1,000 Taka.</li></ul>",
        meta: "Sylhet · 2017",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine net purchases and net sales.", 
                answer: "<div class='text-xs space-y-1'><p>Net Purchase = 60k - 2k = 58,000 Taka</p><p>Net Sales = 40k + 40k = <strong>80,000 Taka</strong></p></div>" 
            },
            { 
                label: "b", 
                text: "Prepare a tabular summary of transactions.", 
                answer: "<div class='text-sm font-bold'>Final Asset Total = <strong>1,34,595 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Prepare an income statement for January.", 
                answer: "<div class='text-sm font-medium'>Gross Profit = 35,000 Taka | Net Profit = <strong>31,895 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b69",
        stem: "<p>Mr. Kamran started a law firm with cash 1,00,000 and computer 50,000. January info:</p><ul class='list-disc ml-6 mt-2'><li>Jan 2: Appointed a manager at 15,000 Taka/month.</li><li>Jan 8: Credit furniture purchase 30,000 Taka.</li><li>Jan 12: Cash service revenue 25,000 Taka.</li><li>Jan 18: Credit service revenue 30,000 Taka.</li><li>Jan 20: Personal loan 50,000 taken from bank.</li><li>Jan 30: Paid manager's salary.</li><li>Jan 31: Paid office rent 12,000 Taka.</li></ul>",
        meta: "Jessore · 2017",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Identify non-transactional events and find their total.", 
                answer: "<div class='text-sm font-medium'>Total = Jan 2 (Appt) + Jan 20 (Personal Loan) = <strong>65,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Determine owner's equity at the end of January.", 
                answer: "<div class='text-sm font-bold'>End OE = 1.5L + 55k (Rev) - 27k (Exp) = <strong>1,78,000 Taka</strong></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect on the accounting equation in a descriptive table.", 
                answer: "<div class='text-sm font-bold'>Equation Total = <strong>1,98,000 Taka</strong></div>" 
            }
        ]
    },
    {
        id: "b70",
        stem: "<p>Architect Imran started a firm with cash 50,000, furniture 20,000, and loan 10,000. Transactions:</p><ul class='list-disc ml-6 mt-2'><li>Jan 2: Credit service provided 15,000 Taka.</li><li>Jan 5: Credit purchase of supplies 500 Taka.</li><li>Jan 16: Rent paid 3,000 Taka.</li><li>Jan 31: Loan repayment 5,000 Taka.</li></ul>",
        meta: "Barisal · 2017",
        type: "board",
        questions: [
            { 
                label: "a", 
                text: "Determine the amount of initial capital.", 
                answer: "<div class='text-sm font-medium'>Initial Capital = Cash (50k) + Furniture (20k) = <strong>70,000 Taka</strong></div>" 
            },
            { 
                label: "b", 
                text: "Provide journal entries for the transactions.", 
                answer: "<div class='text-xs space-y-1'><p>Jan 2: A/R Dr 15k; Service Rev Cr 15k</p><p>Jan 5: Supplies Dr 500; A/P Cr 500</p><p>Jan 16: Rent Dr 3k; Cash Cr 3k</p><p>Jan 31: Loan Dr 5k; Cash Cr 5k</p></div>" 
            },
            { 
                label: "c", 
                text: "Show the effect on the accounting equation via tabular analysis.", 
                answer: "<div class='text-sm font-bold'>Final Equation Total = <strong>82,500 Taka</strong></div>" 
            }
        ]
    }
];
