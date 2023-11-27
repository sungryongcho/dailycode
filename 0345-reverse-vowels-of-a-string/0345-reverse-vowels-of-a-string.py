class Solution:
    def reverseVowels(self, s: str) -> str:
        a = list(s)
        list1 = {'a','e','i','o','u','A','E',"I","O","U"}
        l = 0
        r = len(s)-1
        while l < r:
            while l < r and a[l] not in list1:
                l +=1
            while l < r and a[r] not in list1:
                r -= 1
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1

        return ''.join(a)