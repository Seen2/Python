def main():
    l = [1, 2, 4, 6, 8]

    print(binarySearch(l, 8, len(l)-1))


def binarySearch(l, n, e, i=0):
    m = (i+e)//2

    if i > e:
        return False
    if l[m] == n:
        return True

    elif l[m] > n:

        return binarySearch(l, n, m-1, i)
    else:

        return binarySearch(l, n, e, m+1)


if __name__ == "__main__":
    main()
