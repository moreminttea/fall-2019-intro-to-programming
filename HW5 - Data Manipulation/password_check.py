#Homework 5 Part 2
#Mindy Mohr #Jenny Wang
#
#Password check

#Define password_strength function---------------------------------------------------------------------------------------------------------------------------------
def password_strength(password): #defines password_strength
    if len(password)<8:#password character count >=8 or it is weak
        return "weak"

    #set character values of 0 to keep running count of characters in password
    digit_characters=0
    lower_characters=0
    upper_characters=0
    special_characters=0
    
    for characters in password: #for loop that cycles through all the characters and checks conditions
        if characters.isdigit()==True: #checks if password has at least one digit character
            digit_characters=digit_characters+1
            
        if characters.islower()==True: #checks if password has at least one lowercase character
            lower_characters=lower_characters+1
            
        if characters.isupper()==True: #checks if password has at least one uppercase character
            upper_characters=upper_characters+1
            
        #checks if password has at least one valid special characters
        if characters.find("@")>=0: 
            special_characters=special_characters+1
        if characters.find("*")>=0: 
            special_characters=special_characters+1
        if characters.find("&")>=0: 
            special_characters=special_characters+1
        if characters.find("$")>=0: 
            special_characters=special_characters+1
        if characters.find("!")>=0: 
            special_characters=special_characters+1

    if digit_characters==0 or lower_characters==0 or upper_characters==0 or special_characters==0: #if 1 or more condition isn't approved, will return "weak"
        return "weak"
    else: #all conditions are approved so function will return "strong"
        return "strong" 
    

password=input("Enter password:") #asks for user inputted password
print("Strength is:", password_strength(password))
