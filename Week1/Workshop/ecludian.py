# Example: Finding GCD of 90, 36, and 50
# Step 1: Compute GCD(90, 36) -> 18
# Step 2: Compute GCD(18, 50) -> 2
# Final GCD = 2

a = 90
b = 36
c = 50
r = a % b  # Initialize remainder
fin_r = 1  # This will store the remainder for GCD(b, c)

while fin_r != 0:
    # Compute GCD of a and b using Euclidean algorithm
    while r != 0:
        a = b
        b = r
        r = a % b
    
    # At this point, b holds GCD(a, b)
    
    if b > c:  
        pass  # If b is already greater, do nothing
    else:
        b, c = c, b  # Swap to ensure b is always larger

    r = b % c  # Compute remainder for next GCD computation
    fin_r = r  # Update the loop condition
    if fin_r != 0:
        b = fin_r  # Update b for the next GCD iteration

print(b)  # This will print the final GCD of (90, 36, 50)
