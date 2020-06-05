import unittest


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # binary search
        n = len(nums)
        if n == 0 or nums[0] > target:
            return 0
        elif nums[n-1] < target:
            return n
        p = int(n / 2)
        if nums[p] == target:
            return p
        elif nums[p] < target:
            return self.searchInsert(nums[p+1:], target) + (p + 1)
        else:
            return self.searchInsert(nums[:p-1], target)


class AtnTestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        t1 = [1,3]
        t2 = 2
        r = s.searchInsert(t1, t2)
        print(r)
        assert r == 1


if __name__ == '__main__':
    unittest.main()
