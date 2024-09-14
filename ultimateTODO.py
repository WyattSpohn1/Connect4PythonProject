# Wyatt Spohn             4/11/23
# Assignment 5 - ultimateTODO

# TODO: Ensure that the assignment is turned in by the due date AND Ensure that the file that gets submitted is called 'ultimateTODO.py' (1 pt.)

import sys
import pickle

def initList():
    """Create a Dictionary of Lists - this is the primary data structure for the script.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def saveList(todoList):
    """Allows the user to save their data to a binary file.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    """Allows the user to load their data from a binary file.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    """This function iterates through all the keys in the dictionary, and checks each list to see if a key is present.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, String, Integer: This function returns True/ False depending on whether the item was found, the String of the keyName, and the index in the list where the item was found.
    """
    itemFound = False
    keyName = ""
    index = -1

    for k, v in todoList.items():
        for i in range(0, len(v)):
            if v[i] == item:
                itemFound = True
                keyName = k
                index = index + 1 + i

    # TODO: Iterate through all the keys in the dictionary and check each list of each key to  
    # see if an item is present. If it is, set itemFound to be 'True.' Then, set the keyName variable  
    # to the key where the item was found, and the index in the list where the item was found. 
    # If the item is not found in any of the lists in the dictionary, keep the default values above. 
    # Return the itemFound boolean, the keyName string, and the index integer (1 pt.)
    
    return itemFound, keyName, index

def addItem(item, toList, todoList):
    """This function allows the user to add an item to a specific list in the todoList data structure.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """

    itemFound, keyName, index = checkItem(item, todoList)

    if itemFound == False:

        if toList == "b":
            todoList["backlog"] = todoList["backlog"] + [item]
        elif toList == "t":
            todoList["todo"] = todoList["todo"] + [item]
        elif toList == "p":
            todoList["in_progress"] = todoList["in_progress"] + [item]    
        elif toList == "r":
            todoList["in_review"] = todoList["in_review"] + [item]
        elif toList == "d":
            todoList["done"] = todoList["done"] + [item]

    elif itemFound == True:
        print()
        print("The item {} is already in the {} list. The item has the {} value in this list.".format(item, keyName, index))

    else:
        print("error")


    # TODO: Use the checkItem function to see if the specified 'item' already exists in the dictionary
    # of lists. If the item is not in the Dictionary of Lists, add it to the list specified by the 'toList'
    # variable. If the item is already in the Dictionary of Lists, print an error message specifying:
    # - the name of the item
    # - the keyName of the list where the item is found
    # - the index of the item in the list
    # Return the todoList data structure after it has been modified (or not) (1 pt.)

    return todoList

def deleteItem(item, todoList):
    """This function allows the user to delete an item in the todoList data structure.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, Dictionary of Lists: This function returns True/ False depending on whether the item was found, and the modified Dictionary of Lists data structure.
    """

    itemFound, keyName, index = checkItem(item, todoList)

    if itemFound == False:
        print("The item {} is not in any list.".format(item))

    elif itemFound == True:
        todoList[keyName].remove(item)

    # TODO: Use the checkItem function to see if the specified 'item' already exists in the dictionary
    # of lists. If the item is already in the Dictionary of Lists, delete that item. If the item is not
    # in the Dictionary of Lists, print an error message specifying:
    # - the name of the item
    # Return the itemFound boolean and the todoList data structure after it has been modified (or not) (1 pt.)

    return itemFound, keyName, todoList

def moveItem(item, toList, todoList):
    """This function allows the user to move an item from one List in the Dictionary of Lists to another.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    
    itemFound, keyName, index = checkItem(item, todoList)
    
    if itemFound == False:
        print("The item {} is not in any list.".format(item))

    elif itemFound == True:
        todoList[keyName].remove(item)
        addItem(item, toList, todoList)
        

    # TODO: Use the deleteItem function to search for/ delete the specified item. Use the itemFound boolean
    # it returns to determine if the item was found. If it was, use the addItem function to add the item to  
    # the specified toList key.
    # Return the todoList data structure after it has been modified (or not) (1 pt.)
    
    return todoList

