def characterReplacement(s: str, k: int) -> int:
    # Dictionary to store the frequency of characters in the current window
    count = {}
    # Variable to keep track of the maximum frequency of any single character in the current window
    max_count = 0
    # Left pointer for the sliding window
    left = 0
    # Variable to keep track of the maximum length of a valid window found so far
    max_length = 0

    # Iterate through the string with the right pointer
    for right in range(len(s)):
        # Increment the count of the current character
        count[s[right]] = count.get(s[right], 0) + 1
        # Update max_count to the highest frequency of a single character in the current window
        max_count = max(max_count, count[s[right]])
        
        # Current window size
        window_size = right - left + 1
        # If more replacements are needed than allowed, shrink the window
        if window_size - max_count > k:
            # Decrement the count of the character that is sliding out of the window
            count[s[left]] -= 1
            # Move the left pointer to the right to shrink the window
            left += 1
        
        # Update the maximum length of the window
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
print(characterReplacement("ABAB", 2))  # Expected output: 4
print(characterReplacement("AABABBA", 1))  # Expected output: 4
print(characterReplacement("AAAA", 2))  # Expected output: 4, no need to replace any character
print(characterReplacement("AABBBB", 1))  # Expected output: 6, no need to replace any character
print(characterReplacement("ABCDE", 2))  # Expected output: 3, replace two of 'C', 'D', or 'E'
print(characterReplacement("ABBB", 2))  # Expected output: 4, replace 'A' and 'B' to form "BBBB"
print(characterReplacement("BAAAB", 2))  # Expected output: 5, replace 'B' to form "AAAAA"
print(characterReplacement("AABACCAA", 2))  # Expected output: 5, replace 'B' and 'C' to form "AAAAAAA"
print(characterReplacement("AAAAAA", 0))  # Expected output: 6, no replacements allowed but already the same character
print(characterReplacement("A", 0))  # Expected output: 1, single character string
