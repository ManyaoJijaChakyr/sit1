def fib(n):
    if n == 1:
        print(0)
    if n == 2:
        print(0)
        print(1)
    else:
        a, b = 0, 1
        print(0)
        print(1)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
