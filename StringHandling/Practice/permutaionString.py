
def isPermutaion(a, b):
    if len(a) != len(b):
        return False
    else:
        for c in a:
            if c not in b:
                return False

        return True


print(isPermutaion("str", "jrt"))
