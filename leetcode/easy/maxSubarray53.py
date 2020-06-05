import unittest

class SubResult(object):
    def __init__(self, sum, s, e):
        self.sum = sum
        self.start = s
        self.end = e

class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0
        subsum = nums[0]
        maxs = subsum

        for i in range(1, len(nums)):
            subsum = max(subsum + nums[i], nums[i])
            maxs = max(maxs, subsum)

        return maxs


class AtnTestCase(unittest.TestCase):
    def test_solution_1(self):
        s = Solution()
        t = [4]
        r = s.maxSubArray(t)
        assert r == 4

    def test_solution_2(self):
        s = Solution()
        t = [4,2]
        r = s.maxSubArray(t)
        assert r == 6

    def test_solution_2(self):
        s = Solution()
        t = [4,-1,2,1]
        r = s.maxSubArray(t)
        assert r == 6

    def test_solution_2(self):
        s = Solution()
        t = [4,-1,2,1,-5,4]
        r = s.maxSubArray(t)
        assert r == 6



if __name__ == '__main__':
    unittest.main()
