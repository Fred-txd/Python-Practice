# Ask user to input 2 values and store then in variable num1, num2
num1, num2, = input('Enter values:').split()

# Convert the strings to integers
num1 = int(num1)
num2 = int(num2)
# Add entered values and store in sum
sum = num1 + num2

# Subtract values and store in difference
differance = num1 - num2

# Multiply values and store in product
product = num1 * num2

# Divide values and store in quotient
quotient = num1 / num2

# Use modulus on values to find remainder
remainder = num1 % num2

# Print results for user
print('Sum of {} and {}: {}'.format(num1, num2, sum))
print('Difference of {} and {}: {}'.format(num1, num2, differance))
print('Product of {} and {}: {}'.format(num1, num2, product))
print('Quotient of {} and {}: {}'.format(num1, num2, quotient))
print('Remainder of {} and {}: {}'.format(num1, num2, remainder))