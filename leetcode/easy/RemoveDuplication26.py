import unittest


class Solution:
    def removeDuplicates(self, nums) -> int:
        # edge case
        n = len(nums)
        if n in (0, 1):
            return n

        # at least two items now
        cnt_remove = 0
        need_move = False
        move_index = n-1
        cur = nums[move_index]
        cur_cnt = 1
        for i in range(n-2, -1, -1):
            if nums[i] == cur:
                if cur_cnt == 1:
                    move_index -= 1
                cur_cnt += 1
                cnt_remove += 1
                need_move = False
            else:
                cur = nums[i]
                if cur_cnt > 1:
                    cnt_remove -= 1
                cur_cnt = 1

                # there are items between current to move_index means need move
                if not need_move and ((move_index-i) > 1):
                    need_move = True
            new_len = n - cnt_remove
            if i == 0:
                need_move = True if move_index-(cur_cnt-1) > 0 else False
            if need_move:
                self.move(nums, i+1, move_index, new_len - (i+1))
        return new_len

    def move(self, nums, i_to, i_from, cnt):
        step = 0
        while (step < cnt):
            item = nums[i_from + step]
            nums[i_to + step] = item
            step += 1


class RsTestCase(unittest.TestCase):
    def test_solution_1(self):
        s = Solution()
        t1 = [5,5,5]
        r = s.removeDuplicates(t1)
        assert r == 1

    def test_solution_2(self):
        s = Solution()
        t1 = [5,5,5, 3]
        r = s.removeDuplicates(t1)
        assert r == 2
        assert t1[1] == 3

    def test_solution_3(self):
        s = Solution()
        t1 = [0,0,1,1,1,2,2,3,3,4]
        r = s.removeDuplicates(t1)
        assert r == 5

if __name__ == '__main__':
    unittest.main()
