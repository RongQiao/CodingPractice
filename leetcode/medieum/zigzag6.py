import unittest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s is None or len(s) <= numRows:
            return s
        tmp = [''] * numRows
        current = 0
        sign = 1
        bc_max = 0 if (numRows < 3) else numRows - 2
        bc_left = 0
        turn = False
        for i in range(len(s)):
            if sign > 0:
                tmp[current] += s[i]
            else:
                pre = ' ' * bc_left
                post = ' ' * (bc_max - bc_left - 1)
                tmp[current] += pre + s[i] + post
                if bc_left == bc_max:
                    turn = True
                bc_left += 1
            if turn or current+1 == numRows:
                sign *= (-1)
                turn = False
                if current + 1 == numRows:
                    tmp[current] += ' '*bc_max
                    bc_left = 0
            current += sign
        ret = ''.join(tmp).replace(' ', '')
        return ret


class AnTestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        t = 'PAYPALISHIRING'
        r = s.convert(t, 3)
        print(r)
        assert r == "PAHNAPLSIIGYIR"


if __name__ == '__main__':
    unittest.main()
