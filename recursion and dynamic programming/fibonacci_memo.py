#!/usr/bin/python3

import sys
from timeit import default_timer as timer

# O(n) time, O(n) space
def fibonacci(n, memo):
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

    if (len(memo) - 1 < n):
        memo.append(fibonacci(n - 1, memo) + fibonacci(n - 2, memo))

    return memo[n]


if __name__ == "__main__":
    start = timer()
    print(fibonacci(sys.argv[1], [0, 1]))
    elapsed = timer() - start
    print(f'{elapsed * 1000} ms')