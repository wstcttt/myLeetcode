class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        num = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        i = 0
        j = 1
        while j < len(s):
            if num[s[i]]<num[s[j]]:
                res = res + num[s[j]] - num[s[i]]
                i = j + 1
                j = i + 1
            else:
                res = res + num[s[i]]
                i = j
                j = i + 1
        if i < len(s):
            res = res + num[s[i]]
        return res
