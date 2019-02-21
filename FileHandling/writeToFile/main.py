try:
    # it will automatically closes file after ending of this block
    # w mode overrides the file if exists, or create new filw if doesn't exists.
    # rb, wb, ab are binary mode for reading, writing and appending respectively.
    with open('testWrite.txt', 'w') as f:
        f.writel("Test \n")
        # simillarly as resdlines and readline writeline, writelines works
        # picks where it lefts off we can use f.seak(0)
        # f.write("Test")

except Exception as e:
    print(e)
