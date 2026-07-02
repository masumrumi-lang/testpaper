with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id: "b1"')
if idx >= 0:
    # Show first 200 chars of the block
    print("=== STEM PREVIEW ===")
    print(c[idx:idx+400])
    print("\n=== ANSWER (a) PREVIEW ===")
    a_idx = c.find('Ending Accounts Receivable')
    if a_idx >= 0:
        print(c[a_idx:a_idx+100])
    print("\n=== META CHECK ===")
    meta_idx = c.find('Rajshahi Board - 2025', idx)
    if meta_idx >= 0:
        print(c[meta_idx:meta_idx+50])
    print("\n=== EQUATION TOTAL CHECK ===")
    eq_idx = c.find('52,900', idx)
    if eq_idx >= 0:
        print(c[eq_idx-30:eq_idx+30])
    print("\nAll checks passed!")
else:
    print("ERROR: id b1 not found")
