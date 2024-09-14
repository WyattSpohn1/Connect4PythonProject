# Wyatt Spohn             3/2/2023
# Assignment 3
# "You may play Spinner with 1 or 2 players. Both players start with 10 points and may wager as many points as they have in each round. The name of the game is to obtain the target value with the number of spinners pof your choosing. The player closest to the target value adds their wager to their points while the other gets their points subtracted from their points. The game is finished when one player has 0 points left.





import random

# NOTE: Your functions should go here!
def printTitleMaterial():
    print("Spinner Winner!")
    print()


    print("By: Wyatt Spohn")
    print("[COM S 127 B]")
    print()

def initialChoice():
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

def chooseNumPlayers():
    numPlayers = 0
    print()
    numPlayers = input("How many people are playing? 1 or 2?: ")
    while numPlayers != '1' and numPlayers != '2':
        print("ERROR: Please enter 1 or 2...")
        numPlayers = input("How many people are playing? 1 or 2?: ")
    return numPlayers

def wait():
    print()
    input("Press [Enter] To Continue...")
    print()

def printBanner():
    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()

def printPoints(playerNum, points):
    print("* Player {0} has {1} Points!".format(playerNum, points))
    print()

def wagerPointsHuman(playerNum, player1Points, player2Points):


    if playerNum == 1:
        wager = int(input("Player 1 How much would you like to wager?: "))
        while wager < 1 and wager > player1Points:
            print("ERROR: Please enter a valid wager...")
            wager = int(input("Player 1 How much would you like to wager?: "))
    
    elif playerNum == 2:
        wager = int(input("PLayer 2 How much would you like to wager?: "))
        while wager < 1 and wager > player2Points:
            print("ERROR: Please enter a valid wager...")
            wager = int(input("Player 2 How much would you like to wager?: "))

    return wager

def wagerPointsAI(playerNum, player1Points, player2Points):

    if playerNum == 1:
        wager = int(input("Player 1 How much would you like to wager?: "))

        while wager < 1 and wager > player1Points:
            print("ERROR: Please enter a valid wager...")
            wager = input("Player 1 How much would you like to wager?: ")  

    elif playerNum == 2:
        wager = random.randrange(1, player2Points+1)
        print("Player 2 How much would you like to wager?: ", wager)

    return wager

def generateTargetValue(numSpinners, spinnerLow, spinnerHigh):
    target = random.randrange((spinnerLow*numSpinners), (spinnerHigh*numSpinners)+1)
    print("The target value is ", target)
    return target

def getSpinnerChoiceHuman(playerNum, target, numSpinners, spinnerLow, spinnerHigh):

    print("The target value is ", target)

    print("A single spinner can produce a value between ", spinnerLow, " - ", spinnerHigh)

    print()

    if playerNum == 1:
        spinnerChoice = int(input("Player 1: How many spinners would you like to spin?: "))

        while spinnerChoice < 1 and spinnerChoice > numSpinners+1:
            print("ERROR: Please enter a valid option...")
            spinnerChoice = int(input("Player 1: How many spinners would you like to use?: "))
    elif playerNum == 2:
        spinnerChoice = int(input("Player 2: How many spinners would you like to spin?: "))

        while spinnerChoice < 1 and spinnerChoice > numSpinners+1:
            print("ERROR: Please enter a valid option...")
            spinnerChoice = int(input("Player 2: How many spinners would you like to use?: "))


    return spinnerChoice

def getSpinnerChoiceAI(playerNum, target, numSpinners, spinnerLow, spinnerHigh):


    print("The target value is ", target)

    print("A single spinner can produce a value between ", spinnerLow, " - ", spinnerHigh)

    print()

    if playerNum == 1:
        spinnerChoice = int(input("Player 1: How many spinners would you like to spin?: "))
        
        while spinnerChoice < 1 and spinnerChoice > numSpinners+1:
            print("ERROR: Please enter a valid option...")
            spinnerChoice = int(input("Player 1: How many spinners would you like to use?: "))

    elif playerNum == 2:

        spinrange = int(target/(spinnerLow+spinnerHigh)/2)


        spinnerChoice = random.randrange(spinrange-1, spinrange+2)

        if spinnerChoice < 1:
            spinnerChoice = 1
        elif spinnerChoice > numSpinners:
            spinnerChoice = numSpinners

        print("Player 2: How many spinners would you like to spin (1 - ", numSpinners, ")?: ", spinnerChoice)

    return spinnerChoice

def spinSpinners(playerNum, spinnerChoice, target, spinnerLow, spinnerHigh):
    spinTotal = 0
    
    if playerNum == 1:
        for i in range(0, spinnerChoice):
            spin = random.randrange(spinnerLow, spinnerHigh + 1)
            print("Player 1 has spun a ", spin)
            spinTotal = spinTotal + spin
    
    if playerNum == 2:
        for i in range(0, spinnerChoice):
            spin = random.randrange(spinnerLow, spinnerHigh + 1)
            print("Player 2 has spun a ", spin)
            spinTotal = spinTotal + spin

    print("The total value of the spinner was ", spinTotal, " and the target value was ", target)

    return spinTotal

def resetGameOptions():
    player1Points = 10
    player2Points = 10
    return player1Points, player2Points

