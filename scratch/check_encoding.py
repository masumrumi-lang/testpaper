with open('data.js', 'rb') as f:
    head = f.read(100)
    print("Raw bytes:", head)
    try:
        print("As UTF-8:", head.decode('utf-8'))
    except Exception as e:
        print("UTF-8 decode failed:", e)
    try:
        print("As UTF-16:", head.decode('utf-16'))
    except Exception as e:
        print("UTF-16 decode failed:", e)
