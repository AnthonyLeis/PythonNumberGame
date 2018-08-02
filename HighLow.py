# Intro Screen
print("Welcome to the HercuLeis number game!!")
print()
print("I'm thinking of a number between 1 and 1000. Can you guess it??")
print()
print("Each time you guess, I will tell you if your number is too small or too large.")
# Initial Conditions
import random
terminate = False
while not terminate:
    GameOver = False
    iteration = 0
    lvl = str(input("Enter your desired level of difficulty; easy, med, hard or insane.\n"))
    if lvl == "easy":
        top = 11
        x = random.randint(1,1000)
    elif lvl == "med":
        top = 10
        x = random.randint(1,1000)
    elif lvl == "hard":
        top = 9
        x = random.randint(1,1000)
    elif lvl == "insane":
        print("On insane difficulty, there are ten times more possible numbers,\nbut you still have eleven guesses to find it.")
        bad = str(input("Are you sure you want to play on this difficulty? (y/n)"))
        if bad == "y":
            top = 11
            x = random.randint(1,10000)
        else:
            print("Okay we will play on hard then.")
            top = 9
            x = random.randint(1,1000)
    else:
        print("Please enter 'easy', 'med', 'hard', or insane to indicate your desired difficulty level.\n")
        while lvl != "easy" and lvl !="med" and lvl !="hard" and lvl != "insane":
            lvl = str(input("What is your desired difficulty level? "))
            if lvl == "easy":
                top = 11
                x = random.randint(1,1000)
            if lvl == "med":
                top = 10
                x = random.randint(1,1000)
            if lvl == "hard":
                top = 9
                x = random.randint(1,1000)
            if lvl == "insane":
                print("On insane difficulty, there are ten times more possible numbers,\nbut you still have eleven guesses to find it.")
                bad = str(input("Are you sure you want to play on this difficulty? (y/n)"))
                if bad == "y":
                    top = 11
                    x = random.randint(1,10000)
                elif bad == "n":
                    print("Okay we will play on hard then")
                    top = 9
                    x = random.randint(1,1000)
                else:
                    print("Please enter a valid difficulty.")

    print("You have ", top, "guesses to find my number! Good luck!")
#Game Loop
    while not GameOver:

        iteration = iteration + 1
        if iteration == 1:
            guess = int(input("What is your first guess?: "))
        elif iteration >top:   # limit of guesses
            print("I'm sorry, you are out of guesses now.")
            GameOver = True
        elif iteration == top:
            guess = int(input("Okay, this is your final guess. What is your final guess?: "))
        else:
            guess = int(input("What is your next guess?: "))
        if iteration !=top:
            if guess == x :
                print("You found my number!! Good job!")
                GameOver = True
            elif guess < x :
                print("Your number is too small.")
            elif guess > x :
                print("Your number is too large.")
        if iteration == top:
            if guess == x :
                print("You found my number!! Good job!")
            else:
                print("Sorry, I win. my number was ", x,".")
            GameOver = True
        if GameOver:
            retry = str(input("Would you like to play again, yes or no? "))
            if retry == "no":
               terminate = True
            elif retry == "yes":
                break
            else:
                print("Please enter 'yes' or 'no'.")
                while retry != "yes" and retry != "no":
                    retry = str(input("Would you like to play again, yes or no? "))
                    if retry == "no":
                        terminate = True
print("Thanks for playing....Goodbye.")
