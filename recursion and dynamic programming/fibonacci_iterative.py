#!/usr/bin/python3

import sys
from timeit import default_timer as timer

# O(n) time, O(1) space
def fibonacci(n):
    errmsg = "please enter a non-negative integer"

    try:
        n = int(n)
    except:
        raise TypeError(errmsg)

    if (n < 0):
        raise TypeError(errmsg)

    # base cases
    if (n == 0 or n == 1):
        return n

    a = 0
    b = 1

    for i in range(2, n):
        c = a + b
        a = b
        b = c

    return a + b

if __name__ == "__main__":
    start = timer()
    print(fibonacci(sys.argv[1]))
    elapsed = timer() - start
    print(f'{elapsed * 1000} ms')