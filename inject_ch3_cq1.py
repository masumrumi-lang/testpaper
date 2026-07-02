import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# The exact target string to replace (ch3's empty fullCQData closing into ch4)
OLD = '''            shortCQData: [],
            fullCQData: []
        },
        "4": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 4 : Trial Balance",'''

NEW = '''            shortCQData: [],
            fullCQData: [
{
    id: 1,
    stem: "<p>Mr. Prabal is a businessman. On June 30, 2024, his bank overdraft as per the Bank Statement was Tk. 11,500. Upon comparing the Cash Book and Bank Statement, the following discrepancies were identified:</p><ul class=\\'list-disc ml-6 mt-2 space-y-1 text-sm\\'><li>i. Out of 5 checks totaling Tk. 55,000 issued to creditors, 3 checks totaling Tk. 40,300 were presented to the bank for payment by June 30.</li><li>ii. A receivable bill of Tk. 5,000 was discounted at the bank for Tk. 4,900, but it was recorded at full value in the Cash Book.</li><li>iii. Bank charges of Tk. 300 and interest allowed by the bank of Tk. 800 were not recorded in the Cash Book.</li><li>iv. A direct deposit of Tk. 2,000 made by a debtor into the bank was not recorded in the Cash Book.</li><li>v. The bank paid a loan installment of Tk. 6,600, which was not entered in the Cash Book.</li></ul>",
    meta: "Dhaka Board - 2025",
    type: "board",
    questions: [
        {
            label: "a",
            text: "Determine the amount of unpresented checks.",
            answer: "<div class=\\'space-y-2 font-mono\\'><p class=\\'font-semibold underline text-center text-xs\\'><strong>Calculation of Unpresented Checks</strong></p><div class=\\'overflow-x-auto\\'><table class=\\'w-full text-xs border-collapse border border-gray-300\\'><tbody><tr><td class=\\'border border-gray-300 p-1 text-left pl-4\\'>Total amount of checks issued to creditors</td><td class=\\'border border-gray-300 p-1 text-right\\'>Tk. 55,000</td></tr><tr><td class=\\'border border-gray-300 p-1 text-left pl-4\\'>Less: Amount of checks presented to the bank</td><td class=\\'border border-gray-300 p-1 text-right\\'>Tk. 40,300</td></tr><tr class=\\'bg-gray-50 font-bold\\'><td class=\\'border border-gray-300 p-1 text-left pl-4\\'>Unpresented Checks (55,000 &minus; 40,300)</td><td class=\\'border border-gray-300 p-1 text-right\\' style=\\'text-decoration: underline double;\\'>Tk. 14,700</td></tr></tbody></table></div></div>"
        },
        {
            label: "b",
            text: "Prepare a Bank Reconciliation Statement using the Single Balance method based on the above information.",
            answer: "<div class=\\'space-y-2 font-mono\\'><p class=\\'font-semibold underline text-center text-xs\\'>Bank Reconciliation Statement of Mr. Prabal</p><p class=\\'text-center text-[10px] text-gray-500\\'>(As on June 30, 2024)</p><div class=\\'overflow-x-auto\\'><table class=\\'w-full text-xs border-collapse border border-gray-300\\'><thead><tr class=\\'bg-gray-100\\'><th class=\\'border border-gray-300 p-1 text-left\\'>Particulars</th><th class=\\'border border-gray-300 p-1 text-right\\'>Tk.</th><th class=\\'border border-gray-300 p-1 text-right\\'>Tk.</th></tr></thead><tbody><tr><td class=\\'border border-gray-300 p-1 font-semibold\\'>Bank Overdraft as per Bank Statement</td><td class=\\'border border-gray-300 p-1\\'></td><td class=\\'border border-gray-300 p-1 text-right\\'>11,500</td></tr><tr><td class=\\'border border-gray-300 p-1 pl-4 italic\\'>Add:</td><td class=\\'border border-gray-300 p-1\\'></td><td class=\\'border border-gray-300 p-1\\'></td></tr><tr><td class=\\'border border-gray-300 p-1 pl-8\\'>Unpresented checks (55,000 &minus; 40,300)</td><td class=\\'border border-gray-300 p-1 text-right\\'>14,700</td><td class=\\'border border-gray-300 p-1\\'></td></tr><tr><td class=\\'border border-gray-300 p-1 pl-8\\'>Interest allowed by the bank (not in Cash Book)</td><td class=\\'border border-gray-300 p-1 text-right\\'>800</td><td class=\\'border border-gray-300 p-1\\'></td></tr><tr><td class=\\'border border-gray-300 p-1 pl-8\\'>Direct deposit by a debtor (not in Cash Book)</td><td class=\\'border border-gray-300 p-1 text-right border-b border-gray-400\\'>2,000</td><td class=\\'border border-gray-300 p-1\\'></td></tr><tr class=\\'bg-gray-50\\'><td class=\\'border border-gray-300 p-1 pl-8 font-semibold\\'>Total Additions</td><td class=\\'border border-gray-300 p-1 text-right font-semibold\\' style=\\'text-decoration: underline;\\'>17,500</td><td class=\\'border border-gray-300 p-1 text-right\\'>29,000</td></tr><tr><td class=\\'border border-gray-300 p-1 pl-4 italic\\'>Less:</td><td class=\\'border border-gray-300 p-1\\'></td><td class=\\'border border-gray-300 p-1\\'></td></tr><tr><td class=\\'border border-gray-300 p-1 pl-8\\'>Excess recorded for bill discounting (5,000 &minus; 4,900)</td><td class=\\'border border-gray-300 p-1 text-right\\'>100</td><td class=\\'border border-gray-300 p-1\\'></td></tr><tr><td class=\\'border border-gray-300 p-1 pl-8\\'>Bank charges not recorded in Cash Book</td><td class=\\'border border-gray-300 p-1 text-right\\'>300</td><td class=\\'border border-gray-300 p-1\\'></td></tr><tr><td class=\\'border border-gray-300 p-1 pl-8\\'>Loan installment paid by bank (not in Cash Book)</td><td class=\\'border border-gray-300 p-1 text-right border-b border-gray-400\\'>6,600</td><td class=\\'border border-gray-300 p-1\\'></td></tr><tr class=\\'bg-gray-50\\'><td class=\\'border border-gray-300 p-1 pl-8 font-semibold\\'>Total Deductions</td><td class=\\'border border-gray-300 p-1 text-right font-semibold\\' style=\\'text-decoration: underline;\\'>7,000</td><td class=\\'border border-gray-300 p-1 text-right border-b border-gray-400\\'>7,000</td></tr><tr class=\\'bg-amber-50 font-bold\\'><td class=\\'border border-gray-300 p-1\\'>Bank Overdraft as per Cash Book</td><td class=\\'border border-gray-300 p-1\\'></td><td class=\\'border border-gray-300 p-1 text-right\\' style=\\'text-decoration: underline double;\\'>22,000</td></tr></tbody></table></div><p class=\\'text-[10px] text-gray-500 italic mt-1\\'>*11,500 + 17,500 &minus; 7,000 = Tk. 22,000 (Bank Overdraft as per Cash Book)</p></div>"
        },
        {
            label: "c",
            text: "Provide Journal Entries for the transactions that were not recorded in the Cash Book.",
            answer: "<div class=\\'space-y-2 font-mono\\'><p class=\\'font-semibold underline text-center text-xs\\'>Journal Entries (Dated June 30, 2024)</p><div class=\\'overflow-x-auto\\'><table class=\\'w-full text-xs border-collapse border border-gray-300\\'><thead><tr class=\\'bg-gray-100\\'><th class=\\'border border-gray-300 p-1 text-left\\'>Date</th><th class=\\'border border-gray-300 p-1 text-left\\'>Account Titles &amp; Explanations</th><th class=\\'border border-gray-300 p-1\\'>L.F.</th><th class=\\'border border-gray-300 p-1 text-right\\'>Debit (Tk)</th><th class=\\'border border-gray-300 p-1 text-right\\'>Credit (Tk)</th></tr></thead><tbody><tr><td class=\\'border border-gray-300 p-1 align-top\\'>2024<br>June 30</td><td class=\\'border border-gray-300 p-1 text-left\\'>Bank Charges A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank A/C<br><em class=\\'text-[10px] text-gray-500\\'>(Bank charges deducted by the bank recorded in the books)</em></td><td class=\\'border border-gray-300 p-1\\'></td><td class=\\'border border-gray-300 p-1 text-right align-top\\'>300</td><td class=\\'border border-gray-300 p-1 text-right align-top\\'><br>300</td></tr><tr><td class=\\'border border-gray-300 p-1 align-top\\'>&quot; 30</td><td class=\\'border border-gray-300 p-1 text-left\\'>Bank A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank Interest A/C<br><em class=\\'text-[10px] text-gray-500\\'>(Interest allowed by the bank recorded in the books)</em></td><td class=\\'border border-gray-300 p-1\\'></td><td class=\\'border border-gray-300 p-1 text-right align-top\\'>800</td><td class=\\'border border-gray-300 p-1 text-right align-top\\'><br>800</td></tr><tr><td class=\\'border border-gray-300 p-1 align-top\\'>&quot; 30</td><td class=\\'border border-gray-300 p-1 text-left\\'>Bank A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accounts Receivable A/C<br><em class=\\'text-[10px] text-gray-500\\'>(Direct deposit by a debtor into the bank recorded)</em></td><td class=\\'border border-gray-300 p-1\\'></td><td class=\\'border border-gray-300 p-1 text-right align-top\\'>2,000</td><td class=\\'border border-gray-300 p-1 text-right align-top\\'><br>2,000</td></tr><tr><td class=\\'border border-gray-300 p-1 align-top\\'>&quot; 30</td><td class=\\'border border-gray-300 p-1 text-left\\'>Loan A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank A/C<br><em class=\\'text-[10px] text-gray-500\\'>(Payment of loan installment by the bank recorded)</em></td><td class=\\'border border-gray-300 p-1\\'></td><td class=\\'border border-gray-300 p-1 text-right align-top\\'>6,600</td><td class=\\'border border-gray-300 p-1 text-right align-top\\'><br>6,600</td></tr></tbody></table></div></div>"
        }
    ]
}
            ]
        },
        "4": {
            subjectName: "Accounting 1st Paper",
            chapterName: "Chapter 4 : Trial Balance",'''

# Count occurrences first
count = content.count(OLD)
print(f"Occurrences of target string: {count}")

if count == 1:
    new_content = content.replace(OLD, NEW, 1)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: acc1_ch3_cq1 injected into data.js")
    
    # Verify
    verify_count = new_content.count('Prabal')
    print(f"Verification - 'Prabal' occurrences in data.js: {verify_count}")
else:
    print("ERROR: Target string not found or found multiple times. Aborting.")
