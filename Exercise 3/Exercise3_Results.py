#Imports
import os.path

#globals
global data

def main():
    global data

    #Ask for pupils class
    pupilClass = raw_input("Please enter the class to generate a report for: ")
    print "\n___________________________________________________________________\n\n"

    if os.path.isfile("Class" + pupilClass + ".txt"):
        #Print the table as it stored
        data = readResults(pupilClass)
        printResultsTable(data)

        #Continually loop asking to manipulte the table
        while(True):
            askToSort()
    else:
        print "ERROR: File for that class dosent exist, please try another.\n"
        main()

def readResults(pupilClass):
    #Open file for reading & appending (using the 'r' paramater)
    fileIn = open("Class" + pupilClass + ".txt", "r")

    #An array of the files parsed lines
    linesOut = []

    #Loops through each line in the file looking for the pupils name
    for fileLine in fileIn:
        #Gets an array of the items in the line
        parsedLine = parseLine(fileLine)

        #Calculate average
        avg = 0.0
        count = 0
        for i in range(1,4):
            #Check if empty value
            if parsedLine[i] != "":
                #if value is not empty
                avg = avg + float(parsedLine[i])
                count = count + 1

        #Calculate the average
        avg = avg / count

        #Append the new tuple to the lines to return
        linesOut.append((parsedLine[0],parsedLine[1],parsedLine[2],parsedLine[3],max(parsedLine[1:4]),avg))

    #return the list of lines
    return linesOut

#Expects an array of formatted lines in the form
#(name, result1, result2, result3, highest value, average)
def printResultsTable(linesIn):

    #print the headers
    print '%-20s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s' % ("Name","|","Result 1","|","Result 2","|", "Result 3","|", "Highest","|", "Average")
    print '%-20s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s' % ("--------------------","|","----------","|","----------","|", "----------","|", "----------","|", "----------")

    #loop through each line
    for linePrint in linesIn:
        #Print the row in the table with a spacing between each element to format it.
        print '%-20s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s' % (linePrint[0],"|",linePrint[1],"|",linePrint[2],"|",linePrint[3],"|",linePrint[4],"|",linePrint[5])

def askToSort():
    global data

    print "\n___________________________________________________________________\n\n"

    print "What would you like to do with the table?"
    print " [1] View pupils high scores in alphabetical order"
    print " [2] View by highest score, highest to lowest"
    print " [3] View by average score, highest to lowest"
    print
    option = int(raw_input("Enter a number: ").strip())
    print "\n"

    if option == 1:
        #alphabetical order
        data.sort(key=lambda tup: tup[0])
        print "Data sorted by name, alphabetically."
        print '%-20s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s' % ("    ^","","","","","", "","", "","", "")
        printResultsTable(data)
    elif option == 2:
        #highest score, highest to lowest
        data.sort(key=lambda tup: tup[4], reverse=True)
        print "Data sorted by highest score, highest to lowest"
        print '%-20s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s' % ("","","","","","", "","", "    v","", "")
        printResultsTable(data)
    elif option == 3:
        #average score, highest to lowest
        data.sort(key=lambda tup: tup[5], reverse=True)
        print "Data sorted by average score, highest to lowest"
        print '%-20s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s%-1s%-10s' % ("","","","","","", "","", "","", "    v")
        printResultsTable(data)
    else:
        print "Error with your selection, Please enter a valid number."

#This expects a line with items separated by '@'
#e.g. "Matt@100@75@45" and returns each element in
#an array
def parseLine(line):
    #This splits the line into an array of elements.
    #This uses the special character '@' to determine where
    #one item ends and the next begins
    return line.split("@")

#Used so that if imported as a module main is not instantly called.
if __name__ == "__main__":
    main()
