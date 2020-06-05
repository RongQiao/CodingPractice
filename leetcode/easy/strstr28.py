import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is None or len(needle)==0:
            return 0
        if haystack is None or len(needle) > len(haystack):
            return -1
        # all valid string
        fi = 0
        ni = 0
        result = -1
        while fi < len(haystack):
            if haystack[fi] != needle[ni]:
                if (result < 0):
                    fi += 1
                else:
                    fi = result + 1
                    ni = 0
                    result = -1
            else:
                if (result < 0) and (len(haystack)-fi >= len(needle)):
                    result = fi
                if ni == len(needle) - 1:
                    return result
                ni += 1
                fi += 1
        return result


class AtnTestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        t1 = 'mississippi'
        t2 = 'issipi'
        r = s.strStr(t1, t2)
        print(r)
        assert r == -1


if __name__ == '__main__':
    unittest.main()
