# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SDanh,8.7.2020,Implemented menu options 1,2,&3
# SDanh,8.8.2020,Implemented File Reading & Writing.
# SDanh,8.9.2020,User Readability improvements ('Mode' indication & table formatting)
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

fileList = open(objFile, "r")

for line in fileList.readlines():
    line.strip("\n")
    lstTemp = line.split(" ")
    dicRow = {"Task": lstTemp[0], "Priority": lstTemp[1]}
    lstTable.append(dicRow)

fileList = open(objFile, "w")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task     | Priority")
        print("========================")
        for row in lstTable:
            task = row.get('Task').strip("\n")
            priority = row.get('Priority').strip("\n")
            print('{:10s} {:4s}'.format(task, priority))
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("Adding New Item...")
        strTask = input("Task: ")
        strPriority = input("Priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("Removing Item...")
        strTask = input("Task: ")
        for row in lstTable:
            if(row.get("Task") == strTask):
                lstTable.remove(row)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Saving...")
        for row in lstTable:
            fileList.write(row.get('Task').strip("\n") + " " + row.get('Priority').strip("\n") + "\n")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Closing...")
        fileList.close()
        break  # and Exit the program
