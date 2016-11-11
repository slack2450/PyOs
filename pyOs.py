#pyOs by Joss Bird
import time #imports time module
import os #imports os module
class pyOs: #sets up the os class
    class main: #sets up vital scripts
        def run(): #sets up base vars
            global username #makes username global
            global password #makes password global
            global firstRun
            global version
            login = open("login.txt", "r") #imports login file
            username = login.readline().rstrip("\n") #sets username to login file line 1
            password = login.readline().rstrip("\n") #sets password to login file line 2
            firstRun = login.readline().rstrip("\n") #sets firstRun to login file line 3
            login.close() #closes login file
            version = "0.0.5"
            pyOs.main.displayInfo()
            pyOs.main.login() #runs login
        def displayInfo(): #displays specs
            print("This python window is running: pyOs!")
            print("First made on 30.09.2016")
            print("Version: "+version)
            print("Made by: Joss Bird")
        def login(): #logs in user
            while True: #creates loop
                if input("Username: ") == username: #prompts for username
                    if input("Password: ") == password: #prompts for password
                        print("Access granted") #informs them of granted access
                        break #breaks loop
                    else:
                        print("Access denied") #informs them of denied access
                else:
                    input("Password: ") #prompt for password (Note: no need to store this due to incorrect username)
                    print("Access denied") #informs them of denied access
            if firstRun == "1": #checks to see if this is the first run
                pyOs.main.changeLogin() #if so runs changeLogin
            else:
                pyOs.main.startMenu.base() #runs start menu
        def changeLogin(): #changes login
            login = open("login.txt", "w") #opens login file in write mode
            if firstRun == "1": #checks to see if it is the first run
                print("Welcome to pyOs!") #nice friendly greeting message
                print("You must change your username and password on your first login.") #informs them of the process that is about to take place
            
            while True: #creates username loop
                newUsername = input("New username: ") #creates newUsername var
                newUsernameConfirm = input("Confirm new username: ") #creates newUsernameConfirm var
                if newUsername == newUsernameConfirm: #compares the two previous vars for a match
                    print("Updating username!") #tell them of the process
                    login.write(newUsername+"\n") #writes the new username to the login file
                    global username #makes the var username global
                    username = newUsername #sets the new username to the global username var
                    while True: #creates password loop
                        newPassword = input("New password: ") #creates newPassword var
                        newPasswordConfirm = input("Confirm new password: ") #creates newPasswordConfirm var
                        if newPassword == newPasswordConfirm: #Compares the past two vars for a match
                            print("Updating Password!") #tells the user the password is being update
                            login.write(newPassword+"\n") #writes the new password to the file
                            login.write("0\n") #writes the first run status to 0
                            login.close() #closes the login file
                            global password #sets password to global
                            password = newPassword #sets the global password var to the new password
                            break #breaks the password loop
                        else: #if passwords dont match
                            print("Passwords do not match please try again.") #informs user
                    break #breaks username loop
                else: #if usernames dont match
                    print("Usernames do not match please try again.") #informs user
            print("Your username and password were updated sucessfully they are now:") #informs user of updated password
            print("Username: "+username)#shows new username
            print("Password: "+password)#shows new password
            pyOs.main.startMenu.base()#launches start menu
        def updateLog(): #Defines the updateLog Function
            pyOs.main.displayInfo() #Calls the displayInfo function
            print("""\nUpdate Log:
Version 0.0.1:
+ Added Login
+ Added Update Log
Version 0.0.2:
* Changed to a much better class organisation system
* Changed login to file system
+ Added Start Menu
+ Added Control Panel
Version 0.0.3:
+ Forced user to change login on first attempt
+ Added Log Out and Shutdown
Version 0.0.4:
* Changed Shut down
* Fixed login glitches when the user had previously logged out
+ Verification of startMenu Options
Version 0.0.5:
* Fixed spelling and grammar errors
+ Added Blue Screen Of Death
+ Added Blue Screen Of Death test
Version 0.0.6:
+ Added clearing of screen when used in command prompt
* Changed "os" class to "pyOs" to allow os module to function""")
            input("Press enter to continue...") #Forces user to achknowledge the updateLog
            pyOs.main.startMenu.base() #Calls the startMenu
        class startMenu: #Start menu class
            def base():#base of start menu
                os.system("cls")
                print("\nAvailable options:")
                print("1. Control Panel")
                print("7. Advanced")
                print("8. Log Out")
                print("9. Shut down")
                pyOs.main.startMenu.userInput("base") #calls the input of start menu with the origin of the initation of the command
            def controlPanel():#control pannel menu
                os.system("cls")
                print("\nAvailable Options:")
                print("1. ChangeLogin")
                print("9. Return")
                pyOs.main.startMenu.userInput("controlPanel") #calls the input of start menu with the origin of the initation of the command
            def advanced(): #advanced menu
                os.system("cls")
                print("\nAvailable Options:")
                print("1. Update Log")
                print("2. Blue Screen Of Death Test")
                print("9. Return")
                pyOs.main.startMenu.userInput("advanced") #calls the input of start menu with the origin of the initation of the command
            def userInput(location): #input for start menu
                option = input("Selection>")
                if location == "base":
                    if option == "1":
                        pyOs.main.startMenu.controlPanel()
                    elif option == "7":
                        pyOs.main.startMenu.advanced()
                    elif option == "8":
                        pyOs.main.login()
                    elif option == "9":
                        pyOs.main.shutDown()
                    else:
                        print("Option not recognised!")
                        print("Please try again.")
                        pyOs.main.startMenu.base()
                elif location == "controlPanel":
                    if option == "1":
                        pyOs.main.changeLogin()
                    elif option == "9":
                        pyOs.main.startMenu.base()
                    else:
                        print("Option not recognised!")
                        print("Please try again.")
                        pyOs.main.startMenu.controlPanel()
                elif location == "advanced":
                    if option == "1":
                        pyOs.main.updateLog()
                    elif option == "2":
                        pyOs.main.blueScreenOfDeath("user created test")
                    elif option == "9":
                        pyOs.main.startMenu.base()
                    else:
                        print("Option not recognised!")
                        print("Please try again.")
                        pyOs.main.startMenu.advanced()
        def shutDown(): #Shutdown function
            print("Thank you for using pyOs!") #thank you message
            print("Shutting down") #confirmation of users request
        def blueScreenOfDeath(cause):
            print("Grrrr....")
            print("You made the computer angry!")
            print("FATAL ERROR")
            print("Cause: "+cause)
            print("Creating Error log...")
            errorLog = open("errorLog.txt", "w")
            errorLog.write("pyOs ERROR LOG\n")
            errorLog.write("pyOs version: "+version+"\n")
            errorLog.write("Fatal error on: "+time.strftime("%x")+" at "+time.strftime("%X")+"\n")
            errorLog.write("Cause of error: "+cause+"\n")
            errorLog.write("Current system vairables:\n")
            errorLog.write("Username: "+username+"\n")
            errorLog.write("Password: "+password+"\n")
            errorLog.write("First Run: "+firstRun+"\n")
            errorLog.write("===END OF ERROR LOG===")
            print("Error log created.")
            pyOs.main.shutDown()
    class programs:
        def calculator():
            print("Place Holder")
            
pyOs.main.run() #starts the OS
