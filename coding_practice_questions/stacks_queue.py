# Implement Stack using Queues
#########################################################

# Implement Queue using Stacks
#########################################################

# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
#########################################################
# USe stack: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")": "(", "}": "{", "]": "["}
        values = hashmap.values()
        for i in range(len(s)):
            if s[i] in values:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == hashmap[s[i]]:
                    stack.pop()
                elif stack[-1] != hashmap[s[i]]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


# Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/
#########################################################
# Solution 1: Brute force: O(n*m*n)


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dude = j + 1
                    temp = j + 1
                    count = 0
                    while dude < len(nums2):
                        if nums2[dude] > nums1[i]:
                            res.append(nums2[dude])
                            break
                        else:
                            count += 1
                        dude += 1
                    if count == len(nums2) - temp:
                        res.append(-1)
        return res


# SOlution 2: using hashmap O(m*n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = dict()
        res = []
        for index, value in enumerate(nums2):
            hashmap[value] = index
        for i in range(len(nums1)):
            from_index = hashmap[nums1[i]]
            count = 0
            for j in range(from_index + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break
                count += 1
            if count == len(nums2) - from_index - 1:
                res.append(-1)
        return res


# Solution 3: using stack and hashmap
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = dict()
        stack = []
        res = []
        for index, value in enumerate(nums2):
            while len(stack) != 0 and value > stack[-1]:
                hashmap[stack.pop()] = value
            stack.append(value)
        while len(stack) != 0:
            hashmap[stack.pop()] = -1
        for i in nums1:
            res.append(hashmap[i])
        return res


# Design stack which supports getmin in O(1) time and space (Read editorial)
#########################################################

# Largest Rectangle in Histogram
#########################################################

# LRU Cache
#########################################################

# Rotting Oranges
#########################################################

# Reverse a stack without using extra space
#########################################################

# Basic Calculator
#########################################################

# Basic Calculator II
#########################################################

# Car Fleet
#########################################################

# Online Stock Span
#########################################################