def printTODOList(todoList):
    """This function prints out the contents of the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return None: After printing out the contents of the Dictionary of Lists data structure, we are explicitly returning 'None.'
    """
    print()
    for k, v in todoList.items():
        print(k,":",v)
    print()

    # TODO: Iterate through all the keys in the dictionary and print both the key and the list the dictionary
    # holds for that key on a single line on the screen.
    # ex: todo: ['laundry', 'dishes']
    # Return None (1 pt.)

    return None

def runApplication(todoList):
    """This function provides the primary funcionality for the application. It allows the user to add items to the data structure, move items,
    delete items, save the data structure to a binary file, and return to the main menu.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """

    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to list, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            
            item = input("Enter an item to add: ")
            toList = input("what list would you like to add to?: [b]acklog, [t]odo, in_[p]rogress, in_[r]eview, [d]one: ")
            while toList != "b" and toList != "t" and toList != "p" and toList != "r" and toList != "d":
                print("error please enter a valid option")
                toList = input("what list would you like to add to?: ")
            addItem(item, toList, todoList)
            printTODOList(todoList)
            
            # TODO: Prompt the user to enter an item, and take in that input as a string. Call the addItem function
            # to add the item to the 'backlog' key's corresponding list. Finally, use the printTODOList function
            # to print the todoList data structure. (1 pt.)
            pass
        elif choice == "m":

            item = input("What item would you like to move?: ")
            itemFound, keyName, index = checkItem(item, todoList)
            if itemFound == False:
                print("The item {} is not in any list.".format(item))
            
            elif itemFound == True:   
                toList = input("what list would you like to move that item to?: [b]acklog, [t]odo, in_[p]rogress, in_[r]eview, [d]one: ")
                while toList != "b" and toList != "t" and toList != "p" and toList != "r" and toList != "d":
                    print("error please enter a valid option")
                    toList = input("what list would you like to add to?: ")
                moveItem(item, toList, todoList)
                printTODOList(todoList)


            # TODO: Check to see if any of the lists in the data structure have items in them. If all of the lists in
            # the dictionary are empty, print an error message that states 'No items to move!' or something similar.
            # If at least one of the lists in the dictionary has an item in it, do the following:
            # - Prompt the user to enter an item, and take in that input as a string.
            # - Use the checkItem function to confirm if that item is in the data structure.
            # - While the item is not in the data structure, print an error message stating the item does not exist
            #   and then prompt the user to enter a different item. Use the checkItem function again to confirm if 
            #   the new item is inside the data structure.
            # - Prompt the user to enter a dictionary key for the list to move the item to, and take in that input 
            #   as a string.
            # - While the dictionary key the user specifies is not a key that is in the dictionary, print an error
            #   message stating that the key does not exist. Then, prompt the user to enter a new dictionary key.
            # - call the moveItem function, passing the item, dictionary key, and todoList as arguments.
            # Finally, whether or not the data structure is totally empty or not, call the printTODOList function
            # and print out the data structure. (1 pt.)
            pass
        elif choice == "d":

            item = input("What item would you like to delete?: ")
            deleteItem(item, todoList)
            printTODOList(todoList)

            # TODO: Prompt the user to enter an item, and take in that input as a string. Call the deleteItem function
            # to remove the item from the data structure if it is present. Finally, use the printTODOList function
            # to print the todoList data structure. (1 pt.)
            # HINT: the deleteItem function returns two (2) values - do you need to do things with both of them?
            pass
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    """This is the main() function for the program. It contains all of the initial choices the user can make. These choices include:
    - Starting a new Dictionary of Lists.
    - Loading a previously saved Dictionary of Lists.
    - Quitting the script altogether.
    """
    taskOver = False

    print("The Ultimate TODO List")
    print()
    
    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: Wyatt Spohn")
    print("[COM S 127 B]")
    print()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()