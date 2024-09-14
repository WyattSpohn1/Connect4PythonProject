# Wyatt Spohn             2-15-2023
# COM S 127 Assignment 2
# Create a program that acts as a calculator or a random number generator

import random

print("Lucky Calculator!")
print()

print("By: Wyatt Spohn")
print("[COM S 127 B]")
print()

# Determine initial player choice
print("What would you like to do?")
print()
choice = input("[c]alculator, [l]ucky number, [q]uit: ")
print()

def luckyNumber(a,b):
    y = 0

    if a < b:
        y = random.randrange(a,b+1)

    else:
        y = random.randrange(b,a+1)

    return y

if choice == "c":
    ope = input("Choose an operator to use, [+], [-], [*], [/], [//], [%], [**]: ")

    if ope == "+":
        a = int(input("enter a numberical value: "))
        b = int(input("enter a numberical value: "))
        result = a+b
        print()
        print("The result of {0} {1} {2} is equal to {3}".format(a, ope, b, result))
        print()

    elif ope == "-":
        a = int(input("enter a numberical value: "))
        b = int(input("enter a numberical value: "))
        result = a-b
        print()
        print("The result of {0} {1} {2} is equal to {3}".format(a, ope, b, result))
        print()

    elif ope == "*":
        a = int(input("enter a numberical value: "))
        b = int(input("enter a numberical value: "))
        result = a*b
        print()
        print("The result of {0} {1} {2} is equal to {3}".format(a, ope, b, result))
        print()

    elif ope == "/":
        a = int(input("enter a numberical value: "))
        b = int(input("enter a numberical value: "))    
        if b == 0:
            print()
            print("sorry you cannot divide by 0")
            b = 1
        result = a/b
        print()
        print("The result of {0} {1} {2} is equal to {3}".format(a, ope, b, result))
        print()

    elif ope == "//":
        a = int(input("enter a numberical value: "))
        b = int(input("enter a numberical value: "))    
        if b == 0:            
            print()
            print("sorry you cannot divide by 0")
            b = 1
        result = a//b
        print()
        print("The result of {0} {1} {2} is equal to {3}".format(a, ope, b, result))
        print()

    elif ope == "%":
        a = int(input("enter a numberical value: "))
        b = int(input("enter a numberical value: "))    
        if b == 0:           
            print()
            print("sorry you cannot divide by 0")
            b = 1
        result = a%b
        print()
        print("The result of {0} {1} {2} is equal to {3}".format(a, ope, b, result))
        print()

    elif ope == "**":
        a = int(input("enter a numberical value: "))
        b = int(input("enter a numberical value: "))    
        result = a**b
        print()
        print("The result of {0} {1} {2} is equal to {3}".format(a, ope, b, result))
        print()

    else:
        print()
        print("sorry try again")
        print()


elif choice == "l":
    a = int(input("enter a numberical value: "))
    b = int(input("enter a numberical value: "))
    c = luckyNumber(a,b)

    print("Your lucky number is {0}".format(c))


elif choice == "q":
    print()
    print("Goodbye")
    print()


else:
    print()
    print("Error choose either c, l, or, q")
    print()
















# initial choice tasks (1 pt.) ----------------------------------------------------------------------------------------------------------------
# TODO: Use conditional logic to determine which function of the Magic 9 Ball to use: [c]alculator, [l]ucky number, [q]uit
#       - Create a section of code that executes if the user enters 'c' as their initial choice
#       - Create a section of code that executes if the user enters 'l' as their initial choice
#       - Create a section of code that executes if the user enters 'q' as their initial choice
# TODO: Add another section of code where if the user does not enter "c", "l", or "q" in their initial choice, the script will print out an 
#       error message stating: 
#       print("ERROR: I did not understand your input... Please try again...") or something similar (use your imagination)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'c' option tasks (3 pts.) -------------------------------------------------------------------------------------------------------------------
# TODO: Inside the 'c' option, take in input from the user for one of seven calculations: [+], [-], [*], [/], [//], [%], [**]
# TODO: Depending on the input from the calculation choice step above, use conditional logic to determine which calculation to perform
# TODO: If the user does not enter "+", "-", "*", "/", "//", "%", or "**" in their calculation choice, print out an error message stating: 
#       print("ERROR: You must enter either \"+\", \"-\", \"*\", \"/\", \"//\", \"%\", or \"**\"") or something similar (use your imagination)
# TODO: Program a function that takes in input for the left and right hand terms of the chosen operation, converts this input to the integer 
#       type, and then returns these two integer values. Use a generic prompt for the input such as input("Please Enter An Integer: ")
# TODO: In each condition for each type of calculation, call previously created input function, and return both values to variables
# TODO: Program a function for each calculation type which takes parameters for the left hand side and right hand side
#       of the operator
# TODO: For your /, //, and % functions, use conditional logic to check if the right hand side of the expression is zero (0) and print an error 
#       if it is. In this case, change the right hand side term from zero (0) to one (1), and perform the operation as it would normally be done
# TODO: Pass in the left/ right term variables, found earlier, as arguments to each function, perform the calculation, then returns the 
#       result to a new variable
# TODO: Print the contents of the variable that was assigned the value of your function return with a message like:
#       print("The result of your calculation was: {0}".format(answer))
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'l' option tasks (1 pt.) --------------------------------------------------------------------------------------------------------------------
# TODO: Call the input function created in the 'c' option tasks, and return its output to a pair of variables
# TODO: Create a new function, called 'luckyNumber,' which takes the two previous variables, here called 'a' and 'b,' as input
# TODO: Assign the output of the 'luckyNumber' function to a variable
# TODO: Inside the luckyNumber function, initialize a 'return value variable' to zero (0)
# TODO: After the 'return value variable,' implement the following conditional logic:
#       - if 'a' is less than 'b,' asign a random value between the range of 'a' and 'b + 1' to the 'return value variable'
#       - else, return a random value between the range of 'b' and 'a + 1' to the 'return value variable'
# TODO: Once the 'return value variable' has been assigned its value, return it at the end of the function
# TODO: Back inside the 'l' section of the code, after the 'luckyNumber' function has been called and has returned its value,
#       print a fun message to the user with their 'lucky number,' such as: print("Your lucky number is: {0}".format(answer))
#       (use your imagination)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'q' option tasks (1 pt.) --------------------------------------------------------------------------------------------------------------------
# TODO: Inside the 'q' option, print out a message stating print("Maybe next time..."), or print("Goodbye!"), or something else to that effect 
#       (use your imagination)
# ---------------------------------------------------------------------------------------------------------------------------------------------