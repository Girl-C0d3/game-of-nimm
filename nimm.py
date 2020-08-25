"""
File: nimm.py
-------------------------
The game of nimm begins with 20 stones. Two players will be given the choice, in turn, to take one or two stones.
The game stops when all stones have been taken, and the last player to take a stone loses.
"""


def main():

    """number of stones at the start of the game is 20, and the game will always start with player 1"""
    number_of_stones = 20
    player = 1
    while number_of_stones > 2:
        print("There are " + str(number_of_stones) + " stones left")
        stones_taken = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones?"))
        # The player is asked to choose to take one or two stones
        # If the user inputs a number other than 1 or 2, they will be prompted to choose again until they make a valid
        # choice
        while stones_taken < 1 or stones_taken > 2:
            stones_taken = int(input("Please enter 1 or 2: "))
            print("")
        number_of_stones -= stones_taken
        # Once a selection of 1 or 2 stones has been made, this value is deducted from the total number of stones
        # If current player is 1, player 2 will be prompted to choose next, and vice versa
        if player == 1:
            player = 2
        else:
            player = 1
    print("")

# The overall outcome of the game is based on the decisions made from the point of 2 stones remaining, or 1 stone
# remaining
    if number_of_stones == 2:
        print("There are 2 stones left")
        stones_taken = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones?"))
        print("")

        if stones_taken == 2:
            if player == 1:
                print("Player 2 wins!")
            else: print("Player 1 wins!")
        elif stones_taken == 1:
            print("There is 1 stone left")
            if player == 1:
                print("Player 2 wins!")
            else: print("Player 1 wins!")

# If the 'two stones remaining' stage is bypassed, the player active when there is one stone left is forced to take that
# stone. This results in the opposing player winning.
    if number_of_stones == 1:
        print("There is 1 stone left")
        if player == 1:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")


if __name__ == '__main__':
    main()
