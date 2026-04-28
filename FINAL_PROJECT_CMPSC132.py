import random   # import the random module to generate random numbers in this game

def number_guessing_game():

    target_num = random.randint(1,100)   # generate random number using randint

    tries = 0  # variable to kep track of attempts

    guess = False   # used for the loop, stays false until user guesses correctly

    #Display welcome messages:
    print("Welcome to the number guessing game!")
    print("Your goal is to guess the correct number between 1 and 100!")
    


    # Begin loop using the boolean variable guess
    while guess == False:

        user_input = input("Enter your guess: ")  #take input as string to begin


        # Use a try except block to validate user input, keeping the game running, and allowing the user to enter valid input
        try:
            user_input = int(user_input)
            # validate the input
            

            tries += 1  #increment the tries


            #First case: guess is over the target number
            if user_input > target_num:
                print("Too High, please guess again!")

            #Second case: guess is lower
            elif user_input < target_num:
                print("Too Low, please guess again!")

            #Third case: user is correct -> exit loop and display final message
            else:
                print("Congrats, you guessed the number in " + str(tries) + " tries!")
                guess = True

        except ValueError as e:
            print("Error: Invalid input, Please enter an integer. ")
        
            
        

#Call the game function so user can play
number_guessing_game()