class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        c, tmpC = [0, 0]
        for num in nums:
            if c + num > 0:
                c += num
            tmpC += num
            if tmpC > c:
                c = tmpC
        return c


x = Solution()
print(x.maxSubArray(
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
