x = 10
n = int('1' * x) + 1
j = 0
for i in range(1, n):  # Start from 1 (0 contains digit 0 → invalid)
    temp = i          # 🔹 Use temp to preserve original i
    s = 0
    valid = True      # 🔹 Flag: assume number is valid until proven otherwise
    
    while temp > 0:
        digit = temp % 10
        
        # 🔹 CONDITION: Only allow digits 1, 2, or 3
        if digit not in {1, 2, 3}:
            valid = False
            break  # No need to check remaining digits
        
        s += digit
        temp //= 10
    if valid and s == x:
        j += 1
        print(f"✓ Found: {i} (digits sum to {x})")  # Optional: see which numbers match
print(j)
        
