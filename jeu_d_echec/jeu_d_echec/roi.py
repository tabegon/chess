def identification(i, j):
    print('La pièce est un roi')

def found_piece_color(board):
    if board[j_origine][i_origine] == "K":
        piece = "w"
    else:
        piece = "b"
    return piece

def move_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    i_variation = i_origine - i_clic
    j_variation = j_origine - j_clic
    if abs(i_variation) <= 1 and abs(j_variation) <= 1:
        return eat_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic)
        

def eat_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    piece = found_piece_color(board)
    piece_clic = board[j_clic][i_clic]
    if board[j_clic][i_clic] != ' ': 
        if piece == "b":
            if board[j_clic][i_clic] == piece_clic.lower():
                return False
        elif piece == "w":
            if board[j_clic][i_clic] == piece_clic.upper():
                return False
    return True
