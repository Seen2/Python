try:
    # it will automatically closes file after ending of this block
    with open('test.txt', 'r') as f:
        fContents = f.read(10)

        while len(fContents) > 0:
            # print(fContents, end="*")
            # tell position in file

            print(f.tell())
            print(fContents, end="*")
            fContents = f.read(10)
    print()

except Exception as e:
    print(e)

else:
    with open("test.txt", 'r') as f:
        # set position to 0th charector of file
        f.seek(0)
        print(f.read())
