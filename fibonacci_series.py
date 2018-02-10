def recursive_fib(n):
    if(n == 2):
        return 1
    if(n == 1):
        return 0
    return(recursive_fib(n-1) + recursive_fib(n-2))

def iterative_fib(n):
    if(n == 1):
        return 0
    if(n == 2):
        return 1

    fib_1 = 0
    fib_2 = 1
    for i in range(0, n-2):
        sum = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = sum

    return(sum)

print("Iterative fib: " + str(iterative_fib(7)))
print("Recursive fib: " + str(recursive_fib(13)))