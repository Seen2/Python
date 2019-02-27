def main():
    s = input("Enter String:")
    rS = ""
    for i in range(1, len(s)+1):
        rS += s[-i]

    print("reverse string:", rS)
    print("reverse string:", s[(len(s)-1)::-1])


if __name__ == "__main__":
    main()
