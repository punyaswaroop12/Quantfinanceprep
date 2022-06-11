# Single Number
# https://leetcode.com/problems/single-number/
#####################################################################################################################################


class Solution:
    def singleNumber(self, nums) -> int:
        # initialize the res to 0
        res = 0

        # iterate through the nums array and do a XOR of each elements with the res value
        for i in nums:
            res = res ^ i

        # return the res value
        return res


# Single Number 2
# https://leetcode.com/problems/single-number-ii/
#####################################################################################################################################


class Solution:
    def singleNumber(self, nums) -> int:
        p1 = 0
        p2 = 0
        for i in nums:
            # first appearance:
            # add i to p1
            # don't add to p2 because of presence in p1

            # second appearance:
            # remove num from p1
            # add num to p2

            # third appearance:
            # don't add to p1 because of presence in p2
            # remove num from p2
            p1 = ~p2 & (p1 ^ i)
            p2 = ~p1 & (p2 ^ i)
        return p1


# Majority Element
# https://leetcode.com/problems/majority-element/
# https://www.youtube.com/watch?v=n5QY3x_GNDg
#####################################################################################################################################

# Solution 1:
# Boyer- Moore's voting algo
class Solution:
    def majorityElement(self, nums) -> int:
        # Track the majority element
        me = nums[0]

        # track the count
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == me:
                count += 1
            else:
                count -= 1
            if count == 0:
                me = nums[i]
                count = 1
        # verifying if the majority element we got repeats more than n/2 times
        verify_count = 0
        for j in nums:
            if j == me:
                verify_count += 1
        if verify_count > (len(nums) // 2):
            return me
        else:
            return -1


# Solution 2:
# Bit Manipulation
# More explanation: https://www.geeksforgeeks.org/find-the-majority-element-set-3-bit-magic/
class Solution:
    def majorityElement(self, nums) -> int:
        # Number of bits in the integer
        length = 32
        n = len(nums)

        # Variable to calculate majority element
        number = 0

        # Loop to iterate through
        # all the bits of number
        for i in range(length):
            count = 0

            # Loop to iterate through all elements
            # in array to count the total set bit
            # at position i from right
            for j in range(n):
                if nums[j] & (1 << i):
                    count += 1

            # If the total set bits exceeds n/2,
            # this bit should be present in
            # majority Element.
            if count > (n // 2):
                number += 1 << i

        count = 0

        # iterate through array get
        # the count of candidate majority element
        for i in range(n):
            if nums[i] == number:
                count += 1

        # Verify if the count exceeds n/2
        if count > (n // 2):
            return number
        else:
            return -1


# Bitwise and of numbers range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/
#####################################################################################################################################

# Solution 1 - TLE ( O(32*range))
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        length = 32
        n = right - left + 1
        res = 0
        for i in range(length):
            count = 0
            for j in range(left, right + 1):
                if j & (1 << i):
                    count += 1
            if count == n:
                res = res + (1 << i)
        return res


# Solution 2 - O(1), O(1) - Bit shift
# Explanation
# First of all, one of the most intuitive solutions that one might come up with might be to iterate all the numbers one by one in the range and do the the bit AND operation to obtain the result.

# This could work for test cases with a small range. Unfortunately it would exceed the time limit set by the online judge for test cases with a relative large range. In this article, we would illustrate some other solutions that do not require the iteration of all numbers.

# First of all, let us look into the characteristic of the AND operation.

# For a series of bits, e.g. [1, 1, 0, 1, 1], as long as there is one bit of zero value, then the result of AND operation on this series of bits would be zero.

# Back to our problem, first we could represent each number in the range in its binary form which we could view as a string of binary numbers (e.g. 9 = 00001001). We then align the numbers according to the position of binary string.


# In the above example, one might notice that after the AND operation on all the numbers, the remaining part of bit strings is the common prefix of all these bit strings.

# The final result asked by the problem consists of this common prefix of bit string as its left part, with the rest of bits as zeros.

# More specifically, the common prefix of all these bit string is also the common prefix between the starting and ending numbers of the specified range (i.e. 9 and 12 respectively in the above example).

# As a result, we then can reformulate the problem as "given two integer numbers, we are asked to find the common prefix of their binary strings."
# Given the above intuition about the problem, our task is to calculate the common prefix for the bit strings of the two given numbers. One of the solutions would be to resort to the bit shift operation.

# The idea is that we shift both numbers to the right, until the numbers become equal, i.e. the numbers are reduced into their common prefix. Then we append zeros to the common prefix in order to obtain the desired result, by shifting the common prefix to the left.
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            count += 1
        return left << count


# Solution 3 - O(1), O(1) Brian Kernighan's algo
# Approach 2: Brian Kernighan's Algorithm
# Intuition

# Speaking of bit shifting, there is another related algorithm called Brian Kernighan's algorithm which is applied to turn off the rightmost bit of one in a number.

# The secret sauce of the Brian Kernighan's algorithm can be summarized as follows:

# When we do AND bit operation between number and number-1, the rightmost bit of one in the original number would be turned off (from one to zero).
# Based on the above trick, we could apply it to figure out the common prefix of two bit strings.

# The idea is that for a given range [m, n][m,n] (i.e. m < nm<n), we could iteratively apply the trick on the number nn to turn off its rightmost bit of one until it becomes less or equal than the beginning of the range (mm), which we denote as n'n
# ′
#  . Finally, we do AND operation between n
# ′
#   and m to obtain the final result.

# By applying the Brian Kernighan's algorithm, we basically turn off the bits that lies on the right side of the common prefix, from the ending number nn. With the rest of bits reset, we then can easily obtain the desired result.

# In the example (m=9, n=12) shown in the above figure, the common prefix would be 00001. After applying the Brian Kernighan's algorithm on the number n, its trailing 3 bits would all become zeros. Finally, we apply the AND operation between the reduced n and the m to obtain the common prefix.
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1)
        return left & right


# Counting Bits
# https://leetcode.com/problems/counting-bits/
#####################################################################################################################################

# Brute force - create function to calculate the set bits and append it to a resultant array (O(Nlog(intmax))
class Solution:
    def countBits(self, n: int):
        res = []
        for i in range(n + 1):
            res.append(self.countsetbits(i))
        return res

    def countsetbits(self, x):
        if x & 1 == 1:
            count = 1
        else:
            count = 0
        while x > 0:
            if (x >> 1 & 1) == 1:
                count += 1
            x = x >> 1
        return count


# Another solution - O(N)
# Using the bits from the previous integers to calculate the set bits in current integer
# if integer is even: then that integer has same bits as integer//2
# if it is odd, then that integer has 1+ bits in the integer//2
class Solution:
    def countBits(self, n: int):
        res = [0] * (n + 1)
        for i in range(n + 1):
            if i == 0:
                res[i] = 0
            elif i == 1:
                res[i] = 1
            elif i & 1 == 0:
                res[i] = res[i // 2]
            elif i & 1 != 0:
                res[i] = res[i // 2] + 1
        return res


# Hamming distance
# https://leetcode.com/problems/hamming-distance/
#####################################################################################################################################
# O(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        for i in range(32):
            # ith bit
            xth_bit = (x >> i) & 1
            yth_bit = (y >> i) & 1
            if xth_bit != yth_bit:
                count += 1
        return count


# 0(1), worst - 0(32)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        return self.countsetbits(res)

    def countsetbits(self, x):
        if x & 1 == 1:
            count = 1
        else:
            count = 0
        while x > 0:
            if (x >> 1 & 1) == 1:
                count += 1
            x = x >> 1
        return count


# Decode XORed permutation
# https://leetcode.com/problems/decode-xored-permutation/
#####################################################################################################################################
# example: encoded=[6,5,4,6], answer =[2,4,1,5,3]
# firstly we will have the decoded array as a permutation of [1,2,3,4,5](length =len(encoded)+1)
# we need to find the first element of the decoded array so that we can complete the array.
# to find the first element we can just xor of all the elements in the encoded and that would be equal to the xor of all the elements in the
# decoded array. if i xor of all the elements in the decoded array and xor the odd indexed elements in the encided array would
# give the first element as total(1^2^3^4^5)^firstIndex(2^3)^thirdindex(4^5)
# inverse of xor is the xor
class Solution:
    def decode(self, encoded):
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total = total ^ i
        for i in range(1, n, 2):
            total = total ^ encoded[i]
        decoded = [total]
        for i in encoded:
            decoded.append(decoded[-1] ^ i)
        return decoded

