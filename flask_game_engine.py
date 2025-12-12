from components import *
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global game state 
board = initialise_board()
current_player = dark 

@app.route('/')

def index():
    return render_template(
        'index.html',
        game_board = board
    )

@app.route('/move')

def move():
    global current_player, board
    
    row = int(request.args.get('x'))
    col = int(request.args.get('y'))
    position = (row, col)
    
    if not legal_move(current_player, position, board):
        return jsonify({
            'status': 'fail',
            'message': 'Illegal move',
            'board': board
            })
    
    flip_pieces(current_player, position, board)
    
    # Switch player
    if current_player == dark:
        current_player = light
    else:
        current_player = dark
    
    # Check if new current player has moves
    if not legal_move_left(current_player, board):
        # Player passes 
        passed_player = current_player
        if current_player == dark:
            current_player = light
        else:
            current_player = dark
            
        # Check if game ends
        if not legal_move_left(current_player, board):
            return jsonify({
                'finished': 'Game over! No legal moves left on the board.',
                'board': board
            })
        
        return jsonify({
            'status': 'success',
            'board': board,
            'player': current_player,
            'message': f'{passed_player} passed'
        })
    
    return jsonify({
        'status': 'success',
        'board': board,
        'player': current_player
    })
    
if __name__ == '__main__':
    app.run(debug = True)
    
