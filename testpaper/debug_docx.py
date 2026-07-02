import docx

doc = docx.Document(r"C:\Users\BMTF\.antigravity\testpaper\Acc2_ch4_cq1.docx")
for i, table in enumerate(doc.tables):
    print(f"TABLE {i} START")
    for row in table.rows:
        row_text = [cell.text for cell in row.cells]
        print(f"ROW: {repr(row_text)}")
