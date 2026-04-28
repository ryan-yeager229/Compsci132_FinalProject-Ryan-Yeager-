import random   # import the random module to generate random numbers in this game



def number_guessing_game():

    tries = 0  # variable to kep track of attempts

    guess = False   # used for the loop, stays false until user guesses correctly

    target_num = random.randint(1,100)   # generate random number using randint

    print("Your goal is to guess the correct number between 1 and 100!")

    while guess == False:

            

        user_input = input("Enter your guess: ")  #take input as string to begin

            
        # Use a try except block to validate user input, keeping the game running, and allowing the user to enter valid input
        try:
            user_input = int(user_input)


            # validate the input

            if user_input < 1 or user_input > 100:
                print("Error: Please enter a number between 1 and 100")

            else:
            

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



def end_game():
    # returns True
    user_replay = input("Would you like to play again (yes/no)?: ") # ask user if they want to play again once round end

    while user_replay.lower() != 'yes' and user_replay.lower() != 'no':  #loop until user enters valid answer
        user_replay = input("Error: Please enter a valid response (yes/no):")

    if user_replay.lower() == 'no':
        return False
    else:
        return True
    

def main():

    print("Welcome to the number guessing game!")

    play_again = True  # optional addition that allows user to replay the game

    while play_again == True:
        number_guessing_game() # play new game
        play_again = end_game()  # returns a boolean


    print("Thanks for playing!")
    



#run main function that calls rest of code
main()

