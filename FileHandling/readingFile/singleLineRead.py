try:
    # it will automatically closes file after ending of this block
    with open('test.txt', 'r') as f:
        print(f.name)
        print(f.mode)
        print("\v")
        fContents = f.readline()
        print(fContents, end="")
    print(f"file is closed:{f.closed}")
except Exception as e:
    print(e)
