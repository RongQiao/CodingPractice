import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        #
        # dummy = ListNode(0)
        # h1 = l1
        # h2 = l2
        #
        # # h1 always point to min()
        # if h1.val > h2.val:
        #     t = h1
        #     h1 = h2
        #     h2 = t
        # dummy.next = h1
        #
        # while (h1.next is not None) and (h2 is not None):
        #     while h1.next.val <= h2.val:
        #         h1 = h1.next
        #         if h1.next is None:
        #             break
        #     # insert h2
        #     t = h1.next
        #     h1.next = h2
        #     h1 = h2
        #     h2 = t
        #     # s = self.print_list(dummy)
        #
        #
        # if not h1.next:
        #     h1.next = h2
        # return dummy.next

    def print_list(self, h):
        s = ''
        while h is not None:
            s += str(h.val) + ','
            h = h.next
        print(s)
        return s


class RsTestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        t1 = ListNode(1, None) #ListNode(2, ListNode(4, None)))
        t2 = ListNode(2, ListNode(3, ListNode(4, None)))
        r = s.mergeTwoLists(t1, t2)
        s.print_list(r)
        assert r.val == 1

if __name__ == '__main__':
    unittest.main()
