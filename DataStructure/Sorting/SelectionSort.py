def main():
    l = [1, 2.3, 1]
    print(selectionSort(l))


def selectionSort(l):
    n = len(l)
    for i in range(n):
        m = min(l[i:])
        j = l[i:].index(m)
        l[i], l[j+i] = l[j+i], l[i]

    return l


if __name__ == "__main__":
    main()

# def selectionSort1(l):
#     n = len(l)
#     r = []
#     for _ in range(n):
#         m = min(l)
#         r.append(m)
#         l.remove(m)

#     return r
