import re
import os

def inject():
    data_path = 'data.js'
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        return

    with open(data_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The new CQ object for Mishu Traders (Dhaka College 2026)
    NEW_CQ = '''{
    "id": 2,
    "stem": "<p>On December 31, 2024, the following reasons for the discrepancy between the Cash Book and Bank Statement of Mishu Traders were identified:</p><ul class=\'list-disc ml-6 mt-2 space-y-1 text-sm\'><li>i. Bank balance as per Cash Book (31-12-2024) was Tk 40,000.</li><li>ii. Tk 20,000 was paid by the bank to creditor Shahanaj, which was not recorded in the Cash Book.</li><li>iii. A debtor directly deposited Tk 8,000 into the bank, not recorded in the Cash Book.</li><li>iv. A check of Tk 5,000 was deposited into the bank for collection but was not collected by the bank by December 31.</li><li>v. Interest allowed by the bank Tk 2,500 was not recorded in the Cash Book.</li><li>vi. Three checks of Tk 2,000, Tk 3,500, and Tk 5,000 were issued, but only the Tk 5,000 check was presented to the bank for payment.</li></ul>",
    "meta": "Dhaka College · 2026",
    "type": "college",
    "questions": [
        {
            "label": "a",
            "text": "Determine the amount of issued checks not yet presented to the bank.",
            "answer": "<div class=\'space-y-2 font-mono\'><p class=\'font-semibold underline text-center text-xs\'><strong>Calculation of Issued Checks Not Presented to Bank</strong></p><div class=\\'overflow-x-auto\'><table class=\\'w-full text-xs border-collapse border border-gray-300\'><tbody><tr><td class=\\'border border-gray-300 p-1 text-left pl-4\'>Total checks issued (Tk 2,000 + Tk 3,500 + Tk 5,000)</td><td class=\\'border border-gray-300 p-1 text-right\'>Tk 10,500</td></tr><tr><td class=\\'border border-gray-300 p-1 text-left pl-4\'>Less: Check presented to bank</td><td class=\\'border border-gray-300 p-1 text-right\'>Tk 5,000</td></tr><tr class=\\'bg-gray-50 font-bold\'><td class=\\'border border-gray-300 p-1 text-left pl-4\'>Issued checks not yet presented</td><td class=\\'border border-gray-300 p-1 text-right\\' style=\\'text-decoration: underline double;\\'>Tk 5,500</td></tr></tbody></table></div></div>"
        },
        {
            "label": "b",
            "text": "Provide journal entries for items (ii), (iii), (iv), and (v).",
            "answer": "<div class=\\'space-y-2 font-mono\'><p class=\\'font-semibold underline text-center text-xs\'>Journal Entries of Mishu Traders</p><p class=\\'text-center text-[10px] text-gray-500\'>(Dated December 31, 2024)</p><div class=\\'overflow-x-auto\'><table class=\\'w-full text-[10px] border-collapse border border-gray-300\'><thead><tr class=\\'bg-gray-100\'><th class=\\'border border-gray-300 p-1 text-left\'>Date</th><th class=\\'border border-gray-300 p-1 text-left\'>Account Titles &amp; Explanations</th><th class=\\'border border-gray-300 p-1\'>L.F.</th><th class=\\'border border-gray-300 p-1 text-right\'>Debit (Tk)</th><th class=\\'border border-gray-300 p-1 text-right\'>Credit (Tk)</th></tr></thead><tbody><tr><td class=\\'border border-gray-300 p-1 align-top\'>2024<br>Dec 31</td><td class=\\'border border-gray-300 p-1 text-left\'>Creditors (Shahanaj) A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank A/C<br><em class=\\'text-[10px] text-gray-500\'>(Payment to creditor by bank recorded)</em></td><td class=\\'border border-gray-300 p-1\'></td><td class=\\'border border-gray-300 p-1 text-right align-top\'>20,000</td><td class=\\'border border-gray-300 p-1 text-right align-top\'>20,000</td></tr><tr><td class=\\'border border-gray-300 p-1 align-top\'>&quot; 31</td><td class=\\'border border-gray-300 p-1 text-left\'>Bank A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accounts Receivable A/C<br><em class=\\'text-[10px] text-gray-500\'>(Direct deposit by debtor into bank recorded)</em></td><td class=\\'border border-gray-300 p-1\'></td><td class=\\'border border-gray-300 p-1 text-right align-top\'>8,000</td><td class=\\'border border-gray-300 p-1 text-right align-top\'>8,000</td></tr><tr><td class=\\'border border-gray-300 p-1 align-top\'>&quot; 31</td><td class=\\'border border-gray-300 p-1 text-left\'>Accounts Receivable A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank A/C<br><em class=\\'text-[10px] text-gray-500\'>(Deposited check not yet collected recorded)</em></td><td class=\\'border border-gray-300 p-1\'></td><td class=\\'border border-gray-300 p-1 text-right align-top\'>5,000</td><td class=\\'border border-gray-300 p-1 text-right align-top\'>5,000</td></tr><tr><td class=\\'border border-gray-300 p-1 align-top\'>&quot; 31</td><td class=\\'border border-gray-300 p-1 text-left\'>Bank A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank Interest A/C<br><em class=\\'text-[10px] text-gray-500\'>(Interest allowed by bank recorded)</em></td><td class=\\'border border-gray-300 p-1\'></td><td class=\\'border border-gray-300 p-1 text-right align-top\'>2,500</td><td class=\\'border border-gray-300 p-1 text-right align-top\'>2,500</td></tr></tbody></table></div></div>"
        },
        {
            "label": "c",
            "text": "Prepare a Bank Reconciliation Statement for Mishu Traders as of December 31, 2024.",
            "answer": "<div class=\\'space-y-2 font-mono\'><p class=\\'font-semibold underline text-center text-xs\'>Bank Reconciliation Statement of Mishu Traders</p><p class=\\'text-center text-[10px] text-gray-500\'>(As on December 31, 2024)</p><div class=\\'overflow-x-auto\'><table class=\\'w-full text-xs border-collapse border border-gray-300\'><thead><tr class=\\'bg-gray-100\'><th class=\\'border border-gray-300 p-1 text-left\'>Particulars</th><th class=\\'border border-gray-300 p-1 text-right\'>Tk.</th><th class=\\'border border-gray-300 p-1 text-right\'>Tk.</th></tr></thead><tbody><tr><td class=\\'border border-gray-300 p-1 font-semibold\'>Bank Balance as per Cash Book</td><td class=\\'border border-gray-300 p-1\'></td><td class=\\'border border-gray-300 p-1 text-right\'>40,000</td></tr><tr><td class=\\'border border-gray-300 p-1 italic\'>Add:</td><td class=\\'border border-gray-300 p-1\'></td><td class=\\'border border-gray-300 p-1\'></td></tr><tr><td class=\\'border border-gray-300 p-1 pl-8\'>Direct deposit by debtor (iii)</td><td class=\\'border border-gray-300 p-1 text-right\'>8,000</td><td class=\\'border border-gray-300 p-1\'></td></tr><tr><td class=\\'border border-gray-300 p-1 pl-8\'>Interest allowed by bank (v)</td><td class=\\'border border-gray-300 p-1 text-right\'>2,500</td><td class=\\'border border-gray-300 p-1\'></td></tr><tr><td class=\\'border border-gray-300 p-1 pl-8\'>Issued checks not presented (vi)</td><td class=\\'border border-gray-300 p-1 text-right border-b border-gray-400\'>5,500</td><td class=\\'border border-gray-300 p-1\'></td></tr><tr class=\\'bg-gray-50\'><td class=\\'border border-gray-300 p-1 pl-8 font-semibold\'>Total Additions</td><td class=\\'border border-gray-300 p-1 text-right font-semibold\\' style=\\'text-decoration: underline;\\'>16,000</td><td class=\\'border border-gray-300 p-1 text-right\'>56,000</td></tr><tr><td class=\\'border border-gray-300 p-1 italic\'>Less:</td><td class=\\'border border-gray-300 p-1\'></td><td class=\\'border border-gray-300 p-1\'></td></tr><tr><td class=\\'border border-gray-300 p-1 pl-8\'>Payment to creditor not in Cash Book (ii)</td><td class=\\'border border-gray-300 p-1 text-right\'>20,000</td><td class=\\'border border-gray-300 p-1\'></td></tr><tr><td class=\\'border border-gray-300 p-1 pl-8\'>Deposited check not yet collected (iv)</td><td class=\\'border border-gray-300 p-1 text-right border-b border-gray-400\'>5,000</td><td class=\\'border border-gray-300 p-1\'></td></tr><tr class=\\'bg-amber-50 font-bold\'><td class=\\'border border-gray-300 p-1\'>Bank Balance as per Bank Statement</td><td class=\\'border border-gray-300 p-1\'></td><td class=\\'border border-gray-300 p-1 text-right\\' style=\\'text-decoration: underline double;\\'>31,000</td></tr></tbody></table></div></div>"
        }
    ]
}'''

    # We need to find the specific part of chapter 3 to append this to.
    # The first CQ in Chapter 3 ends with:
    #             }
    #         ]
    #     }
    # ]
    #         },
    #         "4": {

    # Looking at the actual data.js:
    # 9619:     }
    # 9620: ]
    # 9621:         },
    # 9622:         "4": {

    OLD_PATTERN = '''    }
]
        },
        "4": {'''

    NEW_PATTERN = '''    },
''' + NEW_CQ + '''
]
        },
        "4": {'''

    if OLD_PATTERN in content:
        # We need to make sure we are in the right chapter.
        # Let's check if 'Prabal' is before this pattern.
        # Find the last occurrence of 'Prabal'
        prabal_pos = content.rfind('Prabal')
        pattern_pos = content.find(OLD_PATTERN, prabal_pos)
        
        if prabal_pos != -1 and pattern_pos != -1:
            # We found the pattern after Prabal, which should be the end of Chapter 3 fullCQData.
            new_content = content[:pattern_pos] + NEW_PATTERN + content[pattern_pos + len(OLD_PATTERN):]
            with open(data_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("SUCCESS: Mishu Traders injected into Chapter 3.")
        else:
            print("ERROR: Could not find anchor 'Prabal' or the pattern after it.")
    else:
        print("ERROR: OLD_PATTERN not found in data.js.")

if __name__ == "__main__":
    inject()
