def main():
    s = input("Enter String:")
    i = 0
    for c in s:
        i += 1
        if c in s[i:]:
            print(f"{c} occurs so it'sn't unique")
            break


if __name__ == "__main__":
    main()
