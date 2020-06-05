import unittest


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # find shortest str
        shortest = 0
        for i in range(len(strs)):
            if len(strs[i]) < len(strs[shortest]):
                shortest = i

        prefix = ''
        i = 0
        while i < len(strs[shortest]):
            # the char to compare
            current_char = strs[shortest][i]
            for s in strs:
                if i >= len(s):
                    return prefix
                if s[i] != current_char:
                    return prefix
            prefix += current_char
            i += 1
        return prefix


class AtnTestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        t = ['flower', 'flow', 'flight']
        r = s.longestCommonPrefix(t)
        assert r == 'fl'
        t = ['', 'flow', 'flight']
        r = s.longestCommonPrefix(t)
        assert r == ''


if __name__ == '__main__':
    unittest.main()
