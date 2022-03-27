# Create a function that returns true if num1 is greater that the equation of num2 double (num4)

def twice_as_large(num1, num2):

  # Create equation doubling num2 to get num4

  num4 = num2 * 2

  # Create if statement that outputs False if num1 is greater than num4 or True if else

  if num1 > num4:
    return True
  else:
    return False



print(twice_as_large(10,4))
print("")
print(twice_as_large(1, 2))