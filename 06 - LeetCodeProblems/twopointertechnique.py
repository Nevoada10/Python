"""

Original Array:  [3, 2, 2, 3, 4, 5, 3]  (val to remove = 3)
                  ↑
                 slow
                  ↑
                 fast

Steps:
1. If fast pointer finds a non-val element:
   - Copy that element to slow pointer position
   - Move slow pointer forward

Final Result:  [2, 2, 4, 5, _, _, _]
               ↑
              slow (now points to length of new array)

"""

def removeElement(self, nums: List[int], val: int) -> int:
    k = 0  # slow pointer (where to place next valid element)
    
    for i in range(len(nums)):  # fast pointer (scanning the array)
        if nums[i] != val:
            nums[k] = nums[i]  # move valid element to slow pointer position
            k += 1  # advance slow pointer
    
    return k  # k is now the length of the modified array