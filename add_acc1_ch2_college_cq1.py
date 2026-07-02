import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Target: The end of the last board CQ in Chapter 2, before the array closes
OLD = '''        }
    ]
}
            ]
        },
        "3": {'''

# We want to insert the new CQ before the closing ] of fullCQData (line 7358 area)
# The Habib CQ ends with line 7357: } (the CQ object)
# Then 7358: ] (the fullCQData array)

TARGET = '''7357: }
7358:             ]
7359:         },
7360:         "3": {'''

# Let's find the exact end of Habib CQ
HABIB_END = '''        }
    ]
}'''

# Since Habib is the only one right now, we can replace the closing ] of the array
SEARCH_STRING = '''        }
    ]
}
            ]
        },
        "3": {'''

NEW_CQ = ''',
{
    id: "01",
    stem: "<p>The transactions of Nadim Traders for the month of June 2024 are as follows:</p><ul class='list-disc ml-6 mt-2 space-y-1 text-sm'><li>June 1: Cash in hand Tk 15,000 and bank balance Tk 20,000.</li><li>June 2: Cash sales to Ratan Store Tk 3,000.</li><li>June 4: Withdrawn from bank Tk 5,000.</li><li>June 7: Cash purchase of Tk 6,000 from Tajul Islam with a 10% discount.</li><li>June 10: Credit purchase Tk 4,000.</li><li>June 12: Paid debt of Tk 4,000 with a 5% discount.</li><li>June 15: Issued a check for Tk 8,400 for a purchase.</li><li>June 20: Received Tk 7,200 from Selina in full settlement of a Tk 7,500 receivable.</li><li>June 28: Paid salary: Tk 2,000 in cash and Tk 1,000 by check.</li><li>June 30: Received sub-rent Tk 3,000.</li></ul>",
    meta: "Dhaka College · 2026",
    type: "college",
    questions: [
        {
            label: "a",
            text: "Determine the total amount of cash discount.",
            answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'>Calculation of Total Cash Discount</p><div class='overflow-x-auto'><table class='w-full text-xs border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1 text-left'>Date</th><th class='border border-gray-300 p-1 text-left'>Particulars</th><th class='border border-gray-300 p-1 text-right'>Tk.</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1'>June 12</td><td class='border border-gray-300 p-1'>Discount Received (4,000 &times; 5%)</td><td class='border border-gray-300 p-1 text-right'>200</td></tr><tr><td class='border border-gray-300 p-1'>June 20</td><td class='border border-gray-300 p-1'>Discount Allowed (7,500 &minus; 7,200)</td><td class='border border-gray-300 p-1 text-right border-b border-gray-400'>300</td></tr><tr class='bg-gray-50 font-bold'><td class='border border-gray-300 p-1' colspan='2'>Total Cash Discount</td><td class='border border-gray-300 p-1 text-right' style='text-decoration: underline double;'>500</td></tr></tbody></table></div></div>"
        },
        {
            label: "b",
            text: "Prepare a Cash Receipts Journal.",
            answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'>Nadim Traders: Cash Receipts Journal</p><div class='overflow-x-auto'><table class='w-full text-[10px] border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Date</th><th class='border border-gray-300 p-1'>Credit Account Title</th><th class='border border-gray-300 p-1'>Ref</th><th class='border border-gray-300 p-1'>Cash (Dr)</th><th class='border border-gray-300 p-1'>Disc Allowed (Dr)</th><th class='border border-gray-300 p-1'>Sales (Cr)</th><th class='border border-gray-300 p-1'>A/R (Cr)</th><th class='border border-gray-300 p-1'>Other (Cr)</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1'>June 2</td><td class='border border-gray-300 p-1'>Sales A/C</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>3,000</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>3,000</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td></tr><tr><td class='border border-gray-300 p-1'>June 20</td><td class='border border-gray-300 p-1'>Selina A/C</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>7,200</td><td class='border border-gray-300 p-1 text-right'>300</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>7,500</td><td class='border border-gray-300 p-1'></td></tr><tr><td class='border border-gray-300 p-1'>June 30</td><td class='border border-gray-300 p-1'>Sub-rent A/C</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>3,000</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>3,000</td></tr><tr class='bg-gray-50 font-bold'><td class='border border-gray-300 p-1' colspan='3'>Total</td><td class='border border-gray-300 p-1 text-right underline'>13,200</td><td class='border border-gray-300 p-1 text-right underline'>300</td><td class='border border-gray-300 p-1 text-right underline'>3,000</td><td class='border border-gray-300 p-1 text-right underline'>7,500</td><td class='border border-gray-300 p-1 text-right underline'>3,000</td></tr></tbody></table></div></div>"
        },
        {
            label: "c",
            text: "Prepare a Cash Payments Journal.",
            answer: "<div class='space-y-2 font-mono'><p class='font-semibold underline text-center text-xs'>Nadim Traders: Cash Payments Journal</p><div class='overflow-x-auto'><table class='w-full text-[10px] border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Date</th><th class='border border-gray-300 p-1'>Debit Account Title</th><th class='border border-gray-300 p-1'>Ref</th><th class='border border-gray-300 p-1'>Purchase (Dr)</th><th class='border border-gray-300 p-1'>A/P (Dr)</th><th class='border border-gray-300 p-1'>Other (Dr)</th><th class='border border-gray-300 p-1'>Disc Rec (Cr)</th><th class='border border-gray-300 p-1'>Cash (Cr)</th></tr></thead><tbody><tr><td class='border border-gray-300 p-1'>June 7</td><td class='border border-gray-300 p-1'>Purchase A/C</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>5,400</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>5,400</td></tr><tr><td class='border border-gray-300 p-1'>June 12</td><td class='border border-gray-300 p-1'>Accounts Payable</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>4,000</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>200</td><td class='border border-gray-300 p-1 text-right'>3,800</td></tr><tr><td class='border border-gray-300 p-1'>June 15</td><td class='border border-gray-300 p-1'>Purchase A/C</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>8,400</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>8,400</td></tr><tr><td class='border border-gray-300 p-1'>June 28</td><td class='border border-gray-300 p-1'>Salary A/C</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>3,000</td><td class='border border-gray-300 p-1'></td><td class='border border-gray-300 p-1 text-right'>3,000</td></tr><tr class='bg-gray-50 font-bold'><td class='border border-gray-300 p-1' colspan='3'>Total</td><td class='border border-gray-300 p-1 text-right underline'>13,800</td><td class='border border-gray-300 p-1 text-right underline'>4,000</td><td class='border border-gray-300 p-1 text-right underline'>3,000</td><td class='border border-gray-300 p-1 text-right underline'>200</td><td class='border border-gray-300 p-1 text-right underline'>20,600</td></tr></tbody></table></div></div>"
        }
    ]
}'''

REPLACEMENT = NEW_CQ + '''
            ]
        },
        "3": {'''

# Find the Habib CQ end and following ]
# 7357: }
# 7358:             ]
# 7359:         },
# 7360:         "3": {

NEW_CONTENT = content.replace(SEARCH_STRING, REPLACEMENT)

if content != NEW_CONTENT:
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(NEW_CONTENT)
    print("SUCCESS: Nadim Traders injected")
else:
    print("ERROR: Target not found")
