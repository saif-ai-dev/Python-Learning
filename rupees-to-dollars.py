# Rupees to dollar converter!

def rupees_to_dollars(amount):
    dollars = amount / 85
    return dollars

# Taking user input for amount in rupees.
rupees = float(input("Enter amount in Rupees: "))
dollars = rupees_to_dollars(rupees)
print(f"Amount in dollars: $", dollars)