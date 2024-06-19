class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Dictionary to keep track of the count of characters in the current window
        char_frequency = {}
        # The start index of the current window
        window_start = 0
        # To store the length of the longest valid substring found
        max_length = 0

        # Iterate over the string with `window_end` as the index of the current character
        for window_end in range(len(s)):
            # Current character in the window
            char = s[window_end]
            # Add the character to `char_frequency` and increment its count
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
                
            print("Dictionary: ", char_frequency)

            # If the number of distinct characters exceeds `k`, shrink the window from the left
            while len(char_frequency) > k:
                # Character at the start of the window
                left_char = s[window_start]
                print("left char", left_char)
                # Decrement the count of the character at the start of the window
                char_frequency[left_char] -= 1
                # If the count of the character becomes 0, remove it from `char_frequency`
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                # Move the start of the window to the window_end
                window_start += 1
                
                print("window start", window_start)

            # Update `max_length` to be the maximum of its current value or the size of the current window
            max_length = max(max_length, window_end - window_start + 1)
            print("Max Length",max_length)

        # Return the length of the longest substring found that contains at most `k` distinct characters
        return max_length

# Test cases
solution = Solution()

# Test case 1
s1 = "eceba"
k1 = 2
print(f"Test case 1: {solution.lengthOfLongestSubstringKDistinct(s1, k1)}")  # Expected output: 3 ("ece" or "cec")

# # Test case 2
# s2 = "aa"
# k2 = 1
# print(f"Test case 2: {solution.lengthOfLongestSubstringKDistinct(s2, k2)}")  # Expected output: 2 ("aa")

# # Test case 3
# s3 = "aabbcc"
# k3 = 2
# print(f"Test case 3: {solution.lengthOfLongestSubstringKDistinct(s3, k3)}")  # Expected output: 4 ("aabb", "bbcc")

# # Test case 4
# s4 = "abcadchcacaca"
# k4 = 3
# print(f"Test case 4: {solution.lengthOfLongestSubstringKDistinct(s4, k4)}")  # Expected output: 11 ("cadcacacaca")

# # Test case 5
# s5 = "abaccc"
# k5 = 2
# print(f"Test case 5: {solution.lengthOfLongestSubstringKDistinct(s5, k5)}")  # Expected output: 4 ("abac", "bacc", "accc")
