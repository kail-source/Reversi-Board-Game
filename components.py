
# for reliability I have used variables so spacing issue will not be a problem
empty = 'None '
dark = 'Dark '
light = 'Light'

# Initialising the board 
def initialise_board(size = 8):
    board = []
    for row_num in range(size):
        row = [] # Creates 8 rows  
        for col_num in range(size):
            row.append(empty) # Fills the collumns with None and apprends it all to the board
        board.append(row)
        
    # Starting point 
    board[3][3] = light 
    board[4][4] = light
    board[3][4] = dark
    board[4][3] = dark


    return board
        
def print_board(board):
    print('\n')
    for row in board:
        print(" ".join(row)) # Starting a new line after the row
    print('\n')



# Defining directions
directions = [
              (-1,0), # up
              (1,0), # Down
              (0,-1), # left 
              (0,1), # right 
              (-1,-1), # up left
              (1,-1), # down left
              (-1,1), # up right 
              (1,1), #down righ
              ]
                        
                    
# Defining legality 
def legal_move(colour, position, board):
    board_size = 8
    row = position[0]
    col = position[1]
    if board[row][col] != empty:
        return False
    if colour == dark:
        opponent = light
    else:
        opponent = dark
    for direction in directions:
        direction_rows = direction[0]
        direction_cols = direction[1]
        current_row = row + direction_rows
        current_col = col + direction_cols
        
        opponent_found = False
        # creating the bounds to which it can keep looking
        while 0 <= current_row < board_size and 0<= current_col < board_size:
            current_square = board[current_row][current_col]
            # If we find opponent piece, keep going
            if current_square == opponent:
                opponent_found = True
                current_row += direction_rows
                current_col += direction_cols
                continue
            if current_square == colour and opponent_found: # if we found the current players colour and the opponents piece in one direction                 
                return True # It is a valid move
            else:
                break # else it means we hit empty or our colour with no opponent in the middle so not valid           
    return False

#checking if there are ny legal moves that can be played
def legal_move_left(colour,board):
    for row in range(8):
        for col in range(8):
            if board[row][col] == empty:
                if legal_move(colour,(row,col), board): # for every row and column, if there are legal moves that cane played
                    return True # function returns true
                
    return False # else false


                


def to_flip(colour,position,board):
    board_size = 8
    row = position[0]
    col = position[1]
    to_flip_coords = []
    if colour == dark:
        opponent = light
    else:
        opponent = dark
    for direction in directions:
        direction_rows = direction[0]
        direction_cols = direction[1]
        current_row = row + direction_rows
        current_col = col + direction_cols
        temp_coords = []
        # creating the bounds to which it can keep looking
        while 0 <= current_row < board_size and 0<= current_col < board_size:
            current_square = board[current_row][current_col]
            # If we find opponent piece, keep going
            if current_square == opponent:
                #opponent_found = True
                temp_coords.append((current_row, current_col))
                current_row += direction_rows
                current_col += direction_cols
                continue
            elif current_square == colour and temp_coords: # if our colour and temporary coordinates list is not empty 
                to_flip_coords.extend(temp_coords)
                break
            else:
                break
    return to_flip_coords
# The Flip pieces function 
def flip_pieces(colour, position, board):
    row = position[0]
    col = position[1]
    
    pieces_to_flip = to_flip(colour, position, board) #Calling the function with all the coordinates of to flip 
    for rows, cols in pieces_to_flip:
        board[rows][cols] = colour # I understand rows and cols only represent a single row but I wrote it like this for readability
        
    board[row][col] = colour
    
    return True
