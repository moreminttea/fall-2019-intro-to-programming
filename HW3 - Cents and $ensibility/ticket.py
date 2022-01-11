#Homework 3 Problem 2
#Mindy Mohr
#
#Computes price of a Monterey Bay Aquarium ticket

age=input("Enter age:")
age=int(age)
if age<3:
    print("Price: FREE") 
elif age>=3 and age<=12:
    print("Price: $29.95") #child price
elif age>=13 and age<=17:
    print("Price: $39.95") #student price
elif age>=65:
    print("Price: $39.95") #senior price
else:
    college_id=input("College ID? (y/n)") #ask for college ID if in adult category
    if college_id=="y":
        print("Price: $39.95")
    elif college_id=="n":
        print("Price: $49.95") #adult price
