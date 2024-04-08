import time
from datetime import datetime
import csv
import os
import getpass

moviesDictionary = {"1": "Jurassic Cabin", "2": "The Dark Night", "3": "The Nightmare on First Street",
"4": "Quantum Mania", "5": "The Game of Thorns", "6": "The Shape of Time"}
inputMovieChoice = None  #several variables are included here as global variables defined outside of any functions and can therefore be called within any function
inputDate = None         #they may be required in. I found this was an easier fix than returning each variable and calling them along with the function they would be used in.
inputTime = None         #Many of these variables are defined as None as they are later defined by user inputs and fed into the dictionary which then writes to the csv file
globalScreenType = None
ticketType = []
inputFirstName = None
inputSurname = None
inputContactnumber = None
totalCost = None
totalTickets = None
chosenMovie = None
bookingData = []
fileName = "Booking Details.csv"

def welcomeMessage():
    #defines function for menu page, will be called from "CineVerse" file

    print("""
-----------------------------------
-----------------------------------
          
        Welcome to Cineverse!
          
-----------------------------------
-----------------------------------
          """)
    
    time.sleep(2) #Imports sleep function to delay between welcome message and main menu
    mainmenu()

def mainmenu():
    
    menuSelection = input("""   
                               
-----------------------------------
                               
             Main Menu
                               
-----------------------------------
                               
1.) Purchase Tickets

2.) Admin Access

3.) Exit

Please make a selection: """) #defines which menu the user will navigate to, calls function to display each menu
    
    if menuSelection == "1":
        movieSelection()      #movieSelection function allows user to select which movie they want to see    
    elif menuSelection == "2":
        adminAccess()         #takes the user to the admin screen where they can login and view previous bookings
    elif menuSelection == "3":   #I found it simpler to code the number selection as a string as opposed to an integer to handle errors
                                 #otherwise the code was crashing if the user entered a string rather than an int    
        print("""
-----------------------------------
              
    Thank you for using Cineverse!
              Goodbye!

-----------------------------------              
              """)
        os._exit(0) #command to effectively end the program when the user enters "3"
    else:
        print("\nInvalid input entered")
        mainmenu()   #uses recursive error handling so if an invalid input is entered the user is greeted with an error message and reidrected
        
        
def movieSelection(): #calls initial function to select the desired movie
    global inputMovieChoice
    global moviesDictionary
    global chosenMovie
    inputMovieChoice = input("""
          
------------------------------------------------
          
               Currently Showing
          
1 - Jurassic Cabin	
          
2 - The Dark Night	
          
3 - The Nightmare on First Street	
          
4 - Quantum Mania	
          
5 - The Game of Thorns	
          
6 - The Shape of Time
          
------------------------------------------------          
                            
Please make a selection: """) 
    
    if inputMovieChoice not in moviesDictionary: #utilises the moviesDictionary, each number corresponds to a movie, if the user input matches one of these numbers it will proceed  
        print("\nInvalid input. Please select a number on screen which corresponds to your chosen film") #if not then this erorr message will be thrown and movieSeelction will be called again
        movieSelection()
    else:
        chosenMovie = moviesDictionary[inputMovieChoice]
        print("\nYou have chosen " + chosenMovie)
        movieDate() #this is the else statement for if the user enters a number which matches one that is contained within a list and prints the movie associated with said number
        
def movieDate(): #allows the user to select a desired date to view their film of choice
        global inputDate
        today = datetime.now().date() #sets the today variable to todays date
        
        inputDate = input("\nPlease enter a date you would like to view " + chosenMovie + ". Use format DD/MM/YYYY: ")
        dateFormat = "%d/%m/%Y" #declares that the dateFormat must be in DD/MM/YYYY, throws an error otherwsie
        
        try:
            chosenDate = datetime.strptime(inputDate, dateFormat).date()
            
            if chosenDate and chosenDate > today: #if the user inputted date is greater than today then the program proceeds to selecting an available time
                movieTime()
            elif chosenDate and chosenDate <= today:
                print("\nInvalid. Cannot enter today's date or a day in the past. Please enter a future date")
                movieDate() #if the user inputted date is less than, or equal to todays date an error will be thrown and movieDate is called again
        except:
            print("\nInvalid date format entered, use DD/MM/YYYY") #try/except loop uses the specified date format, if any other format is used an error is thrown and movieDate called again
            movieDate()

