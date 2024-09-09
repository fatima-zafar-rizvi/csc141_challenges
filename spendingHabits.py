# Fatima Rizvi
# Date: 09/08/24 
# This is the starter file for CSC141 lab day 4.

PA_TAX = 0.06
PRICE_OF_MEAL = 12.49

# Calculations:

tax_per_meal = (PA_TAX * PRICE_OF_MEAL)
total_without_tax = (PRICE_OF_MEAL * 5)
total_with_tax = (total_without_tax + (tax_per_meal) * 5)

print("| Lunch Spending Habits |")
print("-------------------------")
print(f"Tax per meal: {tax_per_meal}")
print(f"Total without tax: {total_without_tax}")
print(f"Total with tax: {total_with_tax}")
print("-------------------------")