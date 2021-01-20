def birthday(s, d, m):
    c = 0
    op = ''
    for i in range(len(s)):
        l = [s[i]]
        if len(l) == m and sum(l) == d:
            print(l)
            c += 1
            continue
        for j in range(i+1, len(s)):
            l.append(s[j])
            if len(l) == m and sum(l) == d:
                #     print(','.join(list(map(str,l))))
                if str(sorted(l)) not in op:
                    c += 1
                    print(l)
                # op+=','.join(list(map(str,l)))
                op += str(sorted(l))
                l.clear()
                l.append(s[i])
    return c
