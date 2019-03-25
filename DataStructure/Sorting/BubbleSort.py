def main():
    l = [1, 2, 0, 2, 3, 1]
    print(bubbleSort(l))


def bubbleSort(l):
    n = len(l)
    for i in range(n):
        for j in range(n):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]

    return l


if __name__ == "__main__":
    main()
