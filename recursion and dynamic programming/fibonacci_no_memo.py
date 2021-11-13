#!/usr/bin/python3

import sys
from timeit import default_timer as timer

# O(2^n) time, O(2^n) space
def fibonacci(n):
    try:
        n = int(n)
    except:
        raise TypeError("please enter a non-negative integer")

    if (n < 0): raise TypeError("please enter a non-negative integer")

    # base cases
    if (n == 0): return 0
    if (n == 1): return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    start = timer()
    print(fibonacci(sys.argv[1]))
    elapsed = timer() - start
    print(f'{elapsed * 1000} ms')