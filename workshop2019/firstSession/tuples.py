# tuples are immutable
# t.count(  t.index(
t = ("rahul", 100, 60.4, 'shintu', "rahul", 100, 60.4, 'shintu')
# slicing
print(t[0])
print(t[1::2])
print(t[-1])
# t[11] = 'new' # gives error # tuples are immutable

for e in t:
    print(e)

print(t.index("rahul"))
