#Homework 5 Part 5
#Mindy Mohr #Jenny Wang
#
#Read and create "world_population_2017.tsv" dictionary 

#Define main function---------------------------------------------------------------------------------------------------------
def main():
     pops=make_pop_dict() #creates population dictionary
     filter_dw_data(pops) #filters drinking water data

#Define make_pop_dict function------------------------------------------------------------------------------------------------
pop_dict={} #creates empty dictionary
def make_pop_dict():
     for line in pop_infile: #for loop that reorganizes file lines
          country=line[1] #country is list of "second" column
          population=line[2] #population is list of "third" column
        
          line=line.strip() #removes white space
          (number,country,population)=line.split("\t") #split lines by tabs 

          population=population.replace(",","") #replace commas with spaces
          population=int(population) #convert population to integer
          pop_dict.update({country:population}) #update dictionary so that it adds country:population
          #print(country,population) #ignore number column
     return pop_dict #return dictionary

pop_filename="world_population_2017.tsv"
pop_infile=open(pop_filename, "r") #opens file for reading
make_pop_dict() #dictionary function

#Define filter_dw_data function-----------------------------------------------------------------------------------------------
def filter_dw_data(pops):
     print("Country	1990	2010	Change")
     n=0 #keep count of lines
     for line in dw_infile: #for loop that reorganizes file lines in data file
          if n<=1: #program will read by skip first 2 lines
               n=n+1
               continue #return to beginning of for loop and skip during next iteration
          
          line=line.strip() #removes white space
          column=line.split(",") #split lines by commas
          country=column[0] #country is the list of "first" column
          if column[1]=="" or column[21]=="": #if 1990 or 2011 percentages don't exist, return to beginning and skip
               continue

          percent_change=int(column[21])-(int(column[1])) #convert values to integers and calculate change (2011% - 1990%)
          print(country, int(column[1]), int(column[21]), percent_change)
     return #return function values

dw_filename="drinking_water.csv"
dw_infile=open(dw_filename, "r") #opens file for reading

main()
