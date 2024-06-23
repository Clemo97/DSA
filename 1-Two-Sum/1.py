def two_sum(nums, target):
    # Initialize an empty hash map to store numbers and their indices
    num_to_index = {}
    
    # Iterate over the list of numbers with their indices
    for index, num in enumerate(nums):
        # Calculate the complement of the current number with respect to the target
        complement = target - num
        
        # Check if the complement is already in the hash map
        if complement in num_to_index:
            # If it is, return the indices of the complement and the current number
            return [num_to_index[complement], index]
        
        # If the complement is not in the hash map, add the current number and its index to the hash map
        num_to_index[num] = index

# Example usage
nums = [2, 7, 11, 15]
target = 9

# This will print [0, 1] because nums[0] + nums[1] == 9
print(two_sum(nums, target))
