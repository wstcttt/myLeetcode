class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Force solution will be TLE
        # i = 0
        # j = 1
        # ed = len(height)
        # maxarea = 0
        # while i < ed-1:
        #     while j < ed:
        #         h = height[j] if height[j] < height[i] else height[i]
        #         area = (j-i)*h
        #         if area > maxarea:
        #             maxarea = area
        #         j += 1
        #     i += 1
        #     j = i + 1
        # return maxarea

        i = 0
        j = len(height) - 1
        maxarea = 0
        while i<j:
            h = height[i] if height[i]<height[j] else height[j]
            area = (j-i)*h
            if area > maxarea:
                maxarea = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxarea
