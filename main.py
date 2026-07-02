# EXPENSE TRACKER APP PROJECT

# Question|Problem Statement:

# Create a Console-based Expense Tracker program in Python that allows the user to record daily expenses and view Summaries like total spending. Use only
# the concepts learned till chapter 6.


# -Project Details :→
# You are required to build a simple personal management tool.

# The program should allow the user to :
# • Add an expense with details like date, category, description and amount.
# • View all recorded expense in a clean format.
# • Calculate total spending so far.
# • Exit the program gracefully when the user chooses to.

# ✓ All tasks must be implemented using loops, if-else, lists and dictionaries only. No user-defined functions or file handling should be used.


expensesList =[]  #list of expenses in form of dictionary

print("\n\n🌝 !!...WELCOME TO EXPENSE TRACKER...!! 🌝\n")

while True:
    print("""
            ╔══════════════════════════════╗
            ║          MAIN MENU           ║
            ╠══════════════════════════════╣
            ║  1. Add Expense              ║
            ║  2. View all Expense         ║
            ║  3. View total Expense       ║
            ║  4. Exit                     ║
            ╚══════════════════════════════╝
            """)
    choice = int(input("Please enter your choice : "))

# Add Expense
    if(choice == 1):

        date = input("Enter a expense date in form of (DD-MM-YYYY) : ")
        category = input("Enter the category (Food, Travel, Shopping, Study, Other) : ")
        description = input("Enter a short description : ")
        amount = float(input("Enter the amount in form of INR(₹) : "))

        expense= {
            "Date " : date,
            "Category " : category,
            "Description " : description,
            "Amount " : amount
        }

        expensesList.append(expense)

        print("\n💸💵...YOUR EXPENSE IS ADDED SUCCESFULLY...💵💸\n")

# View all Expense 
    elif(choice == 2):

        if(len(expensesList)==0):
            print("\n 💸...NO EXPENSE ADDED...💸")
        else:
            print("\n ::--- ALL EXPENSES ---::\n\n")
            count= 1

            for eachcost in expensesList:

                print(f"Expense Number {count} --> {eachcost["Date "]}, {eachcost["Category "]},{eachcost["Description "]},{eachcost["Amount "]} ")

                count = count + 1

# View Total Expense 

    elif(choice == 3 ):
        total = 0
        for eachcost in expensesList:
            total = total + eachcost["Amount "]

        print(" \n:--TOTAL EXPENSES IS--: \n\n",total)
        
# Exit

    elif(choice == 4):
        print("""
                     THANK YOU FOR USING OUR    
                         EXPENSE TRACKER        
                            GOODBYE!            """)
        
        break

    else:
        print("""
                        __INVALID CHOICE__      
                          --TRY AGAIN--            """)
        

#  SUCCESSFULLY THE CODE IS RUNNING AND AL THE WORK SUCCESSFULLY DONE :) HAPPY LEARNING 