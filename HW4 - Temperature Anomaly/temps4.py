#Homework 4 Part 4
#Mindy Mohr #Jenny Wang
#
#Writes tsv file to csv file


#User input--------------------------------------------------------------------------------------------------
infile_name=input("Temperature anomaly filename:")
infile=open(infile_name) #opens infile

outfile_name="moving_ave.csv"
outfile=open(outfile_name,"w") #opens outfile

infile.readline() #reads lines of user inputted file

#Create lists------------------------------------------------------------------------------------------------
year_list=[] #marked as empty list
temp_list=[] #marked as empty list

#For loop that reads user inputted file----------------------------------------------------------------------
n=0 #first line
for line in infile:
    if n<=3: #program will read but ignore first 5 lines 
        n=n+1
        continue
    line=line.strip() #removes white space
    (year,temp)=line.split(',') #removes commas
    temp=float(temp) #convert to float pt; gets rid of trailing 0s
    
    year_list.append(year) #add year to end of list
    temp_list.append(temp) #add temp to end of list
    
#While loop that asks for user inputted integer--------------------------------------------------------------
while True:
    num=int(input("Enter an integer between 0 and 60:")) #converts input to integer
    try: 
        if num<0 or num>60: #error
            print("Your integer is out of range")
        else:
            break
    except: #prevent timeout error if out of range
        if num>=0 and num<=60:
            i=year
            
print("Year,Value")

#Calculates moving average based on user inputted integer between years 1880-2018----------------------------
for i in range(num,len(year_list)-num,1): #start at user input; stop at last valid year; diff b/w years is 1
    moving_avg=temp_list[i-num:i+num+1] #take temp from valid years
    avg=(sum(moving_avg)/((2*num)+1)) #sum of temp list divided by (2num+1) w/ num being parameter for range
    formatted="{:.4f}".format(avg) #format avg to 4 decimal places
    print(year_list[i]+","+formatted) #print years and moving avg

outfile.close() #closes outfile
