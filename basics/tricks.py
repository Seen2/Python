#comprehension
#type of syntactic sugar for iterative objects
l=[x**2 for x in range(9)]
print(l)

d={x:x**2 for x in range(9)}
print(d)
di={x:type(d[x]) for x in d}
print(di)

string="abcdefghijkl"
l=[x for x in string]
k=[ord(x) for x in string]
nedict=dict(list(zip(l,k)))
print(nedict)
