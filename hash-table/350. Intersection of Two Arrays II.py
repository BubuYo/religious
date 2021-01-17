class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1, m2 = DefaultDict(int), DefaultDict(int)
        for i in nums1:
            m1[i] += 1
        for i in nums2:
            m2[i] += 1
        result = []
        for i in nums1:
            if i in nums2:
                if m1[i] and m2[i]:
                    result.append(i)
                    m1[i] -= 1
                    m2[i] -= 1
        return result
