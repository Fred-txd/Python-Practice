# Problem: Receive miles and convert to kilometers
# Kilometers = miles * 1.60934

miles = input('Enter distance in miles:')
miles = float(miles)
kilometers = miles * 1.60934
print("{} miles equals {:.3} Kilometers".format(miles, kilometers))