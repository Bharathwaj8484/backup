arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)
if n <= 1:
    print(0)
if arr[0] == 0:
    print(-1)

jumps = 0
i = 0

while i < n - 1:
    # If we can directly reach the end
    if i + arr[i] >= n - 1:
        jumps += 1
        break

# Find best next index
    max_reach = -1
    next_index = -1

    for j in range(i + 1, i + arr[i] + 1):
        if j < n and j + arr[j] > max_reach:
            max_reach = j + arr[j]
            next_index = j

# If no progress possible
    if next_index == -1:
        print(-1)
        break

    i = next_index
    jumps += 1

print(jumps)
