import random
#imports random function

def guess_number(x):
#defining a function, named guess_number, with the value x
    random_number = random.randint(1,x)
    #ask for the system to get a random number inclusive, randint means random integer
    #inclusive = including the endpoints
    guess = 0
    #create a guess value, used to store the user's data

    while guess != random_number:
        #while loop
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {x}: "))
                #use input to get an input from the user, int to change the input from the user from string to int
                #the input typed by the user will be stored into the "guess" value
                if 1 <= guess <= x:
                    break
                else:
                    print(f"Please enter a number between 1 and {x}: ")
            except ValueError:
                print ("That is not a valid number! Please try again.")

        #if elif else loop
        if guess < random_number:
            print("Higher")
        elif guess > random_number:
            print("Lower")
        else:
            print("Congratulations! You have guessed the number correctly!")
        
guess_number(40)