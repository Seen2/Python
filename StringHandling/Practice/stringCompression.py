

# def stringCompress(s):
#     op = ""
#     s = s+' '
#     j = 0
#     for i in range(len(s)-1):
#         if j == 0:
#             op += s[i]
#             j += 1
#         if s[i] == s[i+1]:
#             j += 1
#         if s[i] != s[i+1] and j != 0:
#             op += str(j)
#             j = 0

#     return op


# def stringCompress(s):
#     op = ''
#     tb = []
#     for c in s:
#         if c not in tb:
#             if len(tb) > 0:
#                 op += str(len(tb))
#             tb.clear()
#         if len(tb) == 0:
#             op += c
#         tb.append(c)
#     op += str(len(tb))
#     del tb
#     return op
# print("op=", stringCompress("aabcccccaaa"))
