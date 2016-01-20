def fib(n):
    if int(n) == 0:
        return 0
    elif int(n) == 1:
        return 1
    else:
        return fib(int(n)-1) + fib(int(n)-2)
