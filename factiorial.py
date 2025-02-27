def functionfind(a, fact=1):
    if a < 1:
        return fact
    return functionfind(a - 1, fact * a)
print(functionfind(5))  # Output: 120
 