#Homework 6 Part 1
#Mindy Mohr 
#Worked on during discussion session
#Word Counting Class - Creating dictionary with methods

#import wordle
import string #import punctuation to strip later

#Count class-------------------------------------------------------------------------------------------------------------------------------------------------------
#The wordleFromObject function takes a Count object as input, and calls its getTopWords method.
class Count: #method to initialize any data structures, such as dictionary to hold the counts for each word, and a list of stop words
    def __init__(self):
        print("Initializing Word Counter")
        self.wordCounts={} #set the attrbute wordCounts to an empty dictionary
        
    def incCount(self,word): #method to add one to count for a word in dictionary; if word not yet in dictionary, add a record for the word, with a count of one.
        word=word.lower() #convert words to lowercase
        word=word.strip(string.punctuation) #strips words of punctuation
        if word=="": #do not add empty string to dictionary
            return
        if word in self.wordCounts: #if word is in dictionary add 1 to count
            self.wordCounts[word]=self.wordCounts[word] + 1
        else: 
            self.wordCounts[word]=1 #if word not in dictionary, add to dictionary
        return

    def lookUpCount(self,word): #method to look up the count for a word
        return self.wordCounts.get(word,0) #gets word from dictionary and returns it
    
    def getTopWords(self,num): #method to get the most frequent words out of dictionary; argument "num" indicates how many words to return.
        pass

#Main Program--------------------------------------------------------------------------------------------------------------------------------------------------------
def main(): 
    counter = Count() #make a new counter object; the counter holds the counts for all the words
    
    #test code for Part 1; These lines test out the methods you write in part 1. 
    #comment this code once you have completed part 1.
    #calls incCount function to count all the words
    counter.incCount("Well,") 
    counter.incCount("oven")
    counter.incCount("well")
    counter.incCount("....'")
    print(counter.lookUpCount("oven")) #should print 1
    print(counter.lookUpCount("well")) #should print 2
    print(counter.lookUpCount("pizza")) #should print 0
    print(counter.lookUpCount("")) #should print 0
    return

    filename = input("Enter book file:") #open the file
    infile = open(filename,"r") #read file

    #put a loop here that extracts all words and inserts each word into the counter object by calling the counter.incCount() method
    for line in infile:
        continue #replace this
    infile.close() #close the file

    # Test code for Part 2 and 3
    # Comment this code once you have completed part 3.
    print(counter.lookUpCount("alice"))
    print(counter.lookUpCount("rabbit"))
    print(counter.lookUpCount("and"))
    print(counter.lookUpCount("she"))
    return

    #Test code for Part 4 and 5
    #topTen = counter.getTopWords(10)
    #print(topTen)
    
    #Test code for Part 5
    #Import the wordle module and uncomment the call to the wordle function!
    #wordle.wordleFromObject(counter,30)

#run the main program
main()
