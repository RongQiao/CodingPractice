import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """The point is to process the carrier
        """
        carrier = 0
        out = None
        current = None
        while ((l1 is not None) or (l2 is not None)):
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = x + y + carrier
            current_sum = sum % 10
            carrier = sum // 10
            if current is None:
                current = ListNode(current_sum)
            else:
                current.next = ListNode(current_sum)
                current = current.next
            if out is None:
                out = current
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carrier > 0:
            current.next = ListNode(carrier)
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
