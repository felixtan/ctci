#!/usr/bin/python3

import sys
from timeit import default_timer as timer

# O(n) time, O(n) space
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

    memo = [0, 1]

    for i in range(2, n):
        memo.append(memo[i-1] + memo[i-2])

    return memo[n-1] + memo[n-2]

if __name__ == "__main__":
    start = timer()
    print(fibonacci(sys.argv[1]))
    elapsed = timer() - start
    print(f'{elapsed * 1000} ms')