# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <YOUR NAME HERE>,<DATE>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #
# https://www.geeksforgeeks.org/python-removing-dictionary-from-list-of-dictionaries/
import json
# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open("ToDoList.txt", 'r', encoding='utf-8')
for row in objFile:
    lstRow = row.split(",")  # Returns a list!
    dicRow = {"item": lstRow[0], "value": lstRow[1].strip()}
    lstTable.append(dicRow)
    # print(lstRow[0] + '|' + lstRow[1].strip())
    print(dicRow)



# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):  ## Show Current Data
        # TODO: Add Code Here
        for l in lstTable:
            print(l)
        # print(lstTable)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):  ## Add new item
        # TODO: Add Code Here
        strUserInputItem = input("\tPlease enter an item name (e.g. fork) :").lower()
        strUserInputPrice = input("\tPlease enter that item's price (e.g. $1.99):").lower()
        dicRow = {"item": strUserInputItem, "value": strUserInputPrice}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):  ## Remove an item
        # TODO: Add Code Here
        # using del + loop
        # to delete dictionary in list
        strUserInputDeleteItem = input("\tPlease enter an item name to delete:").lower()
        for i in range(len(lstTable)):
            if lstTable[i]['item'] == strUserInputDeleteItem:
                del lstTable[i]
                # break

        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):  ## Save Data to file
        # TODO: Add Code Here
## Json
        # objFile = open("ToDoList.txt", 'a', encoding='utf-8')
        # for dic in lstTable:
        #     json.dump(dic, objFile)
        #     objFile.write("\n")
        # objFile.close()
## For Loop
        for row in lstTable:
            objFile = open("ToDoList.txt", 'a', encoding='utf-8')
            objFile.write('{item_value},{price_value}\n'.format(item_value=row['item'], price_value=row['value']))
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):  ## Exit program
        # TODO: Add Code Here
        break  # and Exit the program
