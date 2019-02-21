from signError import SignError

try:
    s = int(input("Enter Integer:"))
    if s < 0:
        raise SignError
except ValueError as e:
    print(e)
    print("You haven't entered Integer. Please, ", end="")
    s = int(input("Enter Integer:"))
except SignError as e:
    print(e)
    print("SignError, You haven't entered Integer. Please, ", end="")
    s = int(input("Enter Integer:"))

except Exception:
    print("Something went wrong")
else:
    print("Enter s= 1,2,3....")
    s = 5
finally:
    for i in range(1, 11):
        print(f"{s} * {i} = {s*i}")
    if s % 2 == 0 and s >= 0:
        print(f"{s} is even")
    else:
        print(f"{s} is odd")
