# Generic
import random
import time

__author__ = "Brandon"
__version__ = "0.1.1"

def display_board():
    """
    Print's out the board display to users
    """
    print(gameBoard[6:9])
    print(gameBoard[3:6])
    print(gameBoard[0:3])


def player_input():
    """
    Player will decide whether they want to be X or O
    :return: the markers player 1 and player 2 will play with
    """
    choice = ""
    while choice != 'X' or choice != 'O':
        choice = input("Player 1, would you like to be X or O?: ")
        if choice == "X":
            player1 = "X"
            player2 = "O"
            break
        elif choice == "O":
            player1 = "O"
            player2 = "X"
            break
        else:
            print("Invalid selection, try again ... ")
    return player1, player2


def place_marker(board, marker, position):
    """
    Allows user to place a marker on the game board
    :param board: game board
    :param marker: X or O depending on player playing
    :param position: position on the game board corresponding with 1-9
    :return: the new game board
    """
    board[position - 1] = marker
    return board


def win_check():
    """
    all possible combinations of a "win" are searched
    :return: Whether or not someone has won the game
    """
    if gameBoard[0:3] == ["X"] * 3 or gameBoard[0:3] == ["O"] * 3:
        return True
    elif gameBoard[3:6] == ["X"] * 3 or gameBoard[3:6] == ["O"] * 3:
        return True
    elif gameBoard[6:9] == ["X"] * 3 or gameBoard[6:9] == ["O"] * 3:
        return True
    elif gameBoard[0:7:3] == ["X"] * 3 or gameBoard[0:7:3] == ["O"] * 3:
        return True
    elif gameBoard[1:8:3] == ["X"] * 3 or gameBoard[1:8:3] == ["O"] * 3:
        return True
    elif gameBoard[2:9:3] == ["X"] * 3 or gameBoard[2:9:3] == ["O"] * 3:
        return True
    elif gameBoard[0:9:4] == ["X"] * 3 or gameBoard[0:9:4] == ["O"] * 3:
        return True
    elif gameBoard[2:7:2] == ["X"] * 3 or gameBoard[2:7:2] == ["O"] * 3:
        return True
    else:
        return False


def space_occupied(board, position):
    """
    check to see if the space is occupied
    :param board: pass in the gameboard
    :param position: pass in the index position
    :return: a boolean value
    """
    if board[position - 1] == "X" or board[position - 1] == "O":
        return True
    else:
        return False


def board_full(board):
    """
    check to see if the gameboard is full
    :param board: pass in the gameboard
    :return: a boolean value
    """
    if " " in board:
        return False
    else:
        return True


def player_choice(board):
    """
    lets player enter in a choice
    :param board: pass in the gameboard
    :return: an index choice
    """
    persist = False
    while not persist:
        choice = int(input("Choose a number between 1-9 corresponding to numpad to place your move: "))
        outcome = space_occupied(board, choice)
        if outcome:
            print("That space is occupied! Try again ... ")
        else:
            return choice
            break


def replay():
    """
    prompts the user if they want to play again
    :return: a boolean value
    """

    while True:
        choice = input("Do you want to play again? (Y/N) ")
        if choice == "Y":
            return "Y"
            break
        elif choice == "N":
            return "N"
            break
        else:
            print("Invalid choice .. ")
            False


##GAME PLAY
game_on = True
print("Welcome to Tic Tac Toe")
print("This is a game for two players ... find a friend; player one gets to decide on their symbol first")
time.sleep(1)

while game_on:
    gameBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    p1 = ""
    p2 = ""
    display_board()
    time.sleep(1)
    p1, p2 = player_input()
    print("Player one you are: " + p1 + "   Player two you are: " + p2)
    while True:
        print("\n")
        print("Player one - ")
        chosen_space = player_choice(gameBoard)
        place_marker(gameBoard, p1, chosen_space)
        if win_check():
            print("Game over! Look who won ... ")
            break
        if board_full(gameBoard):
            print("Game over! Board is full ...")
            break
        display_board()

        print("\n")
        print("Player two - ")
        chosen_space = player_choice(gameBoard)
        place_marker(gameBoard, p2, chosen_space)
        if win_check():
            print("Game over! Look who won ... ")
            break
        elif board_full(gameBoard):
            print("Game over! Board is full ...")
            break
        else:
            pass
        display_board()


    display_board()
    play_again = replay()
    if play_again == "Y":
        pass
        print("\n")
    if play_again == "N":
        break