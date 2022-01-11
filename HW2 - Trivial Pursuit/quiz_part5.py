#Homework 2 Trivial Pursuit
#Mindy Mohr

x=0
print("ART AND LITERATURE: Who painted Starry Night?")
print("a. Vincent van Gogh")
print("b. Michelangelo")
print("c. Leonardo da Vinci")
choice=input("Enter your choice:")
if choice == "a": 
    print("Correct!")
    x=x+1
if choice != "a": 
    print("The correct answer was a") 
    x=x+0

print("ENTERTAINMENT: How many oscars did Alfred Hitchcock win?")
print("a. None")
print("b. One")
print("c. Two")
choice=input("Enter your choice:")
if choice == "a": 
    print("Correct!")
    x=x+1
if choice != "a": 
    print("The correct answer was a")
    x=x+0

print("GEOGRAPHY: Which is the largest ocean?")
print("a. Pacific")
print("b. Atlantic")
print("c. Indian")
choice=input("Enter your choice:")
if choice == "a": 
    print("Correct!")
    x=x+1
if choice != "a": 
    print("The correct answer was a")
    x=x+0


print("HISTORY: Who was the first U.S. president to appear on a coin?")
print("a. Washington")
print("b. Lincoln")
print("c. Jefferson")
choice=input("Enter your choice:")
if choice == "b": 
    print("Correct!")
    x=x+1
if choice != "b": 
    print("The correct answer was b")
    x=x+0


print("SCIENCE AND NATURE: Can pigs swim?")
print("a. Yes")
print("b. No")
print("c. Only in salt water")
choice=input("Enter your choice:")
if choice == "a": 
    print("Correct!")
    x=x+1
if choice != "a": 
    print("The correct answer was a")
    x=x+0


print("SPORT AND LEISURE: What color is the middle Olympic ring?")
print("a. Red")
print("b. Blue")
print("c. Black")
choice=input("Enter your choice:")
if choice == "c": 
    print("Correct!")
    x=x+1
if choice != "c": 
    print("The correct answer was c")
    x=x+0


print("GENIUS: What is D divided by X?")
answer=input("Enter your answer:")
if answer == "L" or answer == "50": 
    print("Correct!")
    x=x+1
else:
    print("Correct answers were L or 50")
    x=x+0

print("Your final score is", x)

if x>=0 and x<=2:
    print("You were unlucky!")
if x>=3 and x<=4:
    print("You did better than chance!")
if x>=5 and x<=6:
    print("You are a trivia star!")
if x==7:
    print("Genius!")
