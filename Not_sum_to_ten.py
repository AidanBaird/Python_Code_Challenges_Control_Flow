# Create a function that returns True if num1 + num2 are NOT equal to 10 and True else

def not_sum_to_ten(num1, num2):
  if not (num1 + num2) == 10:
    return True
  else:
    return False

print(not_sum_to_ten(10,0))
print("")
print(not_sum_to_ten(10, 1))