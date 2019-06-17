#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (38.02%)
# Total Accepted:    78K
# Total Submissions: 203.9K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
# 
# Example:
# 
# 
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
#
import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s, ans = sorted(nums), []
        for i in nums:
            idx = bisect.bisect_left(s, i)
            ans.append(idx)
            s.pop(idx)
        return ans
