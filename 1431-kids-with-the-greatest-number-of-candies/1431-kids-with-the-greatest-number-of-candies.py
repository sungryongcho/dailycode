class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Maximum_Candies = max(candies)
        answers = []
        for c in candies:
            if c + extraCandies >= Maximum_Candies:
                answers.append(True)
            else:
                answers.append(False)
        return answers