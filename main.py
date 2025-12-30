import random as rd

print("Hello to Number Guessing Game")


def get_user_guess() -> int:
    """_summary_

    Returns:
        int: the user insert gess
    """
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter an integer.")
     
            
def check_guess(guess: int, number: int) -> bool:
    """_summary_

    Args:
        guess (int): the user's guess
        number (int): the randomly generated number

    Returns:
        bool: True if the guess is correct, False otherwise
    """
    if guess < number:
        print("high")
    elif guess > number:
        print("low")
    else:
        print("correct")
        return True
    return False


number = rd.randint(1, 20)
number_of_guesses: int = 0
# print(number)  # For testing purposes; remove or comment out in production
print("You have 6 attempts to guess the number between 1 and 20")
while number_of_guesses < 6:
    guess = get_user_guess()
    number_of_guesses += 1
    isvalid = check_guess(guess, number)
    if isvalid:
        break
if guess == number:
    print(f"Congratulations! {number} in {number_of_guesses} attempts.") 
else:
    print(f"Sorry, you've used all your attempts. The number was {number}.")
    
