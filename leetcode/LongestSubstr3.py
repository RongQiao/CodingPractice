import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """all of the substrings are 1+2+3+...+n = (1+n)n/2
        count every letter, put them into dict
        then the possible longest substr is len(dict)
        think about str len is n, dic len is m
        the possible substring is len<=m

        """
        pass


class LsTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        s = 'bbbbb'
        ret = sol.lengthOfLongestSubstring(s)
        self.assertEqual(ret, 1)


if __name__ == '__main__':
    unittest.main()
