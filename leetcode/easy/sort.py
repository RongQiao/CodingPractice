import unittest


class Solution:
    def merge_sort(self, nums):
        if len(nums) > 1:
            self.merge_sort_helper(nums, 0, len(nums))

    def merge_sort_helper(self, nums, start, end):
        n = end - start
        if n <= 1:
            return
        else:
            m = int((start + end)/2)
            self.merge_sort_helper(nums, start, m)
            self.merge_sort_helper(nums, m, end)
            self.merge(nums, start, m, end)

    def merge(self, nums, start, middle, end):
        i = start
        j = middle
        tmp = []
        while i < middle:
            while j < end:
                if nums[i] < nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
        nums[start:end] = tmp


class AtnTestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        t = [1,3]
        s.merge_sort(t)
        print(t)



if __name__ == '__main__':
    unittest.main()
