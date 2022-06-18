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
#####################################################################################################################################

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


# catalan number O(2**n)
# Nth catalan number is C0Cn-1 +C1Cn-2+.....+ CiCn-i-1+ .....+Cn-1C0
#####################################################################################################################################


def nthcatalannumber(N):
    if N <= 1:
        return 1
    res = 0
    for i in range(N):
        res = res + nthcatalannumber(i) * nthcatalannumber(N - i - 1)
    return res


# Binomial coefficient: O(n)
# more information in the number of Unique BSTs solution below


# Number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
#####################################################################################################################################
# Apply catalan numbers code above Cn is the number of expression containing n pairs of parantheses


# Number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.
# 𝐶𝑛 is the count of full binary trees with 𝑛+1 leaves

# Number of ways to connect the points on a circle disjoint chords
# 2n points in a circle = nth catalan number ways


# Number of different ways N+1 factors can be completely paranthesized
# https://math.stackexchange.com/questions/3491003/number-of-ways-to-insert-parentheses-between-elements
# https://stackoverflow.com/questions/43071803/number-of-different-ways-n-1-factors-can-be-completely-parenthesized


# Rosen defines 𝐶𝑛 to be the number of ways of inserting parentheses in the product 𝑥0⋅𝑥1⋅𝑥2⋅⋯⋅𝑥𝑛, which has 𝑛+1 factors.
#  He then observes that one multiplication symbol remains outside all parentheses and supposes that it lies between 𝑥𝑘 and 𝑥𝑘+1.
# If this occurs, then the number of ways to parenthesize the product 𝑥0⋅𝑥1⋅𝑥2⋅⋯⋅𝑥𝑛 is found by multiplying the number of ways of
#  parenthesizing the 𝑘+1 factors in the product 𝑥0⋅𝑥1⋅𝑥2⋅⋯⋅𝑥𝑘, which is 𝐶𝑘, by the number of ways of parenthesizing the 𝑛−𝑘 factors in the product 𝑥𝑘+1⋅𝑥𝑘+2⋅𝑥𝑘+3⋅⋯⋅𝑥𝑛, which is 𝐶𝑛−𝑘−1.
#  Since 𝑘 can range from 0 to 𝑛−1, we obtain
# 𝐶𝑛 = nth catalan number


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


# Solution 2: O(n) using binomial coeffcient
# C(n) = (2n C n)/(n+1) = (2n!)/n!(n+1)!
# calculate factorial in O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        factorial_2n = self.factorial(n * 2)
        factorial_n = self.factorial(n)
        factorial_n_plus_1 = factorial_n * (n + 1)
        return int((factorial_2n) / (factorial_n * factorial_n_plus_1))

    def factorial(self, N):
        res = 1
        for i in range(1, N + 1):
            res = res * i
        return res


# number of all possible binary trees with given Inorder Traversal of an array
# https://www.geeksforgeeks.org/find-all-possible-trees-with-given-inorder-traversal/
# the solution would be the nth catalan number = Cn for the array of length n


# The number of paths with 2n steps on a rectangular grid from bottom left, i.e., (n-1, 0) to top right (0, n-1) that do not cross above the main diagonal.
# We know that there are (2𝑛 C n) ways of going (𝑛,𝑛) from (0,0) when there is no restriction. So the answer should be (2𝑛 C n)−𝐵 where 𝐵 is the number of "bad paths", that is, number of paths that go above the diagonal line.
# Now, in order to calculate 𝐵, we should notice something: When we go above the diagonal line, we will pass through another diagonal line, which is shown as 𝑟𝑒𝑑 in the figure.
#  And for each bad path (passes through the red line), let us create a new path which has the same moves until we go above the diagonal line (or pass through the red line), 
# and then does the symmetric moves to our original path (original path is shown as 𝑏𝑙𝑢𝑒, symmetric moves are shown in 𝑔𝑟𝑒𝑒𝑛). Therefore, number of bad paths become the number
#  of paths from (0,0) to (𝑛−1,𝑛+1), which means 𝐵=(2𝑛 C (𝑛+1)). So the answer becomes
# (2𝑛 C 𝑛)−(2𝑛 C (𝑛+1)) which is nothing but (2n C n)/(n+1) - nth catalan number