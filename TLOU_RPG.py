#    <Wyatt Spohn>    <4/19/23>
#    <COMS 127 B>
# In this RPG game you will be tasked with a mission in a post-appocyltic world and you will have to make decisions for your 
# hero in hopes to survive.

def initialChoice():
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

def gameStart(dead):
    print("Just a normal day in Ames Iowa")
    input("Press enter to continue...")
    
    cereal = input("What cereal would you like to eat? [l]ucky charms or [h]oneynut cherrios?: ")
    while cereal != "l" and cereal != "h":
        print("ERROR: Please enter 'l' or 'h'...")
        cereal = input("What cereal would you like to eat? [l]ucky charms or [h]oneynut cherrios?: ")

    door = input("Theres a knocking at the door. Do you get up and answer it? [y]es or [n]o?: ")
    while door != "y" and door != "n":
        print("ERROR: Please enter 'y' or 'n'...")
        door = input("Theres a knocking at the door. Do you get up and answer it? [y]es or [n]o?: ")
    
    return cereal, door

def newYork():
    print("NewYork")

def cleveland():
    print("Cleveland")

def chicago():
    print("Chicago")

def minneapolis():
    print("Minneapolis")

def montana():
    print("Montana")

def seattle(dead):
    print("You made it to Seattle, You win!!!")
    dead = True

    return dead
    

def updateHealth(val):
    health = health + val

def updateHunger(val):
    hunger = hunger + val

def gameOver():
    print("DAMN BRO YOU SUCK, YOU DESERVED TO DIE")

def main():
    running = True
    dead = False
 
    while running:
        choice = initialChoice()
        if choice == "p":
            while dead != True:
                
                cereal, door = gameStart(dead)
                if door == "n":
                    print("Good choice")
                elif door == "y":
                    print("You got attacked and died")
                    dead = True
                    break

                if cereal == "l":
                    print("Good choice")
                elif cereal == "h":
                    print("Something doesnt feel so good, maybe it was something you ate")
                    dead = True
                    break

                

                newYork()
                cleveland()
                chicago()
                minneapolis()
                montana()
                dead = seattle(dead)

            #gameOver()

            break
        elif choice == "i":
            print()
            print("instructions")
            print()

            pass
        elif choice == "q":
            print()
            print("Thank you for playing! Goodbye!")
            print()
            running = False
            
            pass
        else:
            print("ERROR: Variable 'choice' should have been 'p', 'i', or 'q', but instead was:", choice)
            quit()

if __name__ == "__main__":
    main()