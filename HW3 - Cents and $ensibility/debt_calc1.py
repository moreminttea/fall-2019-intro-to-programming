#Homework 3 Problem 4
#Mindy Mohr
#
#Debt Modeler Project 

#User Unput---------------------------------------------------------------------
initial_balance=float(input("Enter initial balance:"))
annual_ir=float(input("Enter annual % interest rate:"))
monthly_payment=float(input("Enter monthly payment:"))

#Calculations-------------------------------------------------------------------
amount=(annual_ir/12)*10 #calculates monthly interest

balance=float((((initial_balance)+(amount))-(monthly_payment)))

month=0

#Beginning Set Calculations-----------------------------------------------------
month=month+1
print("Month:", month)

formatted="${0:.2f}".format(initial_balance) #adds 2 decimal points
print("Beginning balance:", formatted)

formatted="${0:.2f}".format(amount)
print("Interest charge this month:", formatted)

formatted="${0:.2f}".format(balance)
print("Balance going forward:", formatted)

formatted="${0:.2f}".format(monthly_payment)
print("Total paid to date:", formatted)
