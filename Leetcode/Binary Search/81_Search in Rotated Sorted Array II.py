# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

""" Hard one for me, the binary search part is easy, but the first 
and second sorted array part is messy. """

""" It is a modified binary search, you have to shrink the search range
until both mid and target are in the same array (where normal binary search
starts to work). So it is still binary search, only the catch part (mid equals begin)
is worth notice, in which case you simply move the begin index plus one to the right
to break the catch."""

class Solution:
    
    def search(self, nums: list[int], target: int) -> bool:
        
        def existsInFirst(nums: list[int], start: int, element: int) -> bool:
            
            return nums[start] <= element
    
        def isBinarySearchHelpful(nums: list[int], start: int, element: int) -> bool:
            
            return nums[start] != element
        
        n = len(nums)
        if n == 0: return False
        end = n - 1
        start = 0
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return True
            
            if not isBinarySearchHelpful(nums, start, nums[mid]):
                start += 1
                continue
            
            midArray = existsInFirst(nums, start, nums[mid])
            targetArray = existsInFirst(nums, start, target)
            
            if midArray != targetArray:
                # mid point and target in different arrays
                
                if midArray:
                    # mid in first and target in second
                    start = mid + 1
                else:
                    # mid in second and target in first
                    end = mid - 1
            else:
                # mid point and target in the same array
                
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return False