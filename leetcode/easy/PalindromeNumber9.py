import unittest


class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False
        elif x < 10:
            return True

        xrev = 0
        while (x > xrev):
            xrev = xrev * 10 + x % 10
            x = int(x / 10)

        return (x == xrev) or (x == int(xrev / 10))

class RsTestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        assert s.isPalindrome(121)

if __name__ == '__main__':
    unittest.main()
