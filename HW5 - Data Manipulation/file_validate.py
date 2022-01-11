#Homework 5 Part 3
#Mindy Mohr #Jenny Wang
#
#Validate file

#Define open_user_file function----------------------------------------------------------------
def open_user_file(): 
    while True: #while loop that checks for valid file
        infile=input("Enter filename:") #asks for user inputted file
        try: #tests loop
            open(infile) #opens user inputted file
            break #if it is a valid file and it opens, then break from loop
        except: #if it is not a valid file, except prevents timeout error if can't find file
            print("Could not open",infile)

while True:
    open(open_user_file()) #opens open_user_file function
