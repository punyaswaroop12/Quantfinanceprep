# Find all prime nos from 1 to N
#####################################################################################################################################

# Solution 1: Naive O(N**2)
from functools import lru_cache


def allprimes(N):
    res = []
    for i in range(2, N + 1):
        if isprime(i):
            res.append(i)
    return res


def isprime(n):
    isitprime = True
    for i in range(2, n):
        if n % i == 0:
            isitprime = False
    return isitprime


# Solution 2: O(N**(3/2))
# Iterating until the square root of N should suffice
# so time complexiety is N multipled by square root of N
def allprimes(N):
    res = []
    for i in range(2, N + 1):
        if isprime(i):
            res.append(i)
    return res


def isprime(n):
    isitprime = True
    num = 2
    while num * num <= n:
        if n % num == 0:
            isitprime = False
        num += 1
    return isitprime


# Solution 3: Sieve of eratosthenes - O(Nlog(log(N)))
def allprimes(N):
    ans = []
    res = [True for i in range(N + 1)]
    num = 2
    while num * num <= N:
        if res[num]:
            for i in range(num * num, N + 1, num):
                res[i] = False
        num += 1
    for j in range(2, N + 1):
        if res[j]:
            ans.append(j)
    return ans


# Given a number find if it's prime
#####################################################################################################################################
# solution 1: O(sqrt(n))
def isprime(n):
    isprimeind = True
    num = 2
    while num * num <= n:
        if n % num == 0:
            isprimeind = False
        num += 1
    return isprimeind


# Calculate X^Y in log(Y) time
#####################################################################################################################################

# Solution 1: Naive(O(Y))
def pow1(x, y):
    res = 1
    for i in range(y):
        res = res * x
    return res


# Solution 2: Most efficient(O(log(y)))
def pow1(x, y):
    res = 1
    while y > 0:
        if y % 2 != 0:
            res = res * x
        y = y >> 1
        x = x * x
    return res


# Find all prime factors of a number N
#####################################################################################################################################

# Solution 1 (naive) O(Nsqrt(N))
def primefactors(N):
    res = []
    for i in range(2, N):
        if N % i == 0 and isprime(i):
            res.append(i)
    return res


def isprime(n):
    isitprime = True
    num = 2
    while num * num <= n:
        if n % num == 0:
            isitprime = False
        num += 1
    return isitprime


# Solution 2 most efficient (O(sqrt(N))) - think of compression factor here as N decreases through compression
def primefactors(N):
    res = []
    num = 2
    while num * num < N:
        while N % num == 0:
            N = N // num
            res.append(num)
        num += 1
    if N > 1:
        res.append(N)
    return res


# Calculate NCR value for given N and R
# we can use a pascal's triangle to calculate this
from functools import lru_cache


@lru_cache()
def ncr_value(N, R):
    # creating a matrix with 1000*1000 dimensions and filling the pascals traingele values in them and NcR value is nothing but
    # the value of the Nth row and rth column
    matrix = [[0 for x in range(1001)] for j in range(1001)]
    matrix[0][0] = 1
    for i in range(1, N + 1):
        matrix[i][0] = 1
        matrix[i][i] = 1
        for j in range(1, i):
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
    return matrix[N][R]


# catalan number
# Nth catalan number is C0Cn-1 +C1Cn-2+.....+ CiCn-i-1+ .....+Cn-1C0
def nthcatalannumber(N):
    if N <= 1:
        return 1
    res = 0
    for i in range(N):
        res = res + nthcatalannumber(i) * nthcatalannumber(N - i - 1)
    return res


# Number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).


# Number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.


# Number of ways to connect the points on a circle disjoint chords


# Number of different ways N+1 factors can be completely paranthesized
# https://math.stackexchange.com/questions/3491003/number-of-ways-to-insert-parentheses-between-elements
# https://stackoverflow.com/questions/43071803/number-of-different-ways-n-1-factors-can-be-completely-parenthesized


# number of unique BSTs
# https://leetcode.com/problems/unique-binary-search-trees/
# Solution 1: O(2**n)
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        res = 0
        for i in range(n):
            res = res + self.numTrees(i) * self.numTrees(n - i - 1)
        return res


# Solution 2: O(n)


# Find all possible binary trees with given Inorder Traversal
# https://www.geeksforgeeks.org/find-all-possible-trees-with-given-inorder-traversal/


# The number of paths with 2n steps on a rectangular grid from bottom left, i.e., (n-1, 0) to top right (0, n-1) that do not cross above the main diagonal.

