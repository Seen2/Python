def main():
    l = [1, 3, 4]

    print(binarySearch(l, 2))


def binarySearch(l, n):
    e = len(l)
    i = 0
    m = (i+e)//2
    while i < e:
        if l[m] == n:
            return True
        elif l[m] > n:
            e = m-1
        else:
            i = m+1
        m = (i+e)//2

    return False


if __name__ == "__main__":
    main()
