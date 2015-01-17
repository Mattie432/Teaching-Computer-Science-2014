#Imports
from random import randint
from operator import add, sub, mul
import random

#Globals
numOfQuestions = 10

def generateQuestion(questionNumber):
    #generate two random numbers between min & max
    minNum = 1
    maxNum = 12
    randNum1 = randint(minNum,maxNum)
    randNum2 = randint(minNum,maxNum)

    #Pick a random operator
    ops = (add, sub, mul)
    op = random.choice(ops)

    #Convert the operator to a string for use when printing.
    if op == add:
        opStr = "+"
    elif op == sub:
        opStr = "-"
    elif op == mul:
        opStr = "*"

    #Calculate the answer.
    ans = op(randNum1, randNum2)

    #Print the questions
    print "Question [",questionNumber,"]"
    print randNum1,opStr,randNum2

    #Ask the use for the answer.
    ansUsr = ""
    while not ansUsr.isdigit() and (not (ansUsr.startswith('-') and ansUsr[1:].isdigit())) :
        ansUsr = raw_input("Please enter your Answer: ")
    #Change input into a number
    ansUsr = int(ansUsr.strip())

    #Check the answer
    correctAnswer = ans == ansUsr

    #Print if the answer was correct
    if correctAnswer:
        print "Correct! \n"
    else:
        print "Incorrect, answer was",ans,"\n"

    #Returns true if the answer was correct.
    return correctAnswer

def askForName():
    #Get global variable
    global numOfQuestions

    #Initial request for the users name.
    str = raw_input("Please enter your name: ")

    #Pause until the user is ready.
    print "\n","Hello",str,"there will be",numOfQuestions, "questions to follow for you to answer."
    raw_input("Are you ready to start? : ")
    print "\n___________________________________________________________________\n"

def main():
    #Variable to count the correct answers
    count = 0

    #Preamble to start the progran
    askForName()

    #Ask the number of questions.
    for i in range(1,numOfQuestions + 1):
        #If the answer was correct increase the count variable
        if generateQuestion(i):
            count = count + 1

    #Print the number of correct answers
    print "\nYou got",count,"/",numOfQuestions,"correct!\n"

#Used so that if imported as a module main is not instantly called.
if __name__ == "__main__":
    main()
