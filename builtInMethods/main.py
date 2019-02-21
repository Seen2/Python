def main():
    s = "hello, world!"
    print(any(s))  # check wheather s is iterable

    i = -1234
    print(abs(i))  # return absolute value of i.

    # l = [s, i, 78]
    try:
        print(all(123))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
