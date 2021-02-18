"""
5

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...

"""

def iterative_fibo(s):  # s = 5, a = 0 , b =1
    a = 0
    b = 1

    for i in range(s):  # 0    |  1   |  2    |  3    | 4
        a,b = b, a+b   # 1, 1  |  2, 3|  3,5  | 5, 8  |8,13
    return a  # 8


def recursive_fibo(s):
    if s==0 or s==1:
        return s
    else:
        return recursive_fibo(s-1) + recursive_fibo(s-2)


cache = dict()

def memoized_fibo(s):  # 5

    if s==0 or s==1:
        return s
    else:
        if s not in cache:
            cache[s] = memoized_fibo(s-1) + memoized_fibo(s-2)  # cache = {5: 5, 4: 4, 3: 3, 2:1, 1:1, 0:0}
        return cache[s]


print(iterative_fibo(1000))
# print(recursive_fibo(10))
print(memoized_fibo(100))