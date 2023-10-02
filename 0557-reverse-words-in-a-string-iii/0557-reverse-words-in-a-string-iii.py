class Solution:
    def reverseWords(self, s: str) -> str:
        L = []
        string = s.split()
        for word in string:
            y = list(word)
            start = 0
            end = len(y) - 1
            while start < end:
                temp = y[start]
                y[start] = y[end]
                y[end] = temp
                start += 1
                end -= 1
            new_string = ''.join(y)
            L.append(new_string)
        return ' '.join(L)