def main():
    # main script running control variable
    running = True
    
    # gameplay variables
    SPINNER_LOW = 1
    SPINNER_HIGH = 3
    NUM_SPINNERS = 3
    player1Points = 10
    player2Points = 10

    # print the title/ author information
    printTitleMaterial()

    # play the game
    while running:
        choice = initialChoice()
        if choice == "p":
            player1Points = 10
            player2Points = 10
            numPlayers = chooseNumPlayers()

            # main game loop
            while True:
                # round setup
                printBanner()
                wait()
                
                printPoints(1, player1Points)
                printPoints(2, player2Points)

                # TODO: Complete the logic of the game (4 pts.)
                # NOTE: You can do this any way you like - in fact, you can even discard this file entirely and make your own version!
                #       The comments below provide a general outline of the overall 'algorithm' of the game
                #       Each comment could have multiple lines of code assiciated with it
                #       Your job is to iteratively build up a game that works - it doesn't really matter how you code it

                if numPlayers == '1':
                    # find a target value
                    target = generateTargetValue(NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                    wait()

                    # player 1 wager
                    wager1 = wagerPointsAI(1, player1Points, player2Points)
                    wait()
                
                    # player 2 wager
                    wager2 = wagerPointsAI(2, player1Points, player2Points)
                    wait()

                    # player 1 spin
                    spinnerchoice1 = getSpinnerChoiceAI(1, target, NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                    spintotal1 = spinSpinners(1, spinnerchoice1, target, SPINNER_LOW, SPINNER_HIGH)
                    wait()


                    # player 2 spin
                    spinnerchoice2 = getSpinnerChoiceAI(2, target, NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                    spintotal2 = spinSpinners(2, spinnerchoice2, target, SPINNER_LOW, SPINNER_HIGH)
                    wait()

                    # calculate winner
                    if (abs(spintotal1 - target)) < (abs(spintotal2 - target)): #player 1 wins
                        print("Player 1 wins this round")
                        player1Points = player1Points + wager1
                        player2Points = player2Points - wager2
                        wait()

                    elif (abs(spintotal1 - target)) > (abs(spintotal2 - target)): #player 2 wins
                        print("Player 2 wins this round")
                        player2Points = player2Points + wager2
                        player1Points = player1Points - wager1
                        wait()

                    elif (abs(spintotal1 - target)) == (abs(spintotal2 - target)): #tie
                        print("Its a tie")
                        wait()
                    

                    # print the points for both players
                    printPoints(1, player1Points)
                    printPoints(2, player2Points)
                    wait()


                    # check of the game is over - if it is, break out of the gameplay loop and resent the points to default values
                    # otherwise print that it is the end of the round
                    if player1Points == 0:
                        print("Player 2 wins the game")
                        break
                    elif player2Points == 0:
                        print("Player 1 wins this game")
                        break
       


                if numPlayers == '2':
                    # find a target value
                    target = generateTargetValue(NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                    wait()

                    # player 1 wager
                    wager1 = wagerPointsHuman(1, player1Points, player2Points)
                    wait()
                
                    # player 2 wager
                    wager2 = wagerPointsHuman(2, player1Points, player2Points)
                    wait()

                    # player 1 spin
                    spinnerchoice1 = getSpinnerChoiceHuman(1, target, NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                    spintotal1 = spinSpinners(1, spinnerchoice1, target, SPINNER_LOW, SPINNER_HIGH)
                    wait()


                    # player 2 spin
                    spinnerchoice2 = getSpinnerChoiceHuman(2, target, NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                    spintotal2 = spinSpinners(2, spinnerchoice2, target, SPINNER_LOW, SPINNER_HIGH)
                    wait()

                    # calculate winner
                    if (abs(spintotal1 - target)) < (abs(spintotal2 - target)): #player 1 wins
                        print("Player 1 wins this round")
                        player1Points = player1Points + wager1
                        player2Points = player2Points - wager2
                        wait()

                    elif (abs(spintotal1 - target)) > (abs(spintotal2 - target)): #player 2 wins
                        print("Player 2 wins this round")
                        player2Points = player2Points + wager2
                        player1Points = player1Points - wager1
                        wait()

                    elif (abs(spintotal1 - target)) == (abs(spintotal2 - target)): #tie
                        print("Its a tie")
                        wait()
                    

                    # print the points for both players
                    printPoints(1, player1Points)
                    printPoints(2, player2Points)
                    wait()


                    # check of the game is over - if it is, break out of the gameplay loop and resent the points to default values
                    # otherwise print that it is the end of the round
                    if player1Points == 0:
                        print("Player 2 wins the game")
                        print()
                        resetGameOptions()
                        break
                    elif player2Points == 0:
                        print("Player 1 wins this game")
                        print()
                        resetGameOptions()
                        break

                

        elif choice == "i":
            print()
            print("You may play Spinner with 1 or 2 players.",
                  "both players start with 10 points and may wager as many points as they have in each round. ", 
                  "The name of the game is to obtain the target value with the number of spinners pof your choosing. ", 
                  "The player closest to the target value adds their wager to their points while the other gets their points subtracted from their points. ", 
                  "The game is finished when one player has 0 points left.")
            print()
            # TODO: Print out the instructions for the game (see the rubric for details) (1 pt.)
            pass
        elif choice == "q":
            running = False
            print()
            print("Thank you for playing, goodbye!")
            print()
            pass
        else:
            print()
            print("ERROR: Variable 'choice' should have been 'p', 'i', or 'q', but instead was:", choice)
            print()
            quit()

if __name__ == "__main__":
    main()
