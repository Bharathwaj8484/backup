import re

# Read number of test cases
T = int(input())
count = 0

# Pattern: one or more 'a' followed by one or more 'b'
pattern = re.compile(r'^a+b+$')

for _ in range(T):
    s = input()
    if pattern.match(s):
        count += 1

print(count)

# T = int(input())

# # Initialize counter for special strings
# special_count = 0

# # Process each test case
# for _ in range(T):
#     s = input()
#     n = len(s)
    
#     # Try every possible split point (excluding empty s1 or s2)
#     for i in range(1, n):
#         s1 = s[:i]
#         s2 = s[i:]
#         if all(c == 'a' for c in s1) and all(c == 'b' for c in s2):
#             special_count += 1
#             break  # Only count once per string

# # Print the result
# print(special_count)