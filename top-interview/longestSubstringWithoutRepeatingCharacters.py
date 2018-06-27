class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l = len(s)
        start = 0
        end = 1
        maxlen = 1
        while end < l:
            clen = end - start + 1
            if s[end] in s[start:end]:
                #start += 1    #first submit, not the best
                #optimized, skip all the elements from start_index to dup_index
                dup = s[start:end].index(s[end])
                start = start + dup + 1
            else:
                end += 1
                if clen > maxlen:
                    maxlen = clen
        return maxlen

