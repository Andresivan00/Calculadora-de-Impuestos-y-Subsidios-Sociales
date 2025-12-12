# =================================================
# GENERAL DESCRIPTION
# This program determines whether a person must pay income tax,
# how much they must pay, and whether they qualify for government subsidies based on:
# - Monthly income
# - Age (benefits for those over 60 and 65)
# - Number of dependents
# Based on simplified Colombian tax rules.
# =================================================

# =================================================
# PART 1: User input data
# =================================================
full_name = input("Enter your full name: ")                                  # Person's name
age = int(input("How old are you?: "))                                       # Age (important for discounts)
monthly_income = int(input("What is your monthly income?: "))                # Monthly salary in pesos
number_of_dependents = int(input("How many dependents do you have?: "))      # Children, parents, etc.

# =================================================
# PART 2: Initialization of result variables
# =================================================
subsidy = ""                      # Subsidy received? → "Yes" or "No"
tax_rate_str = ""                 # Percentage as text: "10%", "20%", etc.
tax_rate_value = 0.0              # Percentage as decimal: 0.1, 0.2, etc.
tax_amount = 0.0                  # Amount of tax to be paid in pesos

# =================================================
# PART 3: Main logic – Determine subsidy and tax
# =================================================
# Rules based on income, age, and dependents

if (monthly_income < 3000000 and number_of_dependents >= 1) or (age > 65 and monthly_income < 4000000):
    # Special case: subsidy for low-income families or elderly people
    subsidy = "Yes"
    tax_rate_str = "0%"
    tax_rate_value = 0

elif 2000000 <= monthly_income <= 4000000 and age < 60:
    # Lower-middle range, under 60 → 10%
    subsidy = "No"
    tax_rate_str = "10%"
    tax_rate_value = 0.1

elif 2000000 <= monthly_income <= 4000000 and age >= 60:
    # Same range but over 60 → still 10% (no discount here, can be improved)
    subsidy = "No"
    tax_rate_str = "10%"
    tax_rate_value = 0.1

elif 4000001 <= monthly_income <= 6000000 and age < 60:
    # Upper-middle range, under 60 → 20%
    subsidy = "No"
    tax_rate_str = "20%"
    tax_rate_value = 0.2

elif 4000001 <= monthly_income <= 6000000 and age >= 60:
    # Same range but over 60 → 15% (age discount)
    subsidy = "No"
    tax_rate_str = "15%"
    tax_rate_value = 0.15

elif monthly_income > 6000000 and age < 60:
    # High income, under 60 → 30%
    subsidy = "No"
    tax_rate_str = "30%"
    tax_rate_value = 0.3

elif monthly_income > 6000000 and age >= 60:
    # High income, over 60 → 25% (age discount)
    subsidy = "No"
    tax_rate_str = "25%"
    tax_rate_value = 0.25

# =================================================
# PART 4: Calculation of the exact tax amount in pesos
# =================================================
tax_amount = int(monthly_income * tax_rate_value)  # Example: 5,000,000 * 0.2 = 1,000,000

# =================================================
# PART 5: Display final result to the user
# =================================================
print(f"\nGood morning Mr/Ms {full_name}, you are {age} years old, your monthly income is ${monthly_income:,}, and you have {number_of_dependents} dependents.")
print(f"A tax rate of {tax_rate_str} was applied, resulting in a tax payment of ${tax_amount:,}.")
print(f"You were {subsidy.lower()} eligible for social benefits.")
