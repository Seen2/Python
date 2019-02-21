try:
    f = open('test.txt', 'r')
    # a=append
    # w=write
except Exception as e:
    print(e)

else:
    print(f.name)
    f.close()
