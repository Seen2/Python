# list are mutable
# basic inbuilt methods
# l.append(   l.copy(     l.extend(   l.insert(   l.remove(   l.sort(
# l.clear(    l.count(    l.index(    l.pop(      l.reverse(
l = ["rahul", 100, 60.4, 'shintu', "rahul", 100, 60.4, 'shintu']
# slicing
print(l[0])
print(l[1::2])
print(l[-1])
l.append('new')   # NO error # list are mutable

for e in l:
    print(e)

print(l.index("rahul"))