def movieTime(): #allows user to select a time to view their chosen movie
    global inputTime
    availableTimes = ["10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", 
"15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00",
"21:00", "21:30", "22:00", "22:00"] #defines list containing available times, all times are shown to the user and will match what is declared in this list
    inputTime = input("""
                    
See all available times below >>>

10:30   11:00   11:30   12:00   12:30   13:00   
                
13:30   14:00   14:30   15:00   15:30   16:00

16:30   17:00   17:30   18:00   18:30   19:00

19:30   20:00   21:00   21:30   22:00   22:00 

Enter your selection below as it is shown on screen, e.g 10:30
    
""")

    if len(inputTime) !=5 or inputTime[2] != ":": #declares the desired time format, must contain ":" and be 5 characters long, as below
        print("\nIncorrect time format entered, use HH:MM") 
        movieTime()
    elif inputTime not in availableTimes:
        print("\nInvalid time entered. Please select from the available showings")
        movieTime() #if the user inputs a time which is not shown above, and therefore not contained in the availableTimes list, an error is thrown
        
        
    else:
        screenType() #calls function to select the type of screen the user would like, if the inputted time is valid

def screenType():
    global globalScreenType #allows the user to select the type of screen they would like to view, also shows prices dependant on screen 
        
    screenTypeSelection = input("""

    1. 2D ------ Child -- Teenager -- Adult -- Student 
                   £4        £6        £10       £8
    2. 3D ------ Child -- Teenager -- Adult -- Student
                   £5        £7        £11       £9
    3. IMAX ---- Child -- Teenager -- Adult -- Student
                   £10       £12       £15       £13
    
    Please choose a screen type: """) 
        
    if screenTypeSelection == "1":      #user input defines which screen type is selected and writes this to a variable for later use, it also prints the chosen screen type 
        globalScreenType = "2D"
        print("\n2D Screen selected")
        ticketTypeSelection()           #once screen type has been selected and written to a variable the program advances to ticketTypeSelection
    elif screenTypeSelection == "2":
        globalScreenType = "3D"
        print("\n3D Screen selected")
        ticketTypeSelection()
    elif screenTypeSelection == "3":
        globalScreenType = "IMAX"
        print("\nIMAX Screen selected")
        ticketTypeSelection()
    else:
        print("\nIncorrect input entered. Please choose a screen type") #if anything other than the available ints are entered an error is thrown, I code these as strings to make my
        screenType()                                                    #error handling simpler as the code was crashing when strings where entered by the user 

def ticketTypeSelection(): #defines function which allows the user to specify how many tickets they would like to purchase and what type of tickets these are
    global ticketType
    
    numberOfTickets = input("\nHow many tickets would you like to purchase? ")

    if not numberOfTickets.isdigit(): #input initialised as a string but then asks if it is NOT a digit, and therefore if the user enters anything other than a number an error is thrown
        print("\nInvalid selection")
        ticketTypeSelection()

    else:
        numberOfTickets = int(numberOfTickets) #for error handling and for the if loop to work correctly if the user correctly enters a digit then numberOfTickets is converted to an int 
        
        if numberOfTickets > 0: #this initailises the numberOfTickets as 0 and then creates a list, ticketType. For the number the user enters in numberOfTickets, the if loop will 
            ticketType = []     #continue to ask which type of ticket the user would like, for each individual ticket, until they have specified a type for each ticket
            for i in range(numberOfTickets): 
                inputTicketType = input(f"""
1. Child
2. Teenager
3. Adult
4. Student

Enter your ticket type for ticket {i + 1}: """) #i + 1 will print whichever number ticket the user is currently selecting a ticket type for
                if not inputTicketType.isdigit(): #similar to numberOfTickets, inputTicketType is initilaised as a string and then an error is thrown if it is NOT a digit, then it 
                    print("\nInvalid value entered") #is converted to an int. This was simpler for error handling as the variable had to be an int for the if loop to function correctly
                    ticketTypeSelection()            #otherwise the code was crashing if the variable was initialised as an int
                else: 
                    inputTicketType = int(inputTicketType)
                if inputTicketType == 1:
                    ticketType.append("Child") #dependant on the user inputted number, the ticketType list is appended to include that type of ticket
                elif inputTicketType == 2:
                    ticketType.append("Teenager")
                elif inputTicketType == 3:
                    ticketType.append("Adult")
                elif inputTicketType == 4:
                    ticketType.append("Student")
                else:
                    print("\nInvalid choice. Please make a selection") #anything other than a valid selection will throw an error and ticketTypeSelection will be called again and reset
                    ticketTypeSelection()

            else:
                bookingInformation() #once all ticket types have been declared, and the list appended, the program advances to bookingInformation

