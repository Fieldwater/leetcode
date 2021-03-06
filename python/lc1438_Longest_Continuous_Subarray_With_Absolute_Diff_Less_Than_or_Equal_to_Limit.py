"""
2021.2
idea: slide window + sorted list achieved by BTree
 - In Python, there is sortedlist faster than Btree in sortedcontainers library
"""


from sortedcontainers import SortedList
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = SortedList()
        n = len(nums)
        left = right = ret = 0

        while right < n:
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            ret = max(ret, right - left + 1)
            right += 1
        
        return ret
