instruction_board = {'7': '7', '8': '8', '9': '9',
                     '4': '4', '5': '5', '6': '6',
                     '1': '1', '2': '2', '3': '3',
                     }

the_board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' ',
             }


def instructions(board):
    print("Welcome to the Tic-Tac-Toe Club")
    print()
    print("The format of board is as follows: ")
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print('-+-+-')
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print('-+-+-')
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print("Enjoy the Game!! Good Luck")
    print()


def print_board(board):
    print()
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print('-+-+-')
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print('-+-+-')
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print()


def game():
    instructions(instruction_board)
    turn = "X"
    count = 0
    input("ENTER to start the game!")
    for i in range(10):
        print_board(the_board)
        move = input("It's your turn, " + turn + ".\nPlease enter the number you want!")

        if the_board[move] == " ":
            the_board[move] = turn
            count += 1

        else:
            print("That's already filled Please choose again: ")
            continue

        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':  # across the top
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':  # across the middle
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':  # across the bottom
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':  # down the left side
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':  # down the middle
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':  # down the right side
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':  # diagonal
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':  # diagonal
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        if count == 9:
            print("Well it's a Tie!")
            break

        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    play_again = input("Do you wanna play again(y/n)").lower()
    if play_again == "y":
        game()
    else:
        print("Thank you for playing! Have a good Day")


if __name__ == "__main__":
    game()