def bookingInformation(): #function which asks the user to input contact details     
    global inputFirstName  #the following variables are also global to allow them to bee called elsewhere in the code 
    global inputSurname
    global inputContactnumber

    inputFirstName = input("\nPlease enter your first name: ")
    inputSurname = input("\nPlease enter your surname: ")
    inputContactnumber = input("\nPlease enter a contact number: ")

    if not inputContactnumber.isdigit() or len(inputContactnumber) != 11: #error handling to check the entered value is an 11 digit number, same format as a UK mobile
        print("\nInvalid contact number entered. Please enter a valid 11 digit phone number")
        bookingInformation() #shows error message and calls bookingInformation again if entered incoorrectly
    else:
        inputContactnumber = int(inputContactnumber)
        confirmationOfBooking() #proceeds to function which allows user to confirm all details

def createBookingData(): #this function serves to write all of ther user inputteed information to a dictionary which is then written to a CSV file
    global chosenMovie, inputDate, inputTime, globalScreenType, totalTickets, ticketType #see various global variables here which are all integral to returning
    global inputFirstName, inputSurname, inputContactnumber, totalCost, bookingData, fileName #the correct info
    
    bookingData = {
        "Movie": chosenMovie,
        "Date": inputDate,
        "Time": inputTime,
        "Screen Type": globalScreenType,
        "Total Tickets": totalTickets,
        "Ticket Types": ", ".join(ticketType),
        "Total Cost": f"£{totalCost:.2f}", #format function here writes the total costs in a £0.00 format eg. £99.99
        "First Name": inputFirstName,
        "Surname": inputSurname,
        "Contact Number": inputContactnumber
    }

    with open(fileName, mode="a", newline="") as file: #opens apppend function of fileName which is initialised at the beginning of the code
        fieldnames = [
            "Movie", "Date", "Time", "Screen Type", "Total Tickets", #writes new line for each field name, creating headings
            "Ticket Types", "Total Cost", "First Name", "Surname", "Contact Number" 
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames) #function to write booking in dictionary form to the file using csv.DictWriter
        if os.path.getsize(fileName) == 0: 
            writer.writeheader()
            
        writer.writerow(bookingData)

def confirmationOfBooking(): #function which follows bookingInformation
    global totalTickets
    global totalCost
    ticketPrices = {        #creates dictionary for different screen types and dictates prices depending on ticket types
        "2D": {
            "Child": 4,
            "Teenager": 6,
            "Adult": 10,
            "Student": 8
            }, 
        "3D": {
            "Child": 5,
            "Teenager": 7,
            "Adult": 11,
            "Student": 9
            },
        "IMAX": {
            "Child": 10,
            "Teenager": 12,
            "Adult": 15,
            "Student": 13,
        }
    }

    globalScreenType
    selectedScreen = ticketPrices.get(globalScreenType, {}) #determines which screen type and their prices by returning user inputted value from screenType() function
    ticketCount = {}                                        #uses this to select relevant list from ticketPrices dictionary
    totalCost = 0

    for typesOfTickets in ticketType: #typesOfTickets being a new variable to store number of different types of tickets selected by user, iterates through ticketType list
        ticketCount[typesOfTickets] = ticketCount.get(typesOfTickets, 0) + 1    #which is present in ticketTypeSelection
        totalCost += selectedScreen.get(typesOfTickets, 0) * 1.2 #works out total cost of tickets dependent on screen type and the type of ticket and adds 20% VAT

        ticketInfo = "\n".join([f"{count} x {typesOfTickets} - £{count * selectedScreen.get(typesOfTickets, 0)}" for typesOfTickets, count in ticketCount.items()])
        totalTickets = len(ticketType) #ticketInfo creates a nicely formatted display to show each ticket type selected and how many of each ticket type as well as the value
                                       #of these individual ticket types, e.g. 1 - Child - £4.00
     
    print(f"""
------------------------------------------------------
                  BOOKING CONFIRMATION

Movie - {chosenMovie}

Date - {inputDate}

Time - {inputTime}

Screen Type - {globalScreenType}

Tickets - {ticketInfo}

Total Tickets - {totalTickets}

Total Cost (+20% VAT) - £{totalCost:.2f}

Booking Details:

Name - {inputFirstName} {inputSurname}

Contact Number - {inputContactnumber}
------------------------------------------------------         
          """) #simple confirmation screen which allows the user to see all of thier chosen detaisl and confirm or cancel
    
    askforConfirmation = input("""
1. Confirm booking details

2. Cancel                               

""")
    
    if askforConfirmation == "1":
        createBookingData()
        askMoreTicketsMenu() #confirm will write the details to a CSV file and also proceed to askMoreTicketsMenu
    elif askforConfirmation == "2":
        mainmenu() #cancel returns the user to the main menu
    else:
        print("\nInvalid input entered")
        confirmationOfBooking() #error handling prevents a crash on the user enteirng something incorrectly and simply reuturns the confirmation message again

