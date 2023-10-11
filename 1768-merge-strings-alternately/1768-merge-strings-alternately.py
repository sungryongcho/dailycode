class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        cur1 = 0
        cur2 = 0
        res = ""
        while cur1 < len(word1) and cur2 < len(word2):
            res += word1[cur1] + word2[cur2]
            cur1 += 1
            cur2 += 1
        if cur1 != len(word1):
            res += word1[cur1:]
        if cur2 != len(word2):
            res += word2[cur2:]
        return res