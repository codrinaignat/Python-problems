def fibo(n):
    a = 0
    b = 1
    while(a<n):
        print(a, end=' ')
        a, b = b, a+b
    print()

fibo(2000)

def fibo2(n):
    result = []
    a = 0
    b = 1
    #a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b, a+b
    return result

f100 = fibo2(100)
print(f100)

#The return statement returns with a value from a function. return without an expression argument returns None. Falling off the end of a function also returns None.
#The statement result.append(a) calls a method of the list object result. A method is a function that ‘belongs’ to an object and is named obj.methodname, where obj is some object 