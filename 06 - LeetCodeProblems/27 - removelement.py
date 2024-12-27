# 13 - Remove Element (Solution)
# Author: Uriel Neves Silva
# Top interview 150 https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
# Github: https://github.com/nevoada10

from typing import List


class Solution(object):
    """
    A class used to remove all occurrences of a specified value from a list of integers in-place.

    Methods
    -------
    removeElement(nums: list[int], val: int) -> int
        Removes all occurrences of 'val' from 'nums' and returns the number of elements left.
    """

    def removeElement(self, nums, val):
        print(f"Initial nums: {nums}, val to remove: {val}")

        counter = 0
        for i in range(len(nums)):
            print(f"Checking element: {nums[i]} at index: {i}")
            
            if nums[i] == val:
                print(f"Element {nums[i]} is equal to val, removing...")
                nums[i] = None  # Mark for removal
                counter += 1
        
        # Remove marked elements
        nums[:] = [num for num in nums if num is not None]
        print(f"Modified nums: {nums}")

        k = len(nums)
        print(f"Number of elements left: {k}")
        return k


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement([3,2,2,3], 3))



# Time complexity: 
# Space complexity:

"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""
