import random

#this by default will take a string even if it is a number, so it needs to be parsed into an int via the int method.
maximumNumberSize = input("Type a number: ")

#checks to make sure that something is a digit by using the isDigit() method
if maximumNumberSize.isdigit():
    maximumNumberSize = int(maximumNumberSize)
    if maximumNumberSize <= 0:
        print("Please type a number greater than 0.")
        quit()
else:
    print("Please type a number next time")
    quit()

randomNumber = random.randint(0, maximumNumberSize)
print(randomNumber)

while True:
    userGuess = input("Can you guess a number: ")
    break #stops the loop when the line is reached
