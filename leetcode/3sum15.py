import unittest
import list


class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(s)
        start = 0
        end = n-1
        while start < end:
            swap = s[start]
            s[start] = s[end]
            s[end] = swap
            # change index
            start += 1
            end -= 1


class RsTestCase(unittest.TestCase):
    def test_RS(self):
        sol = Solution()
        s = list('123456')
        r = s[::-1]
        sol.reverseString(s)
        self.assertEqual(s, r)


if __name__ == '__main__':
    unittest.main()
