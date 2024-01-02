f = -1
s = 1
def fib(n):
    global f,s
    t = f + s
    print(t)

    f = s
    s = t
    if n==0 :
            return
    else:
            fib(n-1)


fib(5)
