def URLify(s):
    op = ''
    for c in s:
        if c == " ":
            op += '%20'
        else:
            op += c

    return op

# using built in methods
# def URLify(s="hey there"):
#     return "%20".join(s.split())

print(URLify("Mr John Smith"))
