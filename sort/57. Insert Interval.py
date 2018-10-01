# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start, end, left, right = newInterval.start, newInterval.end, [], []
        for i in intervals:
            if start > i.end:
                left.append(i)
            elif end < i.start:
                right.append(i)
            else:
                start = min(start, i.start)
                end = max(end, i.end)
        return left + [Interval(start, end)] + right
