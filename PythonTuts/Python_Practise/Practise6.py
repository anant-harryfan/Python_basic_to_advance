# Problem Statement:-
# Generate a random integer from a to b. You and your friend have to guess a number between two numbers, a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number, and your program must tell whether the number is greater than the actual number or less than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same game, and then the person with the minimum number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.
#
# Input:
# Enter the value of a
# 4
#
# Enter the value of b
# 13
#
# Output:
# Player1 :
# Please guess the number between 4 and 13
# 5
#
# Wrong guess a greater number again
# 8
#
# Wrong guess a smaller number again
# 6
#
# Correct, you took 3 trials to guess the number
# Player 2:
# Correct, you took 7 trials to guess the number
#
# Player 1 wins!


import random


def guessGame(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input(f"Enter a bigger number\n"))
            nguess += 1
        else:
            guess = int(input(f"Enter a smaller number\n"))
            nguess += 1

    print(f"You guessed the number in {nguess} guesses\n")
    return nguess


if __name__ == "__main__":
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    actual1 = random.randint(a, b)
    print("Player 1's turn\n")
    g1 = guessGame(a, b, actual1)
    print("Player 2's turn\n")
    actual2 = random.randint(a, b)
    g2 = guessGame(a, b, actual2)

    if g1 < g2:
        print("Player 1 won the match!\n")

    elif g1 > g2:
        print("Player 2 won the match!\n")

    else:
        print("Its a Tie!\n")

    print(f"The number for player 1 was {actual1} and for player 2 was {actual2}")

