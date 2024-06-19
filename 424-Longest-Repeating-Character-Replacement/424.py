class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()  # To track unique characters in the current window
        max_length = start = 0  # Initialize max length and start index
        
        for end, char in enumerate(s):  # Iterate over the string with index and character
            while char in unique_chars:  # If character is a duplicate
                unique_chars.remove(s[start])  # Remove the character at the start index
                start += 1  # Move the start index to the right
            unique_chars.add(char)  # Add the current character to the set
            max_length = max(max_length, end - start + 1)  # Update the max length
        
        return max_length  # Return the length of the longest substring without repeating characters

# Create an instance of the Solution class
solution = Solution()

# Test cases
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
print(solution.lengthOfLongestSubstring(""))          # Output: 0
print(solution.lengthOfLongestSubstring("a"))         # Output: 1
print(solution.lengthOfLongestSubstring("abcbda"))    # Output: 4
