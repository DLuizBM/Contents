print("Enter a number.")

num1 = float(input('\n'))

# Using "num" (only), there is an error.

if num1 > 0:
    print(f"The square root is {num1**(1/2)}.")
else:
    print("Invalid number.")
