from time import sleep


def main():
    s = input("Enter String:")
    print(isUnique(s))


def isUnique(s, c='-0', i=1):

    if c in s[i:]:
        return False
    if i == len(s)-1:
        return True

    else:
        for j in range(i, len(s)-1):
            # print(j)
            # sleep(2)
            return isUnique(s, s[j], j+1)


if __name__ == "__main__":
    main()
