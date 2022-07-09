# Kth Largest Element in an Array
#########################################################
# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Solution1 : Using Min heap O(N+(N-k+1)*Log(N-k+1))
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)


# Solution 2: Using Maxheap O(N+klogN)
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)


# Solution 3: using quick select


# Sort Colors
#########################################################
# https://leetcode.com/problems/sort-colors/ O(N)
# Solution 1 = O(N), O(N) extra space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        self.counting_sort(nums)

    def counting_sort(self, arr):
        count = [0] * 10
        res = [0] * len(arr)
        for i in range(len(arr)):
            count[arr[i]] += 1
        for j in range(1, len(count)):
            count[j] = count[j] + count[j - 1]
        counter = len(arr) - 1
        while counter >= 0:
            res[count[arr[counter]] - 1] = arr[counter]
            count[arr[counter]] -= 1
            counter -= 1
        for i in range(len(res)):
            arr[i] = res[i]


# Solution 2 = O(N), no extra space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        m = 0
        h = len(nums) - 1
        while m <= h:
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                m += 1
                l += 1
            elif nums[m] == 1:
                m += 1
            elif nums[m] == 2:
                nums[m], nums[h] = nums[h], nums[m]
                h = h - 1
        return nums


# Largest sum contiguous subarray
#########################################################
# https://leetcode.com/problems/maximum-subarray/submissions/
# Kadane's algo - O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_till_now = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            sum_till_now = max(sum_till_now + nums[i], nums[i])
            max_sum = max(max_sum, sum_till_now)
        return max_sum


# Merge 2 sorted arrays without using extra space
#########################################################
# https://leetcode.com/problems/merge-sorted-array/
# Solution 1: O(m+n), space=O(m+n)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr = [0] * (m + n)
        l = 0
        r = 0
        k = 0
        while l < m and r < n:
            if nums1[l] <= nums2[r]:
                arr[k] = nums1[l]
                l += 1
            else:
                arr[k] = nums2[r]
                r += 1
            k += 1
        while l < m:
            arr[k] = nums1[l]
            l += 1
            k += 1
        while r < n:
            arr[k] = nums2[r]
            r += 1
            k += 1
        for i in range(len(nums1)):
            nums1[i] = arr[i]


# Merge Intervals O(NlogN)
#########################################################
# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                if merged[-1][1] >= interval[1]:
                    continue
                else:
                    merged[-1][1] = interval[1]
        return merged


# Next Permutation
#########################################################
# https://leetcode.com/problems/next-permutation/
# Solution 1: O(N) time , O(1) space
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        peakindex = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[i - 1]:
                peakindex = i - 1
                break
        # this is for the descending ordered array, returing the reverse of it as per the question
        if peakindex == -1:
            self.reverse(nums, 0, len(nums) - 1)
        else:
            mindiff = math.inf
            swapindex = peakindex
            value_to_compare = nums[peakindex]
            for j in range(peakindex + 1, len(nums)):
                diff = nums[j] - value_to_compare
                if (diff <= mindiff) and diff > 0:
                    mindiff = diff
                    swapindex = j
            nums[peakindex], nums[swapindex] = nums[swapindex], nums[peakindex]
            print(nums)
            self.reverse(nums, peakindex + 1, len(nums) - 1)

    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


# Counting inversion
#########################################################


# Best Time to Buy and Sell Stock
#########################################################
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
# SOlution 1: O(N)
class Solution:
    def maxProfit(self, prices) -> int:
        maxprofit = 0
        minprice = prices[0]
        for i in range(1, len(prices)):
            curr_profit = prices[i] - minprice
            if prices[i] < minprice:
                minprice = prices[i]
            if curr_profit > maxprofit:
                maxprofit = curr_profit
        return maxprofit


# Given array of size N and number K, find all elements that appear more than N/K times
#########################################################

# Trapping Rain Water
#########################################################
# https://leetcode.com/problems/trapping-rain-water/
# Solution 1: O(N**2) time - time limit exceeded
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            left_max = max(height[:i])
            right_max = max(height[i + 1 :])
            final_result = min(left_max, right_max) - height[i]
            result = final_result if final_result > 0 else 0
            res = res + (result)
        return res


# Solution 2: O(N) time O(N) space - Dynamic programming
class Solution:
    def trap(self, height: List[int]) -> int:
        left_arr = [height[0]]
        right_arr = [height[-1]]
        for i in range(1, len(height)):
            left_arr.append(max(height[i], left_arr[-1]))
        for j in range(len(height) - 2, -1, -1):
            right_arr.append(max(height[j], right_arr[-1]))
        right_arr = right_arr[::-1]
        res = 0
        for i in range(len(height)):
            res += min(left_arr[i], right_arr[i]) - height[i]
        return res


# Solution 4: O(N) time and O(1) space


# Minimum Size Subarray Sum
#########################################################

# Median of Two Sorted Arrays
#########################################################

# Two Sum
#########################################################
# https://leetcode.com/problems/two-sum/ = O(N) time, O(N) space
class Solution:
    def twoSum(self, nums, target):
        hashmap = dict()
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            else:
                hashmap[nums[i]] = i


# 3Sum
#########################################################

# 4Sum
#########################################################

# 4Sum II
#########################################################

# Range Sum Query - Immutable
#########################################################

# Sort a K-sorted array
#########################################################

# Shortest Subarray with Sum at Least K
#########################################################

# Search in Rotated Sorted Array
#########################################################

# Find Median from Data Stream
#########################################################

# Closest Subsequence Sum   (Leetcode 1755)
#########################################################

# Range Addition
#########################################################

# Capacity To Ship Packages Within D Days
#########################################################

# Sum of Subarray Minimums
#########################################################

# Count Unique Characters of All Substrings of a Given String
#########################################################
