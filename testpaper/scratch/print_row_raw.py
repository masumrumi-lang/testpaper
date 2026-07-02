with open(r'c:\Users\BMTF\.antigravity\testpaper\Fin2_all_ch_mcq - Sheet1.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print("Row 254 (raw):", repr(lines[253]))
    print("Row 255 (raw):", repr(lines[254]))
    print("Row 256 (raw):", repr(lines[255]))
