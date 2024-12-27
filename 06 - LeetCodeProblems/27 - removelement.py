# 13 - Remove Element (Solution)
# Author: Uriel Neves Silva
# Top interview 150 https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
# Github: https://github.com/nevoada10

from typing import Counter, List


class Solution(object):
    """
    A class used to remove all occurrences of a specified value from a list of integers in-place.

    Methods
    -------
    removeElement(nums: list[int], val: int) -> int
        Removes all occurrences of 'val' from 'nums' and returns the number of elements left.
    """

    def removeElement(self, nums: List[int], val: int) -> int:

        counter: int = 0
        list_length: int = len(nums)
        for i in range(list_length):
            if nums[i] == val:
                nums[i] = None  # Mark for removal
                counter += 1
        
        # Sort the list putting None values at the end
        nums.sort(key=lambda x: x is None)
        k = list_length - counter
        return k

def test_cases():
    solution = Solution()
    
    test_cases = [
        # Input list, value to remove, expected length, expected modified list
        ([3, 2, 2, 3], 3, 2, [2, 2]),           # Basic case with multiple occurrences
        ([1, 2, 3, 4, 5], 6, 5, [1, 2, 3, 4, 5]),  # No occurrences of val
        ([2, 2, 2, 2], 2, 0, []),               # All elements are val
        ([], 1, 0, []),                         # Empty list
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4])  # Mixed elements
    ]
    
    # Run tests
    for nums, val, expected_length, expected_list in test_cases:
        # Create a copy of the original list to preserve input
        nums_copy = nums.copy()
        
        # Call removeElement
        result = solution.removeElement(nums_copy, val)
        
        # Check length
        length_passed = result == expected_length
        
        # Check modified list (first 'result' elements)
        list_passed = nums_copy[:result] == expected_list
        
        print(f"Input: nums = {nums}, val = {val}")
        print(f"Expected Length: {expected_length}, Actual Length: {result}")
        print(f"Expected List: {expected_list}, Actual List: {nums_copy[:result]}")
        print(f"Length Passed: {length_passed}, List Passed: {list_passed}")
        print("---")

# Run the tests
if __name__ == "__main__":
    test_cases()

# Time complexity: O(n)
# - The algorithm iterates through the array nums once, which takes O(n) time.

# Space complexity: O(1)
# - The algorithm uses a constant amount of space, regardless of the size of the input.

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
