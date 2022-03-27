
# Define large_power function

def large_power(base, exponent):

  # Create the equation that raises the base to the exponent

  base_exponent = base ** exponent

  # Write the if function that shows whether the base_exponent is great or lesser than 5000

  if base_exponent > 5000:
    return True
  if base_exponent <= 5000:
    return False

print(large_power(5000, 2))
print("")
print(large_power(5000, 1))