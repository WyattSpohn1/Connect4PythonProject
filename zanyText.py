# Wyatt Spohn            1/26/2023
# Assignment 1 - use input values to create a few mad libs scripts


# Parts of Speech:
# CITATION: http://www.butte.edu/departments/cas/tipsheets/grammar/parts_of_speech.html
# ACCESSED: 1-22-2023
#
# NOUN - "A noun is the name of a person, place, thing, or idea." 
#      - "man... Butte College... house... happiness"
# PRONOUN - "A pronoun is a word used in place of a noun." 
#         - "She... we... they... it"
# VERB - "A verb expresses action or being." 
#      - "jump... is... write... become"
# ADJECTIVE - "An adjective modifies or describes a noun or pronoun." 
#           - "pretty... old... blue... smart"
# ADVERB - "An adverb modifies or describes a verb, an adjective, or another adverb." 
#        - "gently... extremely... carefully... well"
# PREPOSITION - "A preposition is a word placed before a noun or pronoun to form a phrase modifying another word in the sentence." 
#             - "by... with.... about... until"
# CONJUNCTION - "A conjunction joins words, phrases, or clauses." 
#             - "and... but... or... while... because"
# INTERJECTION - "An interjection is a word used to express emotion." 
#              - "Oh!... Wow!... Oops!"

print("Zany Text!")
print()

print("By: Wyatt Spohn")
print("[COM S 127 B]")
print()

# 'Zany Text' #1
print("Zany Text #1")
print()

# Gathering input
noun1 = input("noun: ")
adjective1 = input("adjective: ")
adjective2 = input("adjective: ")
adjective3 = input("adjective: ")
verb1 = input("past tense verb: ")
noun2 = input("noun: ")
print() # Print a blank line

# Printing the final string
print("Once upon a time, there was a " + 
        noun1 + 
        ". It was a " +
        adjective1 + ", " + 
        adjective2 + ", " + 
        adjective3 + " " +
        noun1 + 
        ". And, one day it " + 
        verb1 + " " +
        "all over the " + 
        noun2 + "!")

# Print a blank line between Zany Texts
print()

#--------------------------------------------------------------------------------------------------------------------

# 'Zany Text' #2 (2 pts.)
print("Zany Text #2")
print()

# Gathering input
number1 = input("number greater than 1: ")
noun1 = input("plural noun: ")
verb1 = input("present tense ('ing') verb: ")
place1 = input("a place: ")
verb2 = input("present tense ('ing') verb: ")
verb3 = input("present tense ('ing') verb: ")

print() # Print a blank line

# Printing the final string
print("There were " + 
        number1 + " " +
        noun1 + " " +
        verb1 + " " +
        "in a " + 
        place1 + ". " + 
       "One day the " +
       noun1 + " " +
       "left the " +
       place1 +
       " in order to do new things like " +
       verb2 + " and " +
       verb3 +
       " whereever they wanted to.")

# Print a blank line between Zany Texts
print()

#--------------------------------------------------------------------------------------------------------------------


# 'Zany Text' #3 (2 pts.)
print("Zany Text #3")
print()

# Gathering input
name1 = input("a name: ")
pronoun1 = input("matching pronoun - 'he/she': ")
occupation1 = input("occupation: ")
occupation2 = input("occupation: ")
adjective1 = input("adjective: ")
adjective2 = input("adjective: ")


print() # Print a blank line

# Printing the final string
print("Once upon a time, there was a person named " + 
        name1 + ", " +
        pronoun1 + " was a " +
        occupation1 + ". " + 
        name1 + " didn't like being a " +
        occupation1 + " so " +
        pronoun1 + " decided to quit that job to fullfill a life long dream of being a " +
        occupation2 + ". " +
        name1 + " liked doing this because it was a " +
        adjective1 + " and " + adjective2 +
        " job."

    )

# Print a blank line between Zany Texts
print()

#--------------------------------------------------------------------------------------------------------------------


# 'Zany Text' #4 (2 pts.)
print("Zany Text #4")
print()

# Gathering input
animal1 = input("animal: ")
animal2 = input("animal: ")
subject1 = input("controversal subject: ")
verb1 = input("present tense verb w/o 'ing': ")
select1 = int(input("pick a number 1 or 2: "))


if select1 == 1:
        select1 = animal1
elif select1 == 2:
        select1 = animal2
else:
        select1 = "neither"


print() # Print a blank line

# Printing the final string
print("Once upon a time, there was a " + 
        animal1 + " and a " + animal2 + ". "
        "They were the best of friends, until one day the two started fighting about " +
        subject1 + ". "
        "The two fought and fought until finally they decided that the only way to settle there differences was to compete in a " +
        verb1 + "-off. It was a close match but in the end " +
        select1 + " won.")

# Print a blank line between Zany Texts
print()