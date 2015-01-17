#Imports
import os.path

def readFile():
    print "im here"

def addResult(_name,_class,_percent):
    print "Results saved:"
    print "  Name:",_name
    print "  Class:",_class
    print "  Percent:",_percent,"%"

    #Create a line to write to the file with the new result to
    #the left and 2 empty spaces e.g. "matt@100@@"
    #This will only be used if there is no existing line for this pupil
    line = _name + "@" + str(_percent) + "@" + "@" + "\n"

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
            line = _name + "@" + str(_percent) + "@" + parsedLine[1] + "@" + parsedLine[2] + "\n"

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
#e.g. "Matt@100@75@45" and returns each element in
#an array
def parseLine(line):
    #This splits the line into an array of elements.
    #This uses the special character '@' to determine where
    #one item ends and the next begins
    return line.split("@")
