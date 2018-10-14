class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        count_info, l = collections.Counter(S), len(S)
        if max(count_info.values()) > (l + 1) // 2: return ''

        ans = ''
        for _ in range(l):
            char_info = sorted([(v, k) for k, v in count_info.items()])
            if ans and ans[-1] == char_info[-1][-1]:
                max_char = char_info[-2][-1]
            else:
                max_char = char_info[-1][-1]
            ans, count_info[max_char] = ans + max_char, count_info[max_char] - 1
            if not count_info[max_char]:
                del count_info[max_char]
        return ans
