class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        s = str(x)
        neg = False
        res = ""
        if s[0] == "-":
            neg = True
            s = s[1:]
        i = len(s) - 1
        while i >= 0:
            if s[i] == 0:
                i -= 1
            else:
                break
        while i >= 0:
            res += s[i]
            i -= 1
        maxnum = 1<<31
        minnum = ~(1<<31)
        if len(res) == 1:
            res = int(res)
            return -res if neg else res
        restemp = int(res[:-1])  #res[:-1] is '' if res is 'x'
        reslast = int(res[-1])
        if neg:
            restemp = -restemp
            reslast = -reslast
            if restemp < minnum//10:
                return 0
            elif restemp == minnum//10:
                if reslast < minnum%10:
                    return 0
        else:
            if restemp > maxnum//10:
                return 0
            elif restemp == maxnum//10:
                if reslast > maxnum%10:
                    return 0
        res = int(res)
        return -res if neg else res
