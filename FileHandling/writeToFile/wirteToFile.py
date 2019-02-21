try:
    # it will automatically closes file after ending of this block
    # w mode overrides the file if exists, or create new filw if doesn't exists.
    with open('testWrite.txt', 'w') as f:
        f.write("Test \n")
        # picks where it lefts off we can use f.seak(0)
        # f.write("Test")

except Exception as e:
    print(e)
