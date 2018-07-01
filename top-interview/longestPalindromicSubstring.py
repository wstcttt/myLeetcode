class Solution:
    def getPal(self, s, l, r, res):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                pal = s[l:r+1]
                if len(pal) > len(res):
                    res = pal
                l -= 1
                r += 1
            else:
                break
        return res

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        if len(s) == 1:
            return s
        res = s[0] if s[0]!=s[1] else s[:2]
        for i in range(len(s)):
            res = self.getPal(s, i-1, i+1, res)
            res = self.getPal(s, i, i+1, res)
        return res

#Manacher's Algorithm is too difficult!
