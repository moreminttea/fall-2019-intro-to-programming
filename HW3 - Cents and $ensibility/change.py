#Homework 3 Problem 1
#Mindy Mohr
#
#Optimal Change

change=input("Enter change:")
change=int(change)
if change>0 and change<100:
    print("Smallest number of coins is", (((((change//25)+((change%25)//10))+(((change%25)%10)//5))+((change%5)))))
    Quarters=change//25
    print("Quarters:", Quarters)
    
    Dimes=(change%25)//10 #change divided by 25 -> returns remainder -> remainder divided by 10
    print("Dimes:", Dimes)
    
    Nickels=((change%25)%10)//5 #change divided by 25 -> returns remainder -> remainder divided by 10 -> returns remainder -> remainder divided by 5
    print("Nickels:", Nickels)
    
    Pennies=(change%5) #change divided by 5 
    print("Pennies:", Pennies)
