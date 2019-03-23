def main():
    l = [1, 5, 3, 4, 7]

    print(linearSearch(l, 6))


def linearSearch(l, n, i=0):
    if i == len(l):
        return False
    elif l[i] == n:
        return True
    else:
        return linearSearch(l, n, i + 1)


if __name__ == "__main__":
    main()
