# Binary search
# https://leetcode.com/problems/binary-search/submissions/
#############################################################################

# Solution 1: Recursive (O(log(n)))
class Solution:
    def search(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1
        return self.binarysearch(l, r, target, nums)

    def binarysearch(self, low, high, tar, arr):
        mid = (low + high) // 2
        if high >= low:
            if arr[mid] == tar:
                return mid
            elif arr[mid] > tar:
                return self.binarysearch(low, mid - 1, tar, arr)
            elif arr[mid] < tar:
                return self.binarysearch(mid + 1, high, tar, arr)
        else:
            return -1


# Solution 2: Iterative O(log(n))
class Solution:
    def search(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return -1


# selection sort  - 0(n**2)
#############################################################################

# SOlution 1 using for loops
def selection_sort(arr):
    for i in range(len(arr)):
        tempindex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[tempindex]:
                tempindex = j
        arr[i], arr[tempindex] = arr[tempindex], arr[i]


# Solution 2 using for and while loops
def selection_sort(arr):
    for i in range(len(arr)):
        minindex = i
        res = i
        while res < len(arr):
            if arr[res] < arr[minindex]:
                minindex = res
            res += 1
        arr[i], arr[minindex] = arr[minindex], arr[i]


# Bubble sort- 0(n**2)
#############################################################################


def bubblesort(arr):
    length = len(arr)
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Insertion sort
#############################################################################


def insertion_sort(arr):
    for i in range(1, len(arr)):
        counter = i
        while counter > 0:
            if arr[counter] < arr[counter - 1]:
                arr[counter], arr[counter - 1] = arr[counter - 1], arr[counter]
            counter -= 1


# Counting sort
#############################################################################
def counting_sort(arr):
    count=[0]*10
    for i in arr:
        count[i]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    res=[0]*len(arr)
    for i in range(len(arr)-1, -1,-1):
        res[count[arr[i]]-1]=arr[i]
        count[arr[i]] =count[arr[i]]-1
    return res     

# Merge sort - 0(nlogn) - Divide and Conquer
#############################################################################
def mergeSort(arr):
    if len(arr) > 1:
        mid = int(len(arr) / 2)
        left = arr[:mid]
        right = arr[mid:]
        print(left)
        print(right)
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Quick sort - 0(nlogn)
#############################################################################

# Function to find the partition position
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


# Function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


# radix sort
#############################################################################
def countingSort(arr, exp1):
    n = len(arr)
    # The output array elements that will have sorted arr
    output = [0] * (n)
    # initialize count array as 0
    count = [0] * (10)
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10


# bucket sort
#############################################################################
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucketSort(x):
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x


# Maximum Gap
#########################################################


####bro code youtubre channel
