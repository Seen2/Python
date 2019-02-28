def main():
    a=2 # 2=ob00000010
    b=3 # 3=ob00000011
    
#     logical operations
    print(f"{a} AND {b}={a&b}")
    print(f"{a} OR {b}={a|b}")
    
#     takes binary of a and flips its bits and add 1 to it.
#     whilch is 2 's complement of a
    print(f"2's complement of {a} ={~a}")
    
#     exclusive OR (X-OR)
    print(f"{a} X-OR {b}={a^b}")
    
   


if __name__=="__main__":
    main()
