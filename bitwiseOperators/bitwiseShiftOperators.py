def main():
    a=3 # (00000011)
    b=2
#     a<<b=a*(2**b)
#     3<<2=3*(2**2)
#     a=ob00000011
#     a<<b=a<<2=0b00001100=12 #(shif binary of a left by b times)

    print(f"{a}<<{b}={a<<b}")
    a=8 # (ob00001000)
    b=2
#     a>>b=a//(2**b)
#     8>>2=3//(2**2)
#     a=ob00001000
#     a<<b=a<<2=ob00001000=2 #(shif binary of a right by b times)
    print(f"{a}>>{b}={a>>b}")
    
 


if __name__=="__main__":
    main()
