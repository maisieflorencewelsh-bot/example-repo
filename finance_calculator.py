# Program that allows the user to calculate either the interest on an investment-
# or the amount to repay on a home loan each month, depending on the user's choice.

import math

# First, explain the two options to the user and ask for their choice.

print("Welcome to the financial calculator!")

print("Please choose one of the following options:")

print("Investment - to calculate the amount of interest you'll earn on your investment")

print("Bond - to calculate the amount you'll have to pay on a home loan")

users_choice = input(" Please enter investment or bond to proceed  ")

# The command word the user inputted can be upper or lower case (or first letter uppercase) and will still work.
# If user chooses investment: 

if users_choice == "investment" or users_choice == "Investment" or users_choice == "INVESTMENT":

    # Prompt the user to input deposit amount, interest rate and number of years they plan to invest.
    
    deposit_amount = float(input("Please enter how much you would like to deposit:"))

    interest_rate = float(input("Please enter the interest rate:"))

    invest_years = float(input("How many years would you like to invest for?"))

    # Ask the user if they want the interest calculated to be simple or compound. The input to chose is S for simple or C for compound.

    interest_type = input("Do you want simple or compound interest? Type S for simple, or C for compound. ")

    #If the user chooses compound interest:

    if interest_type == "C" or interest_type == "c":

        #Divide the number of investment years by 100 to get the interest percentage rate

        interest_rate = interest_rate / 100

        # Calculate the total amount (using compound interest) of money the user would make on their deposit after the investment duration.

        total_amount = deposit_amount * math.pow((1+interest_rate), invest_years)

        # Print the total amount to the user

        print(f"The investment amount after interest is {total_amount}.")

    # If the user chooses simple interest:

    elif interest_type == "S" or interest_type == "s":
        
        #Divide the number of investment years by 100 to get the interest percentage rate

        interest_rate = interest_rate / 100

        # Calculate the total amount (using simple interest) of money the user would make on their deposit after the investment duration.

        total_amount = deposit_amount * (1 + (interest_rate * invest_years))

        # Print the total amount to the user

        print(f"The investment amount after interest is {total_amount}.")
   
# Again the command word "bond" can be upper or lower case, and still work.
# If the user chooses bond:

elif users_choice == "bond" or users_choice == "Bond" or users_choice == "BOND":

    # Prompt user to enter current house value, interest rate and how long they plan to repay.
        
    present_value = float(input(" What is the current value of the house?"))

    interest_rate = float(input("Please enter the interest rate:"))

    bond_length = float(input("How many months do you plan to repay the bond?"))

    # Divide the interest rate by 100 to get the percentage rate value

    interest_rate = interest_rate / 100

    # Divide the percentage interest rate by 12 to convert it from annual interest rate to monthly interest rate.
    # The monthly interest rate is necessary if we are to calculate how much the user will be repaying per month.

    interest_rate = interest_rate / 12

    # Calculate how much the user will have to repay each month
    
    repayment_value = (interest_rate * present_value) / (1 - (1 + interest_rate)**(-bond_length))

    # Print how much the user will have to repay each month

    print(f"Your home loan repayment will be {repayment_value} each month for {bond_length} months.")

# If the user enters anything other than "investment" or "bond", an error message will be printed.

else:

    print("Error, invalid command word entered.")