def askMoreTicketsMenu():
    time.sleep(2)

    askMoreTickets = input("""
------------------------------------------------------
         BOOKING CONFIRMED AND SAVED TO FILE
------------------------------------------------------

1. Purchase more tickets?
                        
2. Back to Main Menu?
                           
""")
    
    if askMoreTickets == "1":
        movieSelection() #allows the user to purchase more tickets by returning to the first movieSelection() function
    elif askMoreTickets == "2":
        mainmenu() #otheerwis the user is returned to the main menu
    else:
        print("\nInvalid value entered")
        askMoreTicketsMenu() #incorrect value will simply ask the user the same thing again

def adminAccess(): #defines the admin menu which will allow the user to view previous bookings 

    adminUser = "admin" #values for user and password are simply hard coded
    adminPassword = "password"
    maxLoginAttemps = 3
    loginAttempts = 0
    
    while loginAttempts < maxLoginAttemps: #while number of logins is less than 3 the user can keeep trying to enter
        
        print("""
-----------------------------
         ADMIN ACCESS
-----------------------------
""")
        
        inputAdminUser = input("User: ")
        inputAdminPassword = getpass.getpass("\nPassword: ") #getpass masks the users input in the password field so it appears invisible
        
        if inputAdminUser == adminUser and inputAdminPassword == adminPassword:
            print("\nAccess granted")
            adminMenu() #if the user inputs match the hard coded username and password then the user is sent to the adminMenu() function
        else:
            loginAttempts += 1
            print("\nIncorrect login") 
            print (f"\n{str(loginAttempts)} login attempts remaining") #incorrect attempts generate an error message and displays the current number of login attempts
            
    if loginAttempts == maxLoginAttemps: 
        print("\nMaximum number of login attempts reached") #if the maximum number of login attempts is reached then the user is returned to the main menu
        print("\nReturning to main menu")
        time.sleep(1)
        print("\n---------------------------")
        time.sleep(1)
        print("\n---------------------------")
        time.sleep(2)
        mainmenu()


def adminMenu(): #user can choose to view booking data or return to main menu
    inputAdminMenuSelection = input("""

1. View booking history

2. Back to main menu                                    

""")
    
    if inputAdminMenuSelection == "1":
        bookingHistory()
    elif inputAdminMenuSelection == "2":
        mainmenu()
    else:
        print("Invalid input entered")
        adminMenu()

def bookingHistory(): #function which reads information from previously written CSV file using csv.DictReader
    
    if os.path.exists(fileName): #opens the file in read mode
        with open(fileName, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames: #if data is present then the CSV is read and displayed in a user friendly manner
                print("\nBooking History")
                for index, row in enumerate(reader, start=1):
                    print(f"\nBooking #{index}")
                    for key, value in row.items():
                        print(f"{key}: {value}")

                
                input("\nPress any key to return to main menu")
                mainmenu() #pressing any key when viweing the data will return the user to the main menu        

            else:
                print("\nNo information currently available")
                print("\nReturning to main menu")
                time.sleep(2)
                mainmenu() #if the file is empty or not present then the user is simply returned to the main menu
    else:
        print("\nNo information currently available")

        print("\nReturning to main menu")
        time.sleep(2)
        mainmenu()