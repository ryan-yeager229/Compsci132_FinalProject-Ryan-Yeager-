# Compsci132_FinalProject-Ryan-Yeager-
Terminal Based single player number guessing game. 


# Project Description:
. This the number guessing game project, with the added feature of users being able replay the game
. The code consists of three functions, main(), number_guessing_game(), and end_game().
. The main function introduces that game, and calls the other 2 functions
. The nunmber_guessing_game function runs the user through the game, until they enter the correct number generated using random.randint(1,100)
. In the number_guessing game function, input is also validated, preventing the code from running into errors due to invalid input
. The end_game function checks user input when asked if they want to play again. It returns true if they want to play again, False otherwise
. At the very end, the program ends, leaving a thank you message for the user. 


# Instructions: 
1. First, load the game file into the terminal using the cd command
2. Run the python file, which will call the main function, which controls the 2 game functions
3. User will be prompted to enter number between 1 and 100. Code makes sure that there are exceptions behind invalid input
4. Keep entering numbers until target number is guessed
5. Once user guesses correctly, they will have option to play another round
6. If user plays another round, steps 3-5 will be repeated with a new target number
7. If user does not wish to play again, the program will end. 



