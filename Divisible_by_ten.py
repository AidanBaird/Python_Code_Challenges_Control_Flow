# Creata a function that checks the remainder after dividing a number by 10 and
# return true if the remainder is == to 0 and False if else

def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False

print(divisible_by_ten(10))
print("")
print(divisible_by_ten(11))