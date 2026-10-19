def count_valid_numbers(x):
    if x == 0: return 1
    if x == 1: return 1
    if x == 2: return 2
    
    # Only keep last 3 values
    a, b, c = 1, 1, 2  # dp[0], dp[1], dp[2]
    
    for i in range(3, x + 1):
        a, b, c = b, c, a + b + c
    
    return c
x =4
result = count_valid_numbers(x)
print(f"✅ Count of valid numbers (digits 1,2,3) that sum to {x}: {result}")