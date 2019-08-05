def isPerfectNum(n):
    s = 0
    for i in range(1, 1+n//2):
        if n % i == 0:
            s += i

    if n == s:
        return True
    else:
        return False


print(isPerfectNum(8128))
