import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sub = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }

        result = 0
        i = 0
        n = len(s)
        while i < n:
            a = rom[s[i]]
            b = 0
            # check if it's subtraction case
            if (i+1 < n):
                if (s[i] in sub) and (s[i+1] in sub[s[i]]):
                    a = -a
                    b = rom[s[i+1]]
                    i += 2
                else:
                    i += 1
            else:
                i += 1
            # result
            result += a + b
        return result


class AtnTestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        t = 'III'
        r = s.romanToInt(t)
        assert r == 3


if __name__ == '__main__':
    unittest.main()
