try:
    # it will automatically closes file after ending of this block
    with open('test.txt', 'r') as f:
        print(f.name)
        print(f.mode)
        print("\v")
        sizeToRead = 100
        fContents = f.read(sizeToRead)  # read 100 char from a file
        # fContents = f.readlines() # will give a list as element each line of file ending with \n

        print(fContents)
        # fContents = f.read(100)  # read 100 char from a file
        # # fContents = f.readlines() # will give a list as element each line of file ending with \n
        # takes where it lefts off.
        # print(fContents)
        # fContents = f.read(100)  # read 100 char from a file
        # # fContents = f.readlines() # will give a list as element each line of file ending with \n

        # print(fContents)
    print(f"file is closed:{f.closed}")
except Exception as e:
    print(e)
