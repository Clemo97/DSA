class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize an empty stack to store valid path components
        stk = []
        
        # Split the input path by '/' to process each component individually
        for s in path.split('/'):
            # Skip empty strings and single periods (current directory)
            if not s or s == '.':
                continue
            
            # If the component is a double period (parent directory)
            if s == '..':
                # Pop from stack if it's not empty (move up one directory level)
                if stk:
                    stk.pop()
            else:
                # Append valid directory names or file names to the stack
                stk.append(s)
        
        # Join the components in the stack with '/' and prepend a '/' to form the final path
        return '/' + '/'.join(stk)

# Example usage
solution = Solution()

# Test cases
test_cases = [
    ("/home/", "/home"),
    ("/home//foo/", "/home/foo"),
    ("/a/./b/../../c/", "/c"),
    ("/../", "/"),
    ("/home/../../..", "/"),
    ("/.../a/../b/c/../d/./", "/.../b/d"),
    ("/a//b////c/d//././/..", "/a/b/c"),
    ("/", "/"),
    ("/./././.", "/"),
    ("/../../../../a/b/c", "/a/b/c")
]

# Execute test cases
for path, expected in test_cases:
    result = solution.simplifyPath(path)
    print(f"Input: {path}\nOutput: {result}\nExpected: {expected}\n{'Pass' if result == expected else 'Fail'}\n")
