#Homework 4 Part 1
#Mindy Mohr #Jenny Wang
#
#Reads user inputted file (Temperature anomaly)


#User input---------------------------------------------------------
infile_name=input("Temperature anomaly filename:")
infile=open(infile_name) #opens file
infile.readline() #reads lines of user inputted file

#For loop that reads user inputted file-----------------------------
n=0 #first line
for line in infile:
    if n<=3: #program will read but ignore first 5 lines 
        n=n+1
        continue
    line=line.strip() #removes white space from right side
    (year,temp)=line.split(',') #removes commas
    temp=float(temp) #convert to float pt; gets rid of trailing 0s

#Outputs-------------------------------------------------------------
    print(year,temp)
