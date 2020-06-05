import unittest


class Solution:
    def intToRoman(self, num: int) -> str:
        nsm = {1000:'M',
               500:'D',
               100:'C',
               50:'L',
               10:'X',
               5:'V',
               1:'I'
               }
        sl = sorted(nsm, reverse=True)
        ret = ''
        i = 0
        while num > 0 and i < len(sl)-1:
            cnt = num // sl[i]
            left = num % sl[i]
            if (cnt > 0) and (left // sl[i+1] == 4):
                # 9
                ret += nsm[sl[i+1]] + nsm[sl[i-1]]
                num = num - 9 * sl[i+1]
            elif (cnt == 0) and (left // sl[i+1] == 4):
                # 4
                ret += nsm[sl[i+1]] + nsm[sl[i]]
                num = num - 4 * sl[i+1]
            else:
                ret += nsm[sl[i]] * cnt
                num -= sl[i] * cnt
            i += 1
        # last Is
        if num > 0:
            ret += nsm[sl[len(sl)-1]] * num
        return ret


class AnTestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        t = 9
        r = s.intToRoman(t)
        assert r == 'IX'


if __name__ == '__main__':
    unittest.main()
