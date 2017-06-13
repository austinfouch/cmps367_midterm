
def fib(x):
    global times
    global table
    times += 1
    if x <= 1:
        return 1
    else:
        if table.get(x):
            return table[x]
        else:
            tmp = fib(x-1) + fib(x-2)
            table[x] = tmp
            return tmp

global times
global table
times = 0
n = 30
table = dict()

print("Fib(" + str(n) + ") = " + str(fib(n)))
print("this took " + str(times) + " calls")
