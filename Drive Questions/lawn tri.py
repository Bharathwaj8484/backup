def count_valid_numbers(x):
    # Edge case: sum of 0 has one "empty" solution
    if x == 0:
        return 1
    
    # Create array: dp[i] will store count for sum = i
    dp = [0] * (x + 1)  # e.g., x=4 → [0,0,0,0,0]
    
    # Base case: one way to make sum 0 (use nothing)
    dp[0] = 1
    
    # Build up from sum=1 to sum=x
    for i in range(1, x + 1):
        # If we can add digit 1, inherit solutions from (i-1)
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        # If we can add digit 2, inherit solutions from (i-2)
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        # If we can add digit 3, inherit solutions from (i-3)
        if i - 3 >= 0:
            dp[i] += dp[i - 3]
    
    # Return the count for our target sum x
    return dp[x]
x =4
result = count_valid_numbers(x)
print(f"✅ Count of valid numbers (digits 1,2,3) that sum to {x}: {result}")
# Output: 274 (instant!)
