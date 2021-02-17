"""
5! = 5*4*3*2*1 *1 = 120
n * factorial(n-1)
"""


def recursive_factorial(n):  # 3 | 2 | 1 | 0
    if n == 0:
        return 1  # 1
    else:
        return n * recursive_factorial(n - 1)  # 3 * factorial(2) | 2 * factorial(1) | 1 * 1

def memoized_factorial(n):  # 3 | 2 | 1 | 0
    cache = {}
    if n == 0:
        return 1  # 1
    else:
        return n * recursive_factorial(n - 1)  # 3 * factorial(2) | 2 * factorial(1) | 1 * 1


def iterative_factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f



print(iterative_factorial(500))
#print(recursive_factorial(50))
