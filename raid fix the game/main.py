#Cecily Strong Raid: Fix the Game
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        attempts+=1 #logic error, this kept the program running forever
        guess = int(input("Enter your guess: ")) #runtime error, you forgot the int so and you can not mesure strings as numbers
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif attempts< max_attempts: #syntax error, this prevents the code from printing the previous values message after you run out of guesses
            if guess == number_to_guess: 
                print("Congratulations! You've guessed the number!")
                game_over = True
            elif guess > number_to_guess:
                print("Too high! Try again.")
            elif guess < number_to_guess:
                print("Too low! Try again.")  
        continue
    game_over=True #logic error, you need this to be true for the code to stop
    print("Game Over. Thanks for playing!")
     
start_game()