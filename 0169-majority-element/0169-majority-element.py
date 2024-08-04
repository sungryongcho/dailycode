class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize the count and the candidate for majority element
        count = 0
        majority_candidate = None
      
        # Process each number in the list
        for num in nums:
            # If the current count is 0, we choose a new number as the potential majority candidate
            if count == 0:
                majority_candidate = num
                count = 1
            # If the current number is the same as the majority candidate, increase the count
            elif majority_candidate == num:
                count += 1
            # Otherwise, decrease the count
            else:
                count -= 1
      
        # The majority candidate is the number that remains after pairing off different elements
        return majority_candidate