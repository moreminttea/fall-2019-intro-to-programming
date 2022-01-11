#Homework 3 Problem 5
#Mindy Mohr #Jenny Wang
#
#Debt Modeler Project

#User Unput---------------------------------------------------------------------
initial_balance=float(input("Enter initial balance:"))
annual_ir=float(input("Enter annual % interest rate:"))
monthly_payment=float(input("Enter monthly payment:"))

#Calculations-------------------------------------------------------------------
amount=initial_balance*((annual_ir/100)/12) #calculates monthly interest

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


#Loop---------------------------------------------------------------------------
while balance >0:

    if balance<monthly_payment:
        monthly_payment=(initial_balance)+(amount)
        formatted="${0:.2f}".format(monthly_payment)
    
    month=month+1
    print("Month:", month)

    initial_balance=balance #"balance going forward" is now "beginning balance"
    formatted="${0:.2f}".format(initial_balance) 
    print("Beginning balance:", formatted)

    amount=balance*((annual_ir/100)/12) #calculate new ir every month
    formatted="${0:.2f}".format(amount)
    print("Interest charge this month:", formatted)

    if balance>0 and balance<monthly_payment:
        monthly_payment=(initial_balance)+(amount)
        formatted="${0:.2f}".format(monthly_payment)
        
    balance=float((((initial_balance)+(amount))-(monthly_payment)))
    formatted="${0:.2f}".format(balance)
    print("Balance going forward:", formatted)

    if balance==0:
        break

#End loop when balance going forward is $0---------------------------------------
    total=monthly_payment+(monthly_payment*(month-1)) #consistent monthly payment
    formatted="${0:.2f}".format(total)
    print("Total paid to date:", formatted)

#New total paid to date----------------------------------------------------------
while balance==0:
    total=total+monthly_payment #beginning balance+ir left when < monthly payment
    formatted="${0:.2f}".format(total)
    print("Total paid to date:", formatted)
    break
