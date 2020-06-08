t={0:1,1:1}
def fib_mem(n):
    
    if not n in t:
        t[n] = fib_mem(n-1) + fib_mem(n-2)
    return t[n]

fib_mem(6)
print(t)