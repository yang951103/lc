from typing import List
from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        bl_set = defaultdict(set)
        nums = set([str(i) for i in range(1, 10)])
        dot_list = []
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    dot_list.append([i, j])
                    continue
                bl = (i // 3)*3 + j // 3
                row_set[i].add(val)
                col_set[j].add(val)
                bl_set[bl].add(val)

        n = len(dot_list)
        stack = []
        count = 0
        try_dict = defaultdict(set)
        def next_num(next_count):
            if next_count == n:
                return 0
            i, j = dot_list[next_count]
            b = (i // 3) * 3 + j // 3
            return len(nums - row_set[i] - col_set[j] - bl_set[b])
        while count < n:
            i, j = dot_list[count]
            b = (i // 3) * 3 + j // 3
            left_set = nums - row_set[i] - col_set[j] - bl_set[b] - try_dict[count]
            if left_set:
                insert_num = 0
                space = 0
                for left_num in left_set:
                    for _set in (row_set[i], col_set[j], bl_set[b]):
                        _set.add(left_num)
                    next_space = next_num(count+1)
                    for _set in (row_set[i], col_set[j], bl_set[b]):
                        _set.remove(left_num)
                    if next_space >= space:
                        insert_num = left_num
                        space = next_space
                for _set in (row_set[i], col_set[j], bl_set[b]):
                    _set.add(insert_num)
                stack.append(insert_num)
                try_dict[count].add(insert_num)
                count += 1
            else:
                try_dict[count].clear()
                count -= 1
                rm_num = stack.pop()
                i, j = dot_list[count]
                b = (i // 3) * 3 + j // 3
                for _set in (row_set[i], col_set[j], bl_set[b]):
                    _set.remove(rm_num)

            # print(stack)

        for p, v in zip(dot_list, stack):
            board[p[0]][p[1]] = v


if __name__ == '__main__':
    a = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    Solution().solveSudoku(a)
    for clm in a:
        print(clm)

