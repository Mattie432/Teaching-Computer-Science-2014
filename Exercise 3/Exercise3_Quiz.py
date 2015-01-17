#Imports
from random import randint
from operator import add, sub, mul
import random

#Globals
numOfQuestions = 10
pupilsClass = ""
pupilsName = ""

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
    global pupilsClass
    global pupilsName

    #Initial request for the users name.
    pupilsName = raw_input("Please enter your name: ")

    #Ask for the users class and validate its a number
    while not pupilsClass.isdigit():
        pupilsClass = raw_input("Please enter your class number: ")

    #Pause until the user is ready.
    print "\n","Hello", pupilsName,"there will be", numOfQuestions, "questions to follow for you to answer."
    raw_input("Are you ready to start? : ")
    print "\n___________________________________________________________________\n"

def addResult(_name,_class,_percent):
    print "Results saved:"
    print "  Name:",_name
    print "  Class:",_class
    print "  Percent:",_percent,"%"

    #Create a line to write to the file with the new result to
    #the left and 2 empty spaces e.g. "matt@100@@"
    #This will only be used if there is no existing line for this pupil
    line = _name + "@" + str(_percent) + "@" + "@" + "@" + "\n"

    #Open file for reading & appending (using the 'a+' paramater)
    #This means a blank file is created if it dosent exist
    fileIn = open("Class" + _class + ".txt", "a+")

    #Boolean for if the pupil has been found
    pupilFound = False

    #An array of the lines in the file
    linesOut = []

    #Loops through each line in the file looking for the pupils name
    for fileLine in fileIn:
        #Gets an array of the items in the line
        parsedLine = parseLine(fileLine)

        #Check if the name already exists, convert both to lowercase first
        #so that they ignore capitalisation.
        if parsedLine[0].lower() == _name.lower():
            #If the name exists already then add the new result
            #and keep the previous two (moved to the end)
            #e.g. "name @ newResult @ oldResult1 @ oldResult2"
            line = _name + "@" + str(_percent) + "@" + parsedLine[1] + "@" + parsedLine[2] + "@" + "\n"

            #add the new line to the array of lines to write
            linesOut.append(line)

            #set pupil found = True
            pupilFound = True

        else:
            #add the existing line to the array of lines to write
            linesOut.append(fileLine)

    #We are finished, close the file
    fileIn.close()

    #Check if the search found the pupil
    if not pupilFound:
        #If not found a pupil then need to add this as a new result
        linesOut.append(line)

    #Open file for writing (using the 'w' paramater)
    #This overwrites the existing file
    fileOut = open("Class" + _class + ".txt", "w")

    #Write all the lines of text to the file
    fileOut.writelines(linesOut)

    #We are finished, close the file
    fileOut.close()



#This expects a line with items separated by '@'
#e.g. "Matt@100@75@45@" and returns each element in
#an array
def parseLine(line):
    #This splits the line into an array of elements.
    #This uses the special character '@' to determine where
    #one item ends and the next begins
    return line.split("@")

def main():
    #Get global variable
    global pupilsClass
    global pupilsName

    #Variable to count the correct answers
    count = 0

    #Preamble to start the program
    askForName()

    #Ask the number of questions.
    for i in range(1,numOfQuestions + 1):
        #If the answer was correct increase the count variable
        if generateQuestion(i):
            count = count + 1

    #Print the number of correct answers
    print "\nYou got",count,"/",numOfQuestions,"correct!\n"
    percentage = float(count) / numOfQuestions * 100

    addResult(pupilsName,pupilsClass,percentage)

#Used so that if imported as a module main is not instantly called.
if __name__ == "__main__":
    main()
