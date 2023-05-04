print('Welcome to the computer quiz!')
score = 0

def printCurrentScore():
    print("Your current score is " + str(score))

def negateScore():
    if score > 0:
        score *= -1

#input allows the user to type within the console. Put the String inside of the console with a space 
#at the end of the String to help with the next input variable from the user
playing = input("Do you want to play the computer quiz? ")
print("Hmm... you said " + playing + ". How interesting")

#everything you want to have happen after a condition, you'll use a colon.
if playing.lower() != "yes":
    print("I see, you didn't say yes. Well... this is sad... have a nice day.")
    quit() #this function in pytnhon immediate quits the program.

print("Yay, I finally can play the computer quiz game. It's been a while since somebody wanted to play.")


answer = input("Who is the better CPU manufacturer, AMD or Intel?")

if answer.upper() == "AMD":
    print("Yeah, that's correct")
    print("You get 25 points")
    score += 25
else:
    print("Yes, that's correct, if you like overpriced garbage :)")
    print("-5218 points. Sorry...")
    score -= 5218

printCurrentScore()

answer = input("Which Pokemon is perhaps the greatest Pokemon of all time?")

if answer.lower() == "mudkip" or answer == "that's not a computer question at all":
    score *=25
    print("Of course, Mudkip will always have our hearts and minds <3. Your score is multiplied by 25")
else:
    print("Sorry, that's just not correct. " + answer + " is a good Pokemon but not quite on the level of the greatest Pokemon.")
    score  * 900
    negateScore()

printCurrentScore()

answer = input("What is the capital of Assyria?")

if answer.lower() == "assur" or answer.lower == "nineveh":
    score *=23
    print("Of course, that is most correct")
else:
    print("Sorry, that's just not correct. ")
    score  * 900
    negateScore()

printCurrentScore()



