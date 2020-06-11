board = ["-","-","-",
        "-","-","-",
        "-","-","-"]


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2]) 
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    #Display the board
    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

   


def handle_turn():
    position = input("choose a position from 1-9: ") 
    position = int(position) - 1

    board[position] = "X"
    display_board()


def check_if_game_over()
play_game()    