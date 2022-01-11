#Homework 4 Part 0
#Mindy Mohr #Jenny Wang
#
#Gather statistics by reading user inputted file (nums.txt)

#Set Values------------------------------------------------------------------------
count=0
sum=0 
max=None #marked as empty with None
min=None #marked as empty with None

#User input------------------------------------------------------------------------
infile_name=input("Enter filename:") 
infile=open(infile_name) #opens user inputted file

#For loop that reads user inputted file (nums.txt)---------------------------------
for line in infile:
    sum=sum+float(line) #convert string to floating point
    count=count+1

    #can't compare number to None
    #but or operator will return True without evaluating right if left is True
    
    if max==None or max<line: #if first value, it is max; if not, update so <line
        max=line 
    if min==None or min>line: #if first value, it is min; if not, update so >line
        min=line

#Outputs---------------------------------------------------------------------------
if count > 0: #this protects against dividing by zero
    print("Count",count)
    print("Sum",sum)
    print("Max",max.strip()) #strips white space
    print("Min",min.strip()) #strips white space
    ave=(sum)/(count)
    print("Ave",ave)
