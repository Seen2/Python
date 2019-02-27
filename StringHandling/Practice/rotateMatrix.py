def isStringRotation(s, t):
    j = m = t.index(s[0])
    n = len(s)
    if n != len(t):
        return False
    else:
        for i in range(n):

            print(s[i], t[j])

            if s[i] != t[j]:
                break
            if j == n-1:
                j = -1
            if j == m-1:
                return True

            j += 1

    return False


print(isStringRotation("waterbottle", "erbottlewat")) 
