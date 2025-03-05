# Expansion of (x + y)^3
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

calculation = x**3 + 3 * x**2 * y + 3 * x * y**2 + y**3
print("Result of (x + y)^3:", calculation)

# Solving Quadratic Equation: ax^2 + bx + c = 0
a = int(input("Enter a value of a: "))
b = int(input("Enter a value of b: "))
c = int(input("Enter a value of c: "))

difference = b**2 - 4 * a * c  # Discriminant

if difference > 0:
    x1 = (-b + (difference) ** (1/2)) / (2 * a)
    x2 = (-b - (difference) ** (1/2)) / (2 * a)
    print(f"Roots are real and different: x1 = {x1}, x2 = {x2}")

elif difference == 0:
    x1 = -b / (2 * a)
    print(f"Roots are real and same: x1 = x2 = {x1}")

else:
    real_num = -b / (2 * a)
    imaginary_number = (abs(difference) ** (1/2)) / (2 * a)
    print(f"Roots are complex: {real_num} + {imaginary_number}j and {real_num} - {imaginary_number}j")
