def main():
    l = [1, 2, 3, 4, 5, 9, 11]

    print(binarySearch(l, 11))


def binarySearch(l, n):
    '''
    takes a sorted list :l
    a number :n to be search in the list

    return True if n is in the l
    else return False.
    '''

    e = len(l)-1
    i = e//2
    while e-i != 1:
        print(i, e)
        if n == l[i] or n == l[e]:
            return True
        elif n > l[i]:
            i = (i+e)//2
        else:
            e = (i+e)//2
            i = 0

    return False


if __name__ == "__main__":
    main()
