def askForName():
    #Initial request for the users name.
    str = raw_input("Please enter your name: ")
    print "\n","Hello",str,"there will be 10 questions to follow for you to answer."
    #Pause until the user is ready.
    raw_input("Are you ready to start? : ")

#Main method to start the program.
def main():
    askForName()

#Used so that if imported as a module main is not instantly called.
if __name__ == "__main__":
    main()
