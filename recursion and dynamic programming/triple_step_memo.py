import sys
from timeit import default_timer as timer

# O(n) time and space complexity
def step(n, memo):
    # base case: complete path found
    if n == 0:
        return 1
    # base case: invalid path 
    elif n < 0:
        return 0
    # combine subproblems
    # compute only if result hasn't been saved
    elif len(memo) - 1 < n:
        memo.append(step(n-1, memo) + step(n-2, memo) + step(n-3, memo))

    # return saved result
    return memo[n]

if __name__ == "__main__":
    errmsg = 'please provide a non-negative integer'

    try:
        n = int(sys.argv[1])

        if (n < 0):
            raise TypeError(errmsg)

        start = timer()
        print(step(n, [0, 1]))
        elapsed = timer() - start
        print(f'{elapsed * 1000} ms')
    except:
        raise TypeError(errmsg)