def main():
    l = [1, 2, 3, 4]

    print(linearSearch(l, 2))


def linearSearch(l, n):
    t = len(l)
    for i in range(t):
        if l[i] == n:
            return True

    return False


if __name__ == "__main__":
    main()
