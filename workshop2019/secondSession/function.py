# without parameter
def func():
    a, b = 10, 20
    c = a+b
    print(c)


# func()


def funcP(a, b):
    '''
    takes two integer and print its sum
    '''
    c = a+b
    print(c)


# default argument comes last in parameter sequence.
def funcDefaultP(a, b=1, c=1):
    '''
    takes three integer and print its sum or print default sum
    '''
    c = a+b
    print(c)


# funcP(10, 30)
funcDefaultP(10, 30)
