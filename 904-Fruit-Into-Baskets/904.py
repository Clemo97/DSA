from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Initialize a counter to keep track of the number of each type of fruit in the current window
        cnt = Counter()
        # Initialize the left pointer of the sliding window
        j = 0
        
        # Iterate through the array of fruits with the right pointer
        for x in fruits:
            # Add the current fruit to the counter
            cnt[x] += 1
            
            # If there are more than two types of fruits in the counter
            if len(cnt) > 2:
                # Get the fruit type at the left pointer
                y = fruits[j]
                # Decrease the count of that fruit type in the counter
                cnt[y] -= 1
                # If the count of that fruit type becomes zero, remove it from the counter
                if cnt[y] == 0:
                    cnt.pop(y)
                # Move the left pointer to the right
                j += 1
        
        # The length of the longest valid subarray is the total number of fruits minus the position of the left pointer
        return len(fruits) - j

# Test the function with the given examples
solution = Solution()

# List of test cases with expected results
test_cases = [
    ([1, 2, 1], 3),
    ([0, 1, 2, 2], 3),
    ([1, 2, 3, 2, 2], 4),
    ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5),
    ([1, 2, 1, 1, 2, 2], 6),
    ([1], 1),
    ([0, 1, 2, 3, 4], 2),
    ([1, 2, 2, 3, 3, 4, 4, 5], 4)
]

for fruits, expected in test_cases:
    result = solution.totalFruit(fruits)
    print(f"fruits = {fruits} -> Expected: {expected}, Got: {result}")
