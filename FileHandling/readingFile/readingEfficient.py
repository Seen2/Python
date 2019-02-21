try:
    # it will automatically closes file after ending of this block
    with open('test.txt', 'r') as f:
        # read ine line at a time
        for line in f:
            print(line, end="")
    print()
except Exception as e:
    print(e)
