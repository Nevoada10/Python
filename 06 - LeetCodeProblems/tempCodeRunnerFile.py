class Solution(object):
    """
    A class used to remove all occurrences of a specified value from a list of integers in-place.

    Methods
    -------
    removeElement(nums: List[int], val: int) -> int
        Removes all occurrences of 'val' from 'nums' and returns the number of elements left.
    """

    def removeElement(self, nums: List[int], val: int) -> int:

        counter = 0

        for element in nums:
            if element == val:
                nums.pop(element)
                counter +=1

        return len(nums) - counter


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement([3,2,2,3], 3))
