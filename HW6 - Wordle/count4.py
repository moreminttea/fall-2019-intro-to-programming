#Homework 6 Part 4
#Mindy Mohr 
#
#Word Counting Class - Find and return most frequent words

#import wordle
import string #import punctuation to strip later

#Count class-------------------------------------------------------------------------------------------------------------------------------------------------------
#The wordleFromObject function takes a Count object as input, and calls its getTopWords method.
class Count: #method to initialize any data structures, such as dictionary to hold the counts for each word, and a list of stop words
    def __init__(self):
        print("Initializing Word Counter")
        self.wordCounts={} #set the attrbute wordCounts to an empty dictionary
        self.stopWords=[] #creates empty list of stop words
        infile=open("stop_words.txt","r") #opens stop words file for reading
        for line in infile:
            line=line.strip() #strips lines of white space
            self.stopWords.append(line) #adds line to stop words dictionary
        
    def incCount(self,word): #method to add one to count for a word in dictionary; if word not yet in dictionary, add a record for the word, with a count of one.
        word=word.lower() #convert words to lowercase
        word=word.strip(string.punctuation) #strips words of punctuation
        if word=="": #do not add empty string to dictionary
            return
        if word in self.stopWords: #do not add stop words to dictionary
            return
        if word in self.wordCounts: #if word is in dictionary add 1 to count
            self.wordCounts[word]=self.wordCounts[word] + 1
        else:
            self.wordCounts[word]=1 #if word not in dictionary, add to dictionary
        return

    def lookUpCount(self,word): #method to look up the count for a word
        return self.wordCounts.get(word,0) #gets word from dictionary and returns it
    
    def getTopWords(self,num): #method to get the most frequent words out of dictionary; argument "num" indicates how many words to return.
        self.topWords=[] #creates empty list of top words
        for word,count in self.wordCounts.items(): 
            t=count,word #tuple (count,word)
            self.topWords.append((t)) #add tuple to end of empty top words list
            self.topWords.sort(reverse=True) #sort from highest to lowest count
        for i in range(num):
            return self.topWords[:10] #return top 10 words

#Main Program--------------------------------------------------------------------------------------------------------------------------------------------------------
def main(): 
    counter=Count() #Make a new counter object; the counter holds the counts for all the words
    
##    #test code for Part 1; These lines test out the methods you write in part 1. 
##    #comment this code once you have completed part 1.
##    #calls incCount function to count all the words
##    counter.incCount("Well,")
##    counter.incCount("oven")
##    counter.incCount("well")
##    counter.incCount("....'")
##    print(counter.lookUpCount("oven")) #should print 1
##    print(counter.lookUpCount("well")) #should print 2
##    print(counter.lookUpCount("pizza")) #should print 0
##    print(counter.lookUpCount("")) #should print 0
##    return

    filename = input("Enter book file:") #open the file
    infile = open(filename,"r") #read file
    # put a loop here that extracts all words and inserts each word into the counter object by calling the counter.incCount() method
    
    #for loop that extracts all words and inserts each word into counter object by calling counter.incCount() method
    for line in infile: 
        line=line.strip() #strip white space
        line_words=line.split() #split words on white space
        for words in line_words:
            counter.incCount(words) #call counter.incCount function for words
    infile.close() #close the file

##    #Test code for Part 2 and 3
##    #Comment this code once you have completed part 3.
##    #calls lookUpCount function to count all filtered words
##    print(counter.lookUpCount("alice")) #should be unchanged
##    print(counter.lookUpCount("rabbit")) #should be unchanged
##    print(counter.lookUpCount("and")) #should print 0 after filtering out stop word "and"
##    print(counter.lookUpCount("she")) #should print 0 after filtering out stop word "she"
##    return

    #Test code for Part 4 and 5
    topTen=counter.getTopWords(10) #call getTopWords function for top 10 words
    print(topTen)
    
    #Test code for Part 5
    #Import the wordle module and uncomment the call to the wordle function!
    #wordle.wordleFromObject(counter,30)

#run the main program
main()
