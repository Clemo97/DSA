class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store unique characters in the current window
        unique_chars = set()
        # Variable to store the maximum length of substring found
        max_length = 0
        # Starting index of the current window
        start = 0

        # Loop through each character in the string with its index
        for end, char in enumerate(s):
            # If the character is already in the set, shrink the window from the left
            while char in unique_chars:
                # Remove the character at the start index from the set
                unique_chars.remove(s[start])
                # Move the start index to the right
                start += 1
            
            # Add the current character to the set
            unique_chars.add(char)
            # Update the maximum length if the current window is larger
            max_length = max(max_length, end - start + 1)
        
        # Return the maximum length found
        return max_length

# Testing the function
solution = Solution()

# Test case 1
s1 = "abcabcbb"
print(f"Test case 1 - Input: {s1} - Expected Output: 3 - Actual Output: {solution.lengthOfLongestSubstring(s1)}")

# Test case 2
s2 = "bbbbb"
print(f"Test case 2 - Input: {s2} - Expected Output: 1 - Actual Output: {solution.lengthOfLongestSubstring(s2)}")

# Test case 3
s3 = "pwwkew"
print(f"Test case 3 - Input: {s3} - Expected Output: 3 - Actual Output: {solution.lengthOfLongestSubstring(s3)}")

# Test case 4: String with all unique characters
s4 = "abcdef"
print(f"Test case 4 - Input: {s4} - Expected Output: 6 - Actual Output: {solution.lengthOfLongestSubstring(s4)}")

# Test case 5: String with a mix of repeating and non-repeating characters
s5 = "abcbdeafgh"
print(f"Test case 5 - Input: {s5} - Expected Output: 7 - Actual Output: {solution.lengthOfLongestSubstring(s5)}")

# Test case 6: Empty string
s6 = ""
print(f"Test case 6 - Input: {s6} - Expected Output: 0 - Actual Output: {solution.lengthOfLongestSubstring(s6)}")

# Test case 7: String with spaces and special characters
s7 = "a b c!d!e"
print(f"Test case 7 - Input: {s7} - Expected Output: 7 - Actual Output: {solution.lengthOfLongestSubstring(s7)}")
