from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize the left pointer, current sum, and minimum length
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            # Add the current element to the current sum
            current_sum += nums[right]
            
            # While the current sum is greater than or equal to the target
            while current_sum >= target:
                # Update the minimum length of the subarray
                min_length = min(min_length, right - left + 1)
                # Subtract the element at the left pointer and move the left pointer to the right
                current_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0

# Test the function with the given example
solution = Solution()
print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # Expected output: 2
print(solution.minSubArrayLen(4, [1, 4, 4]))           # Expected output: 1
print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # Expected output: 0
