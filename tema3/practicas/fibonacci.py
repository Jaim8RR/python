def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def serie_fibonacci(n):
    if n == 0:
        print(f" {n} ")
        return 0
    elif n == 1:
        print(f" {n} ")
        return 1
    else:
        print(f" {n} ")
        return fibonacci(n - 1) + fibonacci(n - 2)
    

