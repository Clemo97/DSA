from typing import List

class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        # Initialize the starting index of the subarray with the maximum value
        max_start_index = 0
        
        # Iterate over possible starting indices for subarrays of length k
        # The loop goes from 1 to len(nums) - k to ensure subarray length is always k
        for i in range(1, len(nums) - k + 1):
            print("first: ", i)
            # Compare the current element with the element at max_start_index
            # Update max_start_index if a larger element is found
            if nums[i] > nums[max_start_index]:
                print(True)
                max_start_index = i
            else:
                print(False)
        
        # Return the subarray starting from max_start_index and of length k
        return nums[max_start_index : max_start_index + k]


# Test the function with the given input
nums = [1, 4, 5, 2, 8, 3, 6]
k = 3


# Create an instance of the Solution class
solution = Solution()

# Call the largestSubarray method with the test input and store the result
result = solution.largestSubarray(nums, k)

# Print the result
print(result)  # Expected output: [5, 2, 3]
