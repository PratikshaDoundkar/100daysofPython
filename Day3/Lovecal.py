"""You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number"""


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
fname=name1.lower()+name2.lower()
T=fname.count("t")
R=fname.count("r")
U=fname.count("u")
E=fname.count("e")

L=fname.count("l")
O=fname.count("o")
V=fname.count("v")
EE=fname.count("e")
sum1=T+R+U+E
sum2=L+O+V+EE
score=int(str(sum1)+str(sum2))
print(score)
if (score<10) or (score>90) :
    print(f"your score is {score} , you go together like coke and mentos")
elif score>40 and score<50:
    print(f"Your score is {score}, you're alright together")
else:
    print(f"your score is {score}")

