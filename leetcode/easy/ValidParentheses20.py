import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        # using stack to validate
        stack = []
        openc = set(['{', '(', '['])
        closec = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        for c in s:
            if c in openc:
                stack.append(c)
            else:
                if len(stack) < 1:
                    return False
                elif stack.pop() != closec[c]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

class RsTestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        t = '[}'
        r = s.isValid(t)
        assert not r
        t = '[]'
        r = s.isValid(t)
        assert r


if __name__ == '__main__':
    unittest.main()
