from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result_list = []
        try_list = [set() for _ in range(n)]
        stack = []
        left_pos = [set(range(n)) for _ in range(n)]
        while True:
            print(left_pos, stack)
            i = len(stack)
            # find one solution
            if i == n:
                result_list.append(stack[:])
                stack.pop()
                continue
            if len(left_pos[i]):
                pos = left_pos[i].pop()
                try_list[i].add(pos)
                stack.append(pos)
                # update left_pos
                for j in range(i+1, n):
                    print(left_pos[j], pos)
                    left_pos[j].remove(pos)
                x, y = i + 1, pos + 1
                while x < n and y < n:
                    left_pos[x].remove(y)
                    x += 1
                    y += 1
                x, y = i + 1, pos - 1
                while x < n and y >= 0:
                    left_pos[x].remove(y)
                    x += 1
                    y -= 1
            else:
                if i == 0:
                    break
                left_pos[i] = left_pos[i].union(try_list[i])
                pos = stack.pop()
                i -= 1
                for j in range(i+1, n):
                    left_pos[j].add(pos)
                x, y = i + 1, pos + 1
                while x < n and y < n:
                    left_pos[x].add(y)
                    x += 1
                    y += 1
                x, y = i + 1, pos - 1
                while x < n and y >= 0:
                    left_pos[x].add(y)
                    x += 1
                    y -= 1
        q = []
        for l in result_list:
            one = [['.']*n for _ in range(n)]
            for i, j in enumerate(l):
                one[i][j] = 'Q'
            q.append([''.join(l) for l in one])
        print(len(q))
        return q

if __name__ == '__main__':
    Solution().solveNQueens(4)
