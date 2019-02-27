def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)

def facto(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return fact


print(facto(5))