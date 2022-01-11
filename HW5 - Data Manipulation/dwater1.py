#Homework 5 Part 4
#Mindy Mohr #Jenny Wang
#
#Read and create "world_population_2017.tsv" dictionary 

#Define main function-----------------------------------------------------------------------------
def main():
     pops=make_pop_dict() #creates population dictionary
     filter_dw_data(pops) #filters drinking water data

#Define make_pop_dict function--------------------------------------------------------------------
def make_pop_dict(): #define make_pop_dict
    for line in infile: #for loop that reorganizes file lines
        country=line[1] #country is list of "second" column
        population=line[2] #population is list of "third" column
        
        line=line.strip() #removes white space
        (number,country,population)=line.split("\t") #split lines by tabs 

        population=population.replace(",","") #replace commas with empty strings

        print(country,population) #ignore number column
    return country,population #returns values

filename="world_population_2017.tsv"
infile=open(filename, "r") #opens file for reading
make_pop_dict() #dictionary function

#Define filter_dw_data function-------------------------------------------------------------------
def filter_dw_data(popDict): #define filter water data
     pass #ignore function

main()
