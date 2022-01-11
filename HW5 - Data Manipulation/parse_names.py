#Homework 5 Part 1
#Mindy Mohr #Jenny Wang
#
#Parse names

#Define get_first_last function------------------------------------------------------------------------------------------
def get_first_last(input_name): 
    if input_name.find(',')>=0: #checks user inputted name for comma; >=0 means there is a comma in the index
        last_name,first_name=input_name.split(',') #splits user inputted name at found comma in index
        return first_name.strip(' '),last_name.strip(' ') #return split values as stripped white space variables
    elif input_name.find(' ')>=0:#checks user inputted name for white space; >=0 means there is white space in the index
        first_name,last_name=input_name.split(' ') #splits user inputted name at found white space in index
        return first_name.strip(' '),last_name.strip(' ') #return split values as white space stripped variables
    else: #implies that there is no comma or white space in index
        return None, None #returns None value

#Gets first and last name from user inputted name and parses--------------------------------------------------------------
input_name=input("Enter name:") #asks for user inputted name
input_name=input_name.strip() #strips white space
first_name,last_name=get_first_last(input_name)
print(first_name,last_name)  
