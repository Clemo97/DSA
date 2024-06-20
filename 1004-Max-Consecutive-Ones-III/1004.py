def longestOnes(nums, k):
    left = 0
    max_len = 0
    zero_count = 0
    
    for right in range(len(nums)):
        # If we encounter a zero, increment the zero count
        if nums[right] == 0:
            zero_count += 1
            
        # If zero count exceeds k, move the left pointer to the right
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
            
        # Calculate the maximum length of the window
        max_len = max(max_len, right - left + 1)
        
    return max_len

# Test cases
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # Output: 6
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # Output: 10
