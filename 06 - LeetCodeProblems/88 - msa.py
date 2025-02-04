# Top interview 150 https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
# 88 - Merge Sorted Array (Solution)
# Author: Uriel Neves Silva
# Github: https://github.com/nevoada10

# The List type hint is used to indicate that the function takes a list as an argument.
# This import is necessary because the List type hint is part of the typing module.

from typing import List # Imports static typing

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted integer arrays in-place.
        Do not return anything, modify nums1 in-place instead.
        Uses static typing for code readability.
        """

        # This code works backwards, because starting from the front, the elements
        #  of nums1 will be overwritten and may not be in the correct order, or
        # cause an out of bounds error.

        p1 = m - 1 # pointer1 points to the last element of nums1
        p2 = n - 1 # pointer2 points to the last element of nums2
        p = m + n - 1 # pointer points to the last element of nums1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]: 
                nums1[p] = nums1[p1]  
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)

# Time complexity: O(m + n) 
# - Uses a single pass through the arrays, each element is processed once.

# Space complexity: O(1) 
# - No additional space is used, the input arrays are modified in-place.

"""
Problem:

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


"""
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""