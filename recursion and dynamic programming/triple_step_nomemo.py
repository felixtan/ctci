import sys
from timeit import default_timer as timer

def step(n):
    # base case: complete path found
    if n == 0:
        return 1
    # base case: invalid path 
    elif n < 0:
        return 0
    # combine subproblems
    else:
        return step(n-1) + step(n-2) + step(n-3)

if __name__ == "__main__":
    errmsg = 'please provide a non-negative integer'

    try:
        n = int(sys.argv[1])

        if (n < 0):
            raise TypeError(errmsg)

        start = timer()
        print(step(n))
        elapsed = timer() - start
        print(f'{elapsed * 1000} ms')
    except:
        raise TypeError(errmsg)