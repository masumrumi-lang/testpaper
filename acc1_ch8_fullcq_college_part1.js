const acc1_ch8_fullcq_college_part1 = [
    {
        id: 1,
        stem: "<p>Mr. Kawsar purchased a machine on Jan 1, 2019, for 9,00,000 Taka. Installation cost was 90,000 and carriage was 40,000. Salvage value is estimated at 30,000. The machine's production units are: 2019 – 10,000 units; 2020 – 15,000 units; 2021 – 10,000 units; 2022 – 8,000 units; and 2023 - 7,000 units.</p>",
        meta: "Dhaka College · 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Determine the depreciable value of the machine.",
                answer: "<div class='space-y-1 font-mono text-xs'><p>Cost = 9,00,000 + 90,000 + 40,000 = 10,30,000</p><p>Depreciable Value = Cost - Salvage</p><p>= 10,30,000 - 30,000 = <strong>10,00,000 Taka</strong></p></div>"
            },
            {
                label: "b",
                text: "Calculate the depreciation rate per unit and show journals for the first two years (Production Method).",
                answer: "<div class='space-y-2 text-xs font-mono'><p>Total Units = 10,000+15,000+10,000+8,000+7,000 = <strong>50,000 units</strong>.</p><p>Rate per unit = 10,00,000 / 50,000 = <strong>20 Taka/unit</strong>.</p><p>2019 Dep = 10,000 &times; 20 = <strong>2,00,000</strong>.</p><p>2020 Dep = 15,000 &times; 20 = <strong>3,00,000</strong>.</p><div class='overflow-x-auto'><p class='font-semibold underline text-center'>Mr. Kawsar &mdash; Journal Entries</p><table class='w-full text-[10px] border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Date</th><th class='border border-gray-300 p-1'>Account Title &amp; Explanation</th><th class='border border-gray-300 p-1'>Ref</th><th class='border border-gray-300 p-1'>Debit (Tk)</th><th class='border border-gray-300 p-1'>Credit (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>2019<br>Jan. 1</td><td class='border p-1'>Machine A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Cash A/C<br><em>(Machine purchased for cash)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>10,30,000</td><td class='border p-1 text-right'><br>10,30,000</td></tr><tr><td class='border p-1'>Dec. 31</td><td class='border p-1'>Depreciation Expense A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation A/C<br><em>(Depreciation charged on machine)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>2,00,000</td><td class='border p-1 text-right'><br>2,00,000</td></tr><tr><td class='border p-1'>&quot; &ndash;31</td><td class='border p-1'>Income Summary A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Depreciation Expense A/C<br><em>(Depreciation expense closed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>2,00,000</td><td class='border p-1 text-right'><br>2,00,000</td></tr><tr><td class='border p-1'>2020<br>Dec. 31</td><td class='border p-1'>Depreciation Expense A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation A/C<br><em>(Depreciation charged on machine)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>3,00,000</td><td class='border p-1 text-right'><br>3,00,000</td></tr><tr><td class='border p-1'>&quot; &ndash;31</td><td class='border p-1'>Income Summary A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Depreciation Expense A/C<br><em>(Depreciation expense closed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>3,00,000</td><td class='border p-1 text-right'><br>3,00,000</td></tr></tbody></table></div><p class='text-[9px] text-gray-500'>*Rate = Depreciable Value &divide; Total Units = 10,00,000 &divide; 50,000 = 20 Tk/unit.</p></div>"
            },
            {
                label: "c",
                text: "Prepare a 5-year depreciation table using the Sum-of-the-Years'-Digits method.",
                answer: "<div class='space-y-3'><p class='text-xs font-semibold underline'>Sum-of-the-Years'-Digits (SYD) Table:</p><table class='w-full text-[10px] border-collapse border border-sky-200 shadow-sm'><thead><tr class='bg-sky-50'> <th class='border border-sky-200 p-1'>Year</th><th class='border border-sky-200 p-1'>Depreciable Value</th><th class='border border-sky-200 p-1'>Fraction</th><th class='border border-sky-200 p-1'>Annual Dep.</th><th class='border border-sky-200 p-1'>Accum. Dep.</th><th class='border border-sky-200 p-1'>Book Value</th> </tr></thead><tbody><tr> <td class='border p-1 text-center'>2019</td><td class='border p-1 text-center'>10,00,000</td><td class='border p-1 text-center'>5/15</td><td class='border p-1 text-right'>3,33,333</td><td class='border p-1 text-right'>3,33,333</td><td class='border p-1 text-right'>6,96,667</td> </tr><tr> <td class='border p-1 text-center'>2020</td><td class='border p-1 text-center'>10,00,000</td><td class='border p-1 text-center'>4/15</td><td class='border p-1 text-right'>2,66,667</td><td class='border p-1 text-right'>6,00,000</td><td class='border p-1 text-right'>4,30,000</td> </tr><tr> <td class='border p-1 text-center'>2021</td><td class='border p-1 text-center'>10,00,000</td><td class='border p-1 text-center'>3/15</td><td class='border p-1 text-right'>2,00,000</td><td class='border p-1 text-right'>8,00,000</td><td class='border p-1 text-right'>2,30,000</td> </tr><tr> <td class='border p-1 text-center'>2022</td><td class='border p-1 text-center'>10,00,000</td><td class='border p-1 text-center'>2/15</td><td class='border p-1 text-right'>1,33,333</td><td class='border p-1 text-right'>9,33,333</td><td class='border p-1 text-right'>96,667</td> </tr><tr> <td class='border p-1 text-center'>2023</td><td class='border p-1 text-center'>10,00,000</td><td class='border p-1 text-center'>1/15</td><td class='border p-1 text-right'>66,667</td><td class='border p-1 text-right'>10,00,000</td><td class='border p-1 text-right'>30,000</td> </tr></tbody></table><p class='text-[9px] text-gray-500'>*Sum = 5+4+3+2+1 = 15. Book Value = Total Cost (10,30,000) - Accum. Dep.</p></div>"
            }
        ]
    },
    {
        id: 2,
        stem: "<p>Reza & Co. bought a machine for 1,50,000 on Jan 1, 2023. A 2nd machine was bought for 1,00,000 on July 1, 2023, and a 3rd for 60,000 on Jan 1, 2024. The 1st machine was sold for 90,000 on July 1, 2024. 20% Straight-line method is used.</p>",
        meta: "Notre Dame College · 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Calculate depreciation for 2023 and 2024.",
                answer: "<div class='text-xs font-mono'><p><strong>2023:</strong><br>M1 (Full yr): 1,50,000 &times; 20% = 30,000<br>M2 (6 mo): 1,00,000 &times; 20% &times; 6/12 = 10,000<br>Total = 40,000</p><p><strong>2024:</strong><br>M1 (Sold Jul 1): 1,50,000 &times; 20% &times; 6/12 = 15,000<br>M2 (Full yr): 1,00,000 &times; 20% = 20,000<br>M3 (Full yr): 60,000 &times; 20% = 12,000<br>Total = 47,000</p></div>"
            },
            {
                label: "b",
                text: "Calculate profit/loss on sale of M1 and give journals.",
                answer: "<div class='text-xs font-mono'><p>Cost = 1,50,000<br>Accum Dep (Yr 2023+2024) = 30,000 + 15,000 = 45,000<br>Book Value = 1,05,000<br>Sale Price = 90,000<br><strong>Loss = 15,000</strong></p><p><strong>Journal:</strong><br>Cash Dr 90,000<br>Loss on Sale Dr 15,000<br>Accum. Dep Dr 45,000<br>Machine Cr 1,50,000</p></div>"
            },
            {
                label: "c",
                text: "Prepare Machine A/C and Depreciation A/C for 2023.",
                answer: "<div class='space-y-4'><p class='text-xs font-bold underline'>Reza & Co. Ledger (2023):</p><div class='overflow-x-auto'><table class='w-full text-[10px] border border-gray-300'><caption class='text-[11px] font-bold py-1 bg-gray-100 border border-gray-300'>Machinery Account</caption><thead><tr class='bg-gray-50'><th class='border p-1'>Date</th><th class='border p-1'>Particulars</th><th class='border p-1'>Ref</th><th class='border p-1'>Debit (Tk)</th><th class='border p-1'>Credit (Tk)</th><th class='border p-1'>Balance (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>2023 Jan 1</td><td class='border p-1'>Bank/Cash</td><td class='border p-1'></td><td class='border p-1 text-right'>1,50,000</td><td class='border p-1'></td><td class='border p-1 text-right'>1,50,000 (Dr)</td></tr><tr><td class='border p-1'>July 1</td><td class='border p-1'>Bank/Cash</td><td class='border p-1'></td><td class='border p-1 text-right'>1,00,000</td><td class='border p-1'></td><td class='border p-1 text-right'>2,50,000 (Dr)</td></tr></tbody></table></div><div class='overflow-x-auto'><table class='w-full text-[10px] border border-gray-300'><caption class='text-[11px] font-bold py-1 bg-gray-100 border border-gray-300'>Depreciation Account</caption><thead><tr class='bg-gray-50'><th class='border p-1'>Date</th><th class='border p-1'>Particulars</th><th class='border p-1'>Ref</th><th class='border p-1'>Debit (Tk)</th><th class='border p-1'>Credit (Tk)</th><th class='border p-1'>Balance (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>2023 Dec 31</td><td class='border p-1'>Accum. Depreciation</td><td class='border p-1'></td><td class='border p-1 text-right'>40,000</td><td class='border p-1'></td><td class='border p-1 text-right'>40,000 (Dr)</td></tr><tr><td class='border p-1'>Dec 31</td><td class='border p-1'>Income Summary</td><td class='border p-1'></td><td class='border p-1'></td><td class='border p-1 text-right'>40,000</td><td class='border p-1 text-right'>0</td></tr></tbody></table></div></div>"
            }
        ]
    },
    {
        id: 3,
        stem: "<p>Khan Ltd. imported a machine for 30,00,000 on July 1, 2023. Duty: 3,00,000; Carriage: 1,00,000; Installation: 2,00,000. Life 10 yrs, Salvage: 6,00,000. Reducing Balance method is used.</p>",
        meta: "RAJUK Uttara Model College · 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Determine the depreciable value.",
                answer: "<p class='font-mono text-xs'>Total Cost = 30+3+1+2 = 36,00,000. <br>Depreciable Value = 36,00,000 - 6,00,000 = <strong>30,00,000 Taka</strong> (Note: While base is cost for RB, question asks specifically for depreciable value).</p>"
            },
            {
                label: "b",
                text: "Show journals for 2023 and 2024.",
                answer: "<div class='space-y-2 text-xs font-mono'><p>RB Rate = (100/10) &times; 2 = <strong>20%</strong>.</p><p>Total Cost = 30,00,000 + 3,00,000 + 1,00,000 + 2,00,000 = <strong>36,00,000</strong>.</p><p>2023 Dep (6 mo) = 36,00,000 &times; 20% &times; 6/12 = <strong>3,60,000</strong>.</p><p>2024 Dep = (36,00,000 - 3,60,000) &times; 20% = <strong>6,48,000</strong>.</p><div class='overflow-x-auto'><p class='font-semibold underline text-center'>Khan Ltd. &mdash; Journal Entries</p><table class='w-full text-[10px] border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Date</th><th class='border border-gray-300 p-1'>Account Title &amp; Explanation</th><th class='border border-gray-300 p-1'>Ref</th><th class='border border-gray-300 p-1'>Debit (Tk)</th><th class='border border-gray-300 p-1'>Credit (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>2023<br>July 1</td><td class='border p-1'>Machine A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank A/C<br><em>(Machine imported &amp; installed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>36,00,000</td><td class='border p-1 text-right'><br>36,00,000</td></tr><tr><td class='border p-1'>Dec. 31</td><td class='border p-1'>Depreciation Expense A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation A/C<br><em>(6 months depreciation charged)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>3,60,000</td><td class='border p-1 text-right'><br>3,60,000</td></tr><tr><td class='border p-1'>&quot; &ndash;31</td><td class='border p-1'>Income Summary A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Depreciation Expense A/C<br><em>(Depreciation expense closed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>3,60,000</td><td class='border p-1 text-right'><br>3,60,000</td></tr><tr><td class='border p-1'>2024<br>Dec. 31</td><td class='border p-1'>Depreciation Expense A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation A/C<br><em>(Full year depreciation charged)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>6,48,000</td><td class='border p-1 text-right'><br>6,48,000</td></tr><tr><td class='border p-1'>&quot; &ndash;31</td><td class='border p-1'>Income Summary A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Depreciation Expense A/C<br><em>(Depreciation expense closed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>6,48,000</td><td class='border p-1 text-right'><br>6,48,000</td></tr></tbody></table></div></div>"
            },
            {
                label: "c",
                text: "Prepare Depreciation A/C and Accumulated Dep A/C for 2023-2025.",
                answer: "<div class='space-y-4'><p class='text-[11px] font-bold'>Ledger Extracts for Khan Ltd. (2023-2025):</p><table class='w-full text-[10px] border border-gray-300'><caption class='font-bold bg-sky-50 p-1 border'>Accumulated Depreciation Account</caption><thead><tr class='bg-gray-100'><th class='border p-1'>Date</th><th class='border p-1'>Particulars</th><th class='border p-1'>Dr (Tk)</th><th class='border p-1'>Cr (Tk)</th><th class='border p-1'>Balance (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>2023 Dec 31</td><td class='border p-1'>Depreciation Exp</td><td class='border p-1'></td><td class='border p-1 text-right'>3,60,000</td><td class='border p-1 text-right'>3,60,000 (Cr)</td></tr><tr><td class='border p-1'>2024 Dec 31</td><td class='border p-1'>Depreciation Exp</td><td class='border p-1'></td><td class='border p-1 text-right'>6,48,000</td><td class='border p-1 text-right'>10,08,000 (Cr)</td></tr><tr><td class='border p-1'>2025 Dec 31</td><td class='border p-1'>Depreciation Exp</td><td class='border p-1'></td><td class='border p-1 text-right'>5,18,400</td><td class='border p-1 text-right'>15,26,400 (Cr)</td></tr></tbody></table><table class='w-full text-[10px] border border-gray-300'><caption class='font-bold bg-sky-50 p-1 border'>Depreciation Account (Example 2024)</caption><tbody><tr class='bg-gray-100'><th class='border p-1'>Date</th><th class='border p-1'>Particulars</th><th class='border p-1'>Dr (Tk)</th><th class='border p-1'>Cr (Tk)</th><th class='border p-1'>Balance</th></tr><tr><td class='border p-1'>2024 Dec 31</td><td class='border p-1'>Accum. Depreciation</td><td class='border p-1 text-right'>6,48,000</td><td class='border p-1'></td><td class='border p-1 text-right'>6,48,000 (Dr)</td></tr><tr><td class='border p-1'>2024 Dec 31</td><td class='border p-1'>Income Summary</td><td class='border p-1'></td><td class='border p-1 text-right'>6,48,000</td><td class='border p-1 text-right'>0</td></tr></tbody></table></div>"
            }
        ]
    },
    {
        id: 4,
        stem: "<p>On Jan 1, 2023, Saikat Bros Machine balance: 1,00,000 and Accum. Dep: 14,500. On Apr 1, 2024, bought another for 70,000 and spent 30,000 for installation. 10% Reducing Balance method is used.</p>",
        meta: "Notre Dame College · 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Calculate depreciation for 2023 and 2024.",
                answer: "<div class='text-xs font-mono'><p><strong>2023:</strong> (1,00,000 - 14,500) &times; 10% = 8,550.</p><p><strong>2024:</strong><br>M1: (85,500 - 8,550) &times; 10% = 7,695.<br>M2: 1,00,000 &times; 10% &times; 9/12 = 7,500.<br>Total = 15,195.</p></div>"
            },
            {
                label: "b",
                text: "Prepare Dep A/C and Accum Dep A/C for 2023-2024.",
                answer: "<p class='text-xs'>Accum Dep Bal Dec 31, 2024 = 14,500 + 8,550 + 15,195 = 38,245. Ledgers follow standard dual-entry format closing to income summary.</p>"
            },
            {
                label: "c",
                text: "Show presentation in the Balance Sheet.",
                answer: "<div class='space-y-3'><p class='text-[11px] font-bold underline'>Balance Sheet Presentation (Extract):</p><table class='w-full text-xs border border-gray-300'><thead><tr class='bg-gray-100'><th class='border p-1'>Assets</th><th class='border p-1'>Amount (Tk)</th><th class='border p-1'>Total (Tk)</th></tr></thead><tbody><tr><td class='border p-1 font-semibold'>Fixed Assets:</td><td class='border p-1'></td><td class='border p-1'></td></tr><tr><td class='border p-1 pl-4'>Machinery (1,00,000 + 1,00,000)</td><td class='border p-1 text-right'>2,00,000</td><td class='border p-1'></td></tr><tr><td class='border p-1 pl-4'>Less: Accumulated Depreciation</td><td class='border p-1 text-right italic underline'>(38,245)</td><td class='border p-1'></td></tr><tr><td class='border p-1 font-bold'>Net Book Value (Dec 31, 2024)</td><td class='border p-1'></td><td class='border p-1 text-right font-bold'>1,61,755</td></tr></tbody></table><p class='text-[10px] italic text-gray-500'>*Accumulated Depreciation = Opening (14,500) + 2023 (8,550) + 2024 (15,195).</p></div>"
            }
        ]
    },
    {
        id: 5,
        stem: "<p>Ahnaf Traders bought a machine for 4,00,000 on July 1, 2023. Life 5 yrs, salvage 40,000. Reducing Balance method is used.</p>",
        meta: "Dhaka Commerce College · 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Determine 2023 and 2024 depreciation.",
                answer: "<div class='text-xs font-mono'><p>Rate = (100/5)&times;2 = 40%.</p><p>2023 Dep (6 mo): 4,00,000 &times; 40% &times; 6/12 = 80,000.</p><p>2024 Dep: (4,00,000 - 80,000) &times; 40% = 1,28,000.</p></div>"
            },
            {
                label: "b",
                text: "Prepare Dep A/C and Accum Dep A/C for 2023-2024.",
                answer: "<div class='space-y-3'><p class='text-[10px] font-bold underline text-center'>Ahnaf Traders &mdash; Ledgers (2023-2024)</p><table class='w-full text-[10px] border border-gray-300 shadow-sm'><caption class='font-bold bg-gray-100 p-1 border border-gray-300'>Depreciation Account</caption><thead><tr class='bg-gray-50'><th class='border p-1'>Date</th><th class='border p-1'>Particulars</th><th class='border p-1'>Dr (Tk)</th><th class='border p-1'>Cr (Tk)</th><th class='border p-1'>Balance</th></tr></thead><tbody><tr><td class='border p-1'>2023 Dec 31</td><td class='border p-1'>Accum. Depreciation</td><td class='border p-1 text-right'>80,000</td><td class='border p-1'></td><td class='border p-1 text-right'>80,000 (Dr)</td></tr><tr><td class='border p-1'>2023 Dec 31</td><td class='border p-1'>Income Summary</td><td class='border p-1'></td><td class='border p-1 text-right'>80,000</td><td class='border p-1 text-right'>0</td></tr><tr><td class='border p-1'>2024 Dec 31</td><td class='border p-1'>Accum. Depreciation</td><td class='border p-1 text-right'>1,28,000</td><td class='border p-1'></td><td class='border p-1 text-right'>1,28,000 (Dr)</td></tr><tr><td class='border p-1'>2024 Dec 31</td><td class='border p-1'>Income Summary</td><td class='border p-1'></td><td class='border p-1 text-right'>1,28,000</td><td class='border p-1 text-right'>0</td></tr></tbody></table><table class='w-full text-[10px] border border-gray-300 mt-2 shadow-sm'><caption class='font-bold bg-gray-100 p-1 border border-gray-300'>Accumulated Depreciation Account</caption><thead><tr class='bg-gray-50'><th class='border p-1'>Date</th><th class='border p-1'>Particulars</th><th class='border p-1'>Dr (Tk)</th><th class='border p-1'>Cr (Tk)</th><th class='border p-1'>Balance</th></tr></thead><tbody><tr><td class='border p-1'>2023 Dec 31</td><td class='border p-1'>Depreciation Exp</td><td class='border p-1'></td><td class='border p-1 text-right'>80,000</td><td class='border p-1 text-right'>80,000 (Cr)</td></tr><tr><td class='border p-1'>2024 Dec 31</td><td class='border p-1'>Depreciation Exp</td><td class='border p-1'></td><td class='border p-1 text-right'>1,28,000</td><td class='border p-1 text-right font-bold bg-amber-50'>2,08,000 (Cr)</td></tr></tbody></table></div>"
            },
            {
                label: "c",
                text: "Show presentation in the Balance Sheet.",
                answer: "<div class='space-y-3'><p class='text-xs font-bold'>Balance Sheet (Extract) as of Dec 31, 2024:</p><table class='w-full text-xs border border-gray-400'><thead><tr class='bg-gray-100'><th class='border p-1'>Assets</th><th class='border p-1'>Taka</th><th class='border p-1'>Taka</th></tr></thead><tbody><tr><td class='border p-1'>Fixed Assets:</td><td class='border p-1'></td><td class='border p-1'></td></tr><tr><td class='border p-1 pl-3'>Machinery</td><td class='border p-1 text-right'>4,00,000</td><td class='border p-1'></td></tr><tr><td class='border p-1 pl-3'>(-) Accumulated Depreciation</td><td class='border p-1 text-right underline'>(2,08,000)</td><td class='border p-1'></td></tr><tr><td class='border p-1 font-bold'>Net Asset Value</td><td class='border p-1'></td><td class='border p-1 text-right font-bold'>1,92,000</td></tr></tbody></table><div class='p-2 bg-emerald-50 text-[10px] border-l-4 border-emerald-400'><p><strong>Working:</strong> Accum. Dep = 80,000 (2023) + 1,28,000 (2024) = 2,08,000.</p></div></div>"
            }
        ]
    },
    {
        id: 6,
        stem: "<p>Nadia Co. bought a machine for 1,20,000 on Jan 1, 2023. Life 10 yrs, salvage 20,000. Sold for 80,000 on Dec 31, 2024. Straight-line method used.</p>",
        meta: "Dhaka Commerce College · 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Determine profit or loss on sale.",
                answer: "<div class='text-xs font-mono'><p>Annual Dep = (1,20,000 - 20,000)/10 = 10,000.</p><p>Accum Dep (2 yrs) = 20,000.</p><p>Book Value = 1,00,000. Sale = 80,000. <strong>Loss = 20,000</strong>.</p></div>"
            },
            {
                label: "b",
                text: "Show journals for 2023 and 2024.",
                answer: "<p class='text-xs'>2023: Machine Dr 1.2L, Cash Cr 1.2L; Dep Dr 10k, Accum Dep Cr 10k.</p><p>2024: Dep Dr 10k; Cash Dr 80k, Loss Dr 20k, Accum Dep Dr 20k, Machine Cr 1.2L.</p>"
            },
            {
                label: "c",
                text: "Prepare Machine A/C and Accum Dep A/C for 2023-2024.",
                answer: "<div class='space-y-4'><p class='text-xs font-bold'>Ledgers (Final Settlement):</p><table class='w-full text-[10px] border border-gray-300'><caption class='font-bold bg-amber-50 p-1 border'>Machinery Account</caption><thead><tr><th class='border p-1'>Date</th><th class='border p-1'>Details</th><th class='border p-1'>Dr</th><th class='border p-1'>Cr</th><th class='border p-1'>Bal</th></tr></thead><tbody><tr><td class='border p-1'>2023 Jan 1</td><td class='border p-1'>Cash</td><td class='border p-1 text-right'>1,20,000</td><td class='border p-1'></td><td class='border p-1 text-right'>1,20,000</td></tr><tr><td class='border p-1'>2024 Dec 31</td><td class='border p-1'>Disposal/Sale</td><td class='border p-1'></td><td class='border p-1 text-right'>1,20,000</td><td class='border p-1 text-right'>0</td></tr></tbody></table><table class='w-full text-[10px] border border-gray-300'><caption class='font-bold bg-amber-50 p-1 border'>Accumulated Depreciation Account</caption><thead><tr><th class='border p-1'>Date</th><th class='border p-1'>Details</th><th class='border p-1'>Dr</th><th class='border p-1'>Cr</th><th class='border p-1'>Bal</th></tr></thead><tbody><tr><td class='border p-1'>2023 Dec 31</td><td class='border p-1'>Depreciation</td><td class='border p-1'></td><td class='border p-1 text-right'>10,000</td><td class='border p-1 text-right'>10,000 (Cr)</td></tr><tr><td class='border p-1'>2024 Dec 31</td><td class='border p-1'>Depreciation</td><td class='border p-1'></td><td class='border p-1 text-right'>10,000</td><td class='border p-1 text-right'>20,000 (Cr)</td></tr><tr><td class='border p-1'>2024 Dec 31</td><td class='border p-1'>Machine (Transfer)</td><td class='border p-1 text-right'>20,000</td><td class='border p-1'></td><td class='border p-1 text-right'>0</td></tr></tbody></table></div>"
            }
        ]
    },
    {
        id: 7,
        stem: "<p>Jan 1, 2022: Machine 9,50,000, Carriage 15,000, Installation 35,000 (installed Mar 1). Life 10 yrs, salvage 30,000. July 1, 2023: 2nd Machine 10,00,000, Installation 20,000. Life 8 yrs, salvage 50,000. SLM used.</p>",
        meta: "Govt. Azizul Haque College · 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Determine 2022 depreciation.",
                answer: "<div class='text-xs font-mono'><p>M1 Cost = 10,00,000. Depreciable = 9,70,000.</p><p>Note: Ready for use on Mar 1 (10 months).</p><p>2022 Dep = (9,70,000/10) &times; 10/12 = 80,833.</p></div>"
            },
            {
                label: "b",
                text: "Show journals for 2022 and 2023.",
                answer: "<div class='space-y-2 text-xs font-mono'><p>M1 Annual Dep = (10,00,000 - 30,000)/10 = 97,000.</p><p>M2 Cost = 10,00,000 + 20,000 = 10,20,000. Depreciable = 10,20,000 - 50,000 = 9,70,000.</p><p>M2 Dep (6 mo) = (9,70,000/8) &times; 6/12 = <strong>60,625</strong>.</p><div class='overflow-x-auto'><p class='font-semibold underline text-center'>Journal Entries</p><table class='w-full text-[10px] border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Date</th><th class='border border-gray-300 p-1'>Account Title &amp; Explanation</th><th class='border border-gray-300 p-1'>Ref</th><th class='border border-gray-300 p-1'>Debit (Tk)</th><th class='border border-gray-300 p-1'>Credit (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>2022<br>Mar. 1</td><td class='border p-1'>Machine A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank A/C<br><em>(M1 purchased &amp; installed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>10,00,000</td><td class='border p-1 text-right'><br>10,00,000</td></tr><tr><td class='border p-1'>Dec. 31</td><td class='border p-1'>Depreciation Expense A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation A/C<br><em>(M1: 10 months dep. charged)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>80,833</td><td class='border p-1 text-right'><br>80,833</td></tr><tr><td class='border p-1'>&quot; &ndash;31</td><td class='border p-1'>Income Summary A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Depreciation Expense A/C<br><em>(Depreciation expense closed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>80,833</td><td class='border p-1 text-right'><br>80,833</td></tr><tr><td class='border p-1'>2023<br>July 1</td><td class='border p-1'>Machine A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank A/C<br><em>(M2 purchased &amp; installed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>10,20,000</td><td class='border p-1 text-right'><br>10,20,000</td></tr><tr><td class='border p-1'>Dec. 31</td><td class='border p-1'>Depreciation Expense A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation A/C<br><em>(M1: 97,000 + M2: 60,625 = 1,57,625)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>1,57,625</td><td class='border p-1 text-right'><br>1,57,625</td></tr><tr><td class='border p-1'>&quot; &ndash;31</td><td class='border p-1'>Income Summary A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Depreciation Expense A/C<br><em>(Depreciation expense closed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>1,57,625</td><td class='border p-1 text-right'><br>1,57,625</td></tr></tbody></table></div></div>"
            },
            {
                label: "c",
                text: "Prepare Dep A/C and Accum Dep A/C for 2022-2023.",
                answer: "<div class='space-y-4'><p class='text-xs font-bold'>Combined Ledger Analysis:</p><table class='w-full text-[10px] border border-gray-400 shadow-sm'><caption class='bg-sky-100 font-bold p-1 border border-gray-400'>Accumulated Depreciation Account</caption><thead><tr class='bg-gray-100'><th class='border p-1'>Date</th><th class='border p-1'>Description</th><th class='border p-1'>Dr (Tk)</th><th class='border p-1'>Cr (Tk)</th><th class='border p-1'>Balance</th></tr></thead><tbody><tr><td class='border p-1'>2022 Dec 31</td><td class='border p-1'>Depreciation Expense</td><td class='border p-1'></td><td class='border p-1 text-right'>80,833</td><td class='border p-1 text-right'>80,833 (Cr)</td></tr><tr><td class='border p-1'>2023 Dec 31</td><td class='border p-1'>Depreciation Expense</td><td class='border p-1'></td><td class='border p-1 text-right'>1,57,625</td><td class='border p-1 text-right'>2,38,458 (Cr)</td></tr></tbody></table><div class='p-2 bg-sky-50 text-[10px] italic border-l-2 border-sky-400'><p>Note: 2023 Depreciation = M1 (97,000) + M2 (60,625) = 1,57,625.</p></div></div>"
            }
        ]
    },
    {
        id: 8,
        stem: "<p>CF Moto Ltd. bought a machine for 5,00,000 on Jan 1, 2021. Carriage 50,000, installation 20,000. Life 10 yrs, salvage 50,000. Reducing Balance method used.</p>",
        meta: "Cantonment College, Jashore · 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Determine the Reducing Balance depreciation rate.",
                answer: "<p class='font-mono text-xs'>(100 / 10) &times; 2 = <strong>20%</strong>.</p>"
            },
            {
                label: "b",
                text: "Prepare a 4-year depreciation table.",
                answer: "<div class='text-[10px]'><p>Cost: 5,70,000. </p>Yr 1: 1,14,000 (BV 4,56,000)<br>Yr 2: 91,200 (BV 3,64,800)<br>Yr 3: 72,960 (BV 2,91,840)<br>Yr 4: 58,368 (BV 2,33,472)</div>"
            },
            {
                label: "c",
                text: "Prepare Income Statement and Balance Sheet extracts for the first 2 years.",
                answer: "<div class='space-y-4'><p class='text-xs font-bold'>Financial Statement Extracts (2021-2022):</p><table class='w-full text-[10px] border border-emerald-400'><caption class='bg-emerald-50 font-bold p-1 border border-emerald-400'>Income Statement (Partial)</caption><thead><tr class='bg-gray-100'> <th class='border p-1'>Year</th><th class='border p-1'>Expense Description</th><th class='border p-1 text-right'>Amount (Tk)</th> </tr></thead><tbody><tr> <td class='border p-1 text-center'>2021</td><td class='border p-1'>Depreciation Expense (Machinery)</td><td class='border p-1 text-right'>1,14,000</td> </tr><tr> <td class='border p-1 text-center'>2022</td><td class='border p-1'>Depreciation Expense (Machinery)</td><td class='border p-1 text-right'>91,200</td> </tr></tbody></table><table class='w-full text-[10px] border border-emerald-400 mt-2'><caption class='bg-emerald-50 font-bold p-1 border border-emerald-400'>Balance Sheet (Extract)</caption><thead><tr class='bg-gray-100'> <th class='border p-1'>Year</th><th class='border p-1'>Asset Detail</th><th class='border p-1 text-right'>Net Value (Tk)</th> </tr></thead><tbody><tr> <td class='border p-1 text-center'>2021</td><td class='border p-1'>Machine (5,70,000 - 1,14,000)</td><td class='border p-1 text-right font-bold'>4,56,000</td> </tr><tr> <td class='border p-1 text-center'>2022</td><td class='border p-1'>Machine (5,70,000 - 2,05,200)</td><td class='border p-1 text-right font-bold'>3,64,800</td> </tr></tbody></table></div>"
            }
        ]
    },
    {
        id: 9,
        stem: "<p>Rupali Ltd. imported a machine for 20,00,000 on July 1, 2018. Duty: 2,20,000; Carriage: 80,000; Installation: 1,00,000. Life 10 yrs, salvage 2,00,000. Reducing Balance method used.</p>",
        meta: "Govt. Commerce College, Chattogram · 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Determine the Reducing Balance rate.",
                answer: "<p class='font-mono text-xs'>(100 / 10) &times; 2 = <strong>20%</strong>.</p>"
            },
            {
                label: "b",
                text: "Show journals for 2018 and 2019.",
                answer: "<div class='space-y-2 text-xs font-mono'><p>Cost = 20,00,000 + 2,20,000 + 80,000 + 1,00,000 = <strong>24,00,000</strong>.</p><p>2018 Dep (6 mo) = 24,00,000 &times; 20% &times; 6/12 = <strong>2,40,000</strong>.</p><p>2019 Dep = (24,00,000 - 2,40,000) &times; 20% = <strong>4,32,000</strong>.</p><div class='overflow-x-auto'><p class='font-semibold underline text-center'>Rupali Ltd. &mdash; Journal Entries</p><table class='w-full text-[10px] border-collapse border border-gray-300'><thead><tr class='bg-gray-100'><th class='border border-gray-300 p-1'>Date</th><th class='border border-gray-300 p-1'>Account Title &amp; Explanation</th><th class='border border-gray-300 p-1'>Ref</th><th class='border border-gray-300 p-1'>Debit (Tk)</th><th class='border border-gray-300 p-1'>Credit (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>2018<br>July 1</td><td class='border p-1'>Machine A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Bank A/C<br><em>(Machine imported &amp; installed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>24,00,000</td><td class='border p-1 text-right'><br>24,00,000</td></tr><tr><td class='border p-1'>Dec. 31</td><td class='border p-1'>Depreciation Expense A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation A/C<br><em>(6 months dep. charged @ 20% RB)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>2,40,000</td><td class='border p-1 text-right'><br>2,40,000</td></tr><tr><td class='border p-1'>&quot; &ndash;31</td><td class='border p-1'>Income Summary A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Depreciation Expense A/C<br><em>(Depreciation expense closed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>2,40,000</td><td class='border p-1 text-right'><br>2,40,000</td></tr><tr><td class='border p-1'>2019<br>Dec. 31</td><td class='border p-1'>Depreciation Expense A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Accumulated Depreciation A/C<br><em>(Full year dep. charged @ 20% RB)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>4,32,000</td><td class='border p-1 text-right'><br>4,32,000</td></tr><tr><td class='border p-1'>&quot; &ndash;31</td><td class='border p-1'>Income Summary A/C<br>&nbsp;&nbsp;&nbsp;&nbsp;Depreciation Expense A/C<br><em>(Depreciation expense closed)</em></td><td class='border p-1'></td><td class='border p-1 text-right'>4,32,000</td><td class='border p-1 text-right'><br>4,32,000</td></tr></tbody></table></div></div>"
            },
            {
                label: "c",
                text: "Calculate the balance of Accumulated Depreciation on Dec 31, 2022 via ledgers.",
                answer: "<div class='space-y-4'><p class='text-xs font-bold underline'>Accumulated Depreciation Ledger (Running Balance):</p><table class='w-full text-[10px] border border-gray-300 shadow-sm'><thead><tr class='bg-gray-50'><th class='border p-1'>Date</th><th class='border p-1'>Particulars</th><th class='border p-1 text-right'>Credit (Tk)</th><th class='border p-1 text-right'>Balance (Tk)</th></tr></thead><tbody><tr><td class='border p-1'>2018 Dec 31</td><td class='border p-1'>Depreciation Expense</td><td class='border p-1 text-right'>2,40,000</td><td class='border p-1 text-right'>2,40,000 (Cr)</td></tr><tr><td class='border p-1'>2019 Dec 31</td><td class='border p-1'>Depreciation Expense</td><td class='border p-1 text-right'>4,32,000</td><td class='border p-1 text-right'>6,72,000 (Cr)</td></tr><tr><td class='border p-1'>2020 Dec 31</td><td class='border p-1'>Depreciation Expense</td><td class='border p-1 text-right'>3,45,600</td><td class='border p-1 text-right'>10,17,600 (Cr)</td></tr><tr><td class='border p-1'>2021 Dec 31</td><td class='border p-1'>Depreciation Expense</td><td class='border p-1 text-right'>2,76,480</td><td class='border p-1 text-right'>12,94,080 (Cr)</td></tr><tr><td class='border p-1 font-bold'>2022 Dec 31</td><td class='border p-1 font-bold'>Depreciation Expense</td><td class='border p-1 text-right font-bold'>2,21,184</td><td class='border p-1 text-right font-bold bg-amber-50'>15,15,264 (Cr)</td></tr></tbody></table><p class='text-[10px] italic text-gray-500'>The final balance of Accumulated Depreciation at end of 2022 is 15,15,264 Taka.</p></div>"
            }
        ]
    },
    {
        id: 10,
        stem: "<p>Madhab Ent. imported a machine for 3,00,000 on Jan 1, 2024. Duty: 30,000; Freight: 20,000. Installed on Mar 1 for 10,000. Life 5 yrs, salvage 40,000. SLM used.</p>",
        meta: "Ananda Mohan College · 2024",
        type: "college",
        questions: [
            {
                label: "a",
                text: "Determine the acquisition cost.",
                answer: "<p class='font-mono text-xs'>3,00,000 + 30,000 + 20,000 + 10,000 = <strong>3,60,000 Taka</strong>.</p>"
            },
            {
                label: "b",
                text: "Show journals for 2024 and 2025 using straight-line depreciation.",
                answer: "<div class='text-xs font-mono'><p>Depreciable = 3,20,000. Annual Dep = 64,000.</p><p>2024 Dep (10 mo from Mar 1) = 64,000 &times; 10/12 = 53,333.<br>2025 Dep (Full) = 64,000.</p></div>"
            },
            {
                label: "c",
                text: "Prepare Dep A/C and Accum Dep A/C for 2024-2025.",
                answer: "<div class='space-y-4'><p class='text-[10px] font-bold text-center underline'>Madhab Enterprise Ledger (Moving Balance Format)</p><table class='w-full text-[10px] border border-emerald-300 shadow-md'><caption class='font-bold bg-emerald-100 p-1 border-emerald-300'>Depreciation Account</caption><thead><tr class='bg-emerald-50'> <th class='border p-1'>Date</th> <th class='border p-1'>Description</th> <th class='border p-1'>Dr (Tk)</th> <th class='border p-1'>Cr (Tk)</th> <th class='border p-1'>Bal (Tk)</th> </tr></thead><tbody><tr> <td class='border p-1'>2024 Dec 31</td> <td class='border p-1'>Accum. Dep</td> <td class='border p-1 text-right'>53,333</td> <td class='border p-1'></td> <td class='border p-1 text-right'>53,333 (Dr)</td> </tr><tr> <td class='border p-1'>2024 Dec 31</td> <td class='border p-1'>Income Summary</td> <td class='border p-1'></td> <td class='border p-1 text-right'>53,333</td> <td class='border p-1 text-right'>0</td> </tr><tr> <td class='border p-1'>2025 Dec 31</td> <td class='border p-1'>Accum. Dep</td> <td class='border p-1 text-right'>64,000</td> <td class='border p-1'></td> <td class='border p-1 text-right'>64,000 (Dr)</td> </tr><tr> <td class='border p-1'>2025 Dec 31</td> <td class='border p-1'>Income Summary</td> <td class='border p-1'></td> <td class='border p-1 text-right'>64,000</td> <td class='border p-1 text-right'>0</td> </tr></tbody></table><table class='w-full text-[10px] border border-emerald-300 shadow-md'><caption class='font-bold bg-emerald-100 p-1 border-emerald-300'>Accumulated Depreciation Account</caption><thead><tr class='bg-emerald-50'> <th class='border p-1'>Date</th> <th class='border p-1'>Description</th> <th class='border p-1'>Dr (Tk)</th> <th class='border p-1'>Cr (Tk)</th> <th class='border p-1'>Bal (Tk)</th> </tr></thead><tbody><tr> <td class='border p-1'>2024 Dec 31</td> <td class='border p-1'>Depreciation Exp</td> <td class='border p-1'></td> <td class='border p-1 text-right'>53,333</td> <td class='border p-1 text-right'>53,333 (Cr)</td> </tr><tr> <td class='border p-1 font-bold'>2025 Dec 31</td> <td class='border p-1'>Depreciation Exp</td> <td class='border p-1'></td> <td class='border p-1 text-right'>64,000</td> <td class='border p-1 text-right font-bold bg-yellow-50'>1,17,333 (Cr)</td> </tr></tbody></table></div>"
            }
        ]
    }
];
