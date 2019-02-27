from time import sleep


l = []


def permutation(s):
    while True:
        if s == sorted(s)[len(s):0:-1]:
            break


def palindrome(s):
    s = sorted(s.replace(" ", "").lower())
    print(s)
    permutation(s)


print(palindrome('Tact Coa'))


# from time import sleep


# def palindromePermutation(s):
#     t = s.replace(" ", "").lower()
#     l = []
#     for i in range(len(t)):
#         for j in range(len(t)-1, 0, -1):
#             print(i, j)
#             # p = s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
#             print(t)
#             p = interchange(t, i, j)
#             sleep(2)
#             print(p)

#             if p == p[-1:-len(p)-1:-1]:
#                 l.append(p)
#             del p
#     return l


# def interchange(s, i, j):
#     r = ''
#     for k in range(len(s)):
#         if k == i:
#             r += s[j]
#         elif k == j:
#             r += s[i]
#         else:
#             r += s[k]
#     return r


# print(palindromePermutation('Tact Coa'))
# # print(interchange("shintii", 5, 0))
