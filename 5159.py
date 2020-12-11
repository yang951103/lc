from functools import lru_cache

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = 'abc'

        def get_order(a, b, c):
            enu = list(enumerate([a, b, c]))
            enu.sort(key=lambda x: x[1], reverse=True)
            return [i[0] for i in enu]

        @lru_cache(None)
        def happy(i, j, k):
            arg = [i, j, k]
            i1, i2, i3 = get_order(*arg)
            if arg[i1] == 0:
                return ''
            if arg[i1] == 1:
                arg[i1] -= 1
                pre = s[i1]
                if arg[i2]:
                    arg[i2] -= 1
                    pre += s[i2]
                return pre + happy(*arg)
            if arg[i1] + arg[i1] % 2 == 2 * (arg[i2] + arg[i3] + 1):
                arg[i1] -= 2
                pre = s[i1] * 2
                if arg[i2]:
                    arg[i2] -= 1
                    pre += s[i2]
                return pre + happy(*arg)
            else:
                arg[i1] -= 2
                if arg[i2] >= 2:
                    arg[i2] -= 2
                    p2 = s[i2] * 2
                else:
                    arg[i2] -= 1
                    p2 = s[i2]
                return s[i1] * 2 + p2 + happy(*arg)

        arg = [a, b, c]
        m = max(arg)
        i = arg.index(m)
        arg.remove(m)
        if m > 2 * (sum(arg) + 1):
            m = 2 * (sum(arg) + 1)
        arg.insert(i, m)
        return happy(*arg)


if __name__ == '__main__':
    print(Solution().longestDiverseString(2,4,1))
