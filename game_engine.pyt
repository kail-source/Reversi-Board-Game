from components import *

# Processing coordinates 
def cli_coords_input():
    board_size = 8
    while True:
        try:
            row_input = int(input('Enter the row number of where you wanna place your piece: '))
            col_input = int(input('Enter the column number of where you wanna place your piece: '))
        except ValueError:
            print('PLease only enter Numbers')
            continue
        
        if row_input >= board_size or row_input < 0 :
            print(f'Only enter values between 0 - {board_size-1}')
            continue
        elif col_input >= board_size or col_input < 0:
            print(f'Only enter values between 0 - {board_size -1} and make a valid move')
            continue
        else:
            break
    return (row_input,col_input)


# defining a function for switching players 
def switch_player(current_player):
    if current_player == dark:
        return light
    else:
        return dark
    
    
# Simple Game Loop 
def simple_game_loop():
    print('Welcome To the Game!')
    board = initialise_board()
    current_player = dark
    count_dark = 0
    count_light = 0
    blank = 0
    check_moves = 0 # this was created to see if moves left has return false 2 times consecutively 
    while True:
        if not legal_move_left(current_player,board):
            print("No moves this round")
            current_player = switch_player(current_player)
            check_moves += 1
            if check_moves == 2:
                print('Game Over- no more moves')
                break
            continue
        
        coords = cli_coords_input()
        row = coords[0]
        col = coords[1]
        position = (row,col)
        
        legal_move_allowed = legal_move(current_player,position,board)
        if legal_move_allowed:
            flip_pieces(current_player,position,board)
            print_board(board) # printing board after every valid move
            check_moves = 0  # resets the count if a move is possible
            current_player = switch_player(current_player)
        else:
            print('Invalid move! try again')
    # calculating the number of pieces in the board to determine the winner 
    for row in board:
        for square in row:
            if square == light:
                count_light += 1
            elif square == dark:
                count_dark += 1
            else:
                blank += 1
    print(f'Dark finished the game with {count_dark}  pieces\n')
    print(f'Light finished the game with {count_light} pieces \n')
    if count_dark > count_light:
        print('Dark won!')
    elif count_light > count_dark:
        print('Light won!')
    else:
        print('It was a draw!')
    
            
if __name__ == '__main__':
    simple_game_loop()
