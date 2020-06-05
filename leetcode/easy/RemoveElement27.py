import unittest


class Solution:
    def removeElement(self, nums, val: int) -> int:
        cnt = 0
        for item in nums:
            if item == val:
                cnt += 1
        # only need move items begin from index = n-cnt which != val
        index_to = 0
        index_from = len(nums) - cnt
        while (index_to < len(nums)-cnt):
            if nums[index_to] != val:
                index_to += 1
            else:
                if nums[index_from] == val:
                    index_from += 1
                else:
                    nums[index_to] = nums[index_from]
                    index_to += 1
                    index_from += 1
        return len(nums) - cnt


class AtnTestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        t = [0, 1, 2, 2, 3, 0, 4, 2]
        r = s.removeElement(t, 2)
        assert r == 5
        print(t[:-r])


if __name__ == '__main__':
    unittest.main()
