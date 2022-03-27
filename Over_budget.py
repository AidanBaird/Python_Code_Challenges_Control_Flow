# Define a function that gives you a true or false out put depending on whether you go over your budget

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):

  # Using an if statement that compares you budget to the sum of your expenses

  if (budget < food_bill + electricity_bill + internet_bill + rent):

    # Returning True if you have gone over budget and false otherwise/ else

    return True
  else:
    return False

# Should return False

print(over_budget(100, 0, 0, 0, 0))
print("")
# Should return True

print(over_budget(100, 101, 0, 0, 0))