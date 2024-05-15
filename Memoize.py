def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        

def trace(f):
    def g(x):
        print(f.__name__, x)
        value = f(x)
        print('return', repr(value))
        return value
    return g
    
fib = trace(fib)
print(fib(3))


def memoize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g
    
    
fib = trace(fib)
fib = memoize(fib)
print(fib(4))
