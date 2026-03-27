itemName = input("Enter the item name: ")
itemAmout = int(input("Enter the item amount: "))

if itemAmout < 3000:
    category = "food"
elif itemAmout < 20000:
    category = "etertainment"
elif itemAmout < 10000:
    category = "transportation"
else:
    category = "major expenses"

print(f"The item {itemName} is categorized as {category}.")