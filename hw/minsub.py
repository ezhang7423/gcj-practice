import math


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        a, c = [-math.inf, 0]
        for num in nums:
            if c <= 0:
                c = num
            else:
                c += num
            if c > a:
                a = c

        return a


x = Solution()
print(x.maxSubArray(
    [1, -1, 20]))
