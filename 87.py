from collections import Counter
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if not s1:
            return False
        if Counter(s1) != Counter(s2):
            return False
        self.is_dict = {}
        return self.is_sramble(s1, s2)

    def is_sramble(self, s1, s2):
        # print(s1, s2)
        s = s1 + ' ' + s2
        if s in self.is_dict:
            # print(self.is_dict)
            return self.is_dict[s]
        if s1 == s2:
            self.is_dict[s] = True
            return True
        for i in range(1, len(s1)):
            if self.is_sramble(s1[0:i], s2[0:i]) and self.is_sramble(s1[i:], s2[i:]):
                # print(s, 1)
                self.is_dict[s] = True
                return True

            if self.is_sramble(s1[0:i], s2[-i:]) and self.is_sramble(s1[i:], s2[0:-i]):
                # print(s, 2)
                self.is_dict[s] = True
                return True
        self.is_dict[s] = False
        return False

if __name__ == '__main__':

    print(Solution().isScramble("abcde",
"caebd"))