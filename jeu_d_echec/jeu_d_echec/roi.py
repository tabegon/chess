def identification(i, j):
    print('La pièce est un roi')

def move_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    i_variation = i_origine - i_clic
    j_variation = j_origine - j_clic
    if abs(i_variation) == 1 or abs(j_variation) == 1:
        return True
        

def eat_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    if board[j_origine][i_origine] == "K":
        piece = "w"
    else:
        piece = "b"
    
    piece_black = board[j_clic][i_clic]
    if board[j_clic][i_clic] != ' ': 
        if board[j_clic][i_clic] == piece_black.lower():
            return False
    return True
