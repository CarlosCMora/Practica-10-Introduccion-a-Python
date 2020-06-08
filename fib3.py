def fib_bottom_up(n):
    t=[1,1]
    while len(t)<n:
        t.append(t[-1]+t[-2])
        print (t)
    return t[n-1]

fib_bottom_up(10)