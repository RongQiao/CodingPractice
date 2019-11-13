import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addSameSpotsTwolists(self, cl1: ListNode, cl2: ListNode, sum_h):
        out = None
        pout = None
        while (cl1 is not None) and (cl2 is not None):
            sum = cl1.val + cl2.val + sum_h
            if sum >= 10:
                sum_h = sum // 10
                sum_l = sum % 10
            else:
                sum_h = 0
                sum_l = sum
            if out is None:
                out = ListNode(sum_l)
            if pout is None:
                pout = out
            else:
                pout.next = ListNode(sum_l)
                pout = pout.next
            # next
            cl2 = cl2.next
            cl1 = cl1.next
        if cl1 is None:
            return (out, cl2, pout, sum_h)
        else:
            return (out, cl1, pout, sum_h)

    def addSinglelist(self, cl1: ListNode, sum_h, out: ListNode, pout: ListNode):
        while cl1 is not None:
            sum = cl1.val + sum_h
            if sum >= 10:
                sum_h = sum // 10
                sum_l = sum % 10
            else:
                sum_h = 0
                sum_l = sum
            if out is None:
                out = ListNode(sum_l)
            if pout is None:
                pout = out
            else:
                pout.next = ListNode(sum_l)
                pout = pout.next
            # next
            cl1 = cl1.next
        if sum_h > 0:
            pout.next = ListNode(sum_h)
        return out

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """split the process to two parts:
            the parts both lists have
            the parts only one list and the carry
        """
        # process spots occur in both of l1 and l2,
        # output is in 'out' parameter
        # return a tuple includes:
        #   the output
        #   the longer list
        #   the output's lst node
        #   the sum_h part
        sum_h = 0
        ret = self.addSameSpotsTwolists(l1, l2, sum_h)
        out = ret[0]
        cl1 = ret[1]
        pout = ret[2]
        sum_h = ret[3]
        # process following
        out = self.addSinglelist(cl1, sum_h, out, pout)
        return out


class AtnTestCase(unittest.TestCase):
    def test_something(self):
        l13 = ListNode(3)
        l12 = ListNode(4)
        l11 = ListNode(2)
        l11.next = l12
        l12.next = l13
        l23 = ListNode(4)
        l22 = ListNode(6)
        l21 = ListNode(5)
        l21.next = l22
        l22.next = l23
        sol = Solution()
        o1 = sol.addTwoNumbers(l11, l21)
        self.assertEqual(o1.val, 7)
        o2 = o1.next
        self.assertEqual(o2.val, 0)
        o3 = o2.next
        self.assertEqual(o3.val, 8)
        self.assertIs(o3.next, None)


if __name__ == '__main__':
    unittest.main()
