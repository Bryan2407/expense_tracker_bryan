def expensetracker():
    print("============Expenses Tracker menu============")
    print("1.add expense")
    print("2.view expenses")
    print("3.quit")
 
expensetracker() #call the function to display the menu

expense = [] #list of lists to store item name and amount as a pair

#while loop to keep the program running until the user chooses to quit.

while True:
    choice = input("Enter your choice (1, 2, or 3): ")
    
    match choice:
            case "1":
                while True: #this while is to validate the item name input
                    #Code to add an expense
                    itemName = input("Enter the item name: ")
                    if itemName.isalpha():
                        break
                    else:
                        print("invalid item name, please enter a valid name")

                itemAmount = float(input("Enter the item amount: "))
                print("expense added")
                expense.append([ itemName, itemAmount])#add the item name and amount to the expense list

            case "2":
                #Code to view expenses
                if not expense:
                     print ("no expense to view")
                else:
                     for item in expense:
                          print(item)
                          
            case "3":
                print("Quitting the program. Goodbye!")
                break
         
            case _:
                print("invalid choice")
