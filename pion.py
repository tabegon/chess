def identification(i, j):
    print('La pièce est un pion')
    print(i, j)

bouger = False
def found_piece_color(board, i_origine, j_origine):
    """
    trouve la couleur de la piece cliquée
    @param i_origine, j_origine : coordonnée y, x de la pièce compris entre 0 et 7 inclu
    @return piece : 'w' ou 'b'  
    """
    if board[j_origine][i_origine] == board[j_origine][i_origine].upper(): 
        piece = "w"     # Si le caractére au coordoné du clic est une majuscule alors c'est une piéce blanche  
    else:
        piece = "b"     # Sinon c'est une piece noire 
    return piece

def move_piece(board, player_turn, i_origine, j_origine, i_clic, j_clic):
    global bouger
    condition1 = mouvement_possible(board, player_turn, i_origine, j_origine, i_clic, j_clic)
    condition2 = eat_piece(board,i_origine,j_origine,i_clic,j_clic)
    if condition1 or condition2:
        bouger = True
        return True
    return False

def mouvement_possible(board, player_turn, i_origine, j_origine, i_clic, j_clic):
    piece = found_piece_color(board, i_origine, j_origine)
    if piece == "b":
        if i_origine == i_clic:
            if board[j_origine-1][i_origine] == " ":
                if i_clic == i_origine and j_clic == j_origine-2:
                    return not bouger
                elif i_clic == i_origine and j_clic == j_origine-1:
                    return True
                else:
                    return False
    else:
        if i_origine == i_clic:
            if board[j_origine+1][i_origine] == " ":
                if i_clic == i_origine and j_clic == j_origine+2:
                    return not bouger
                elif i_clic == i_origine and j_clic == j_origine+1:
                    return True
                else:
                    return False
            else:
                return False



def eat_piece(board,i_origine,j_origine,i_clic,j_clic):
    """
    détermine si on a le droit de manger la pièce suivant sa couleur 
    @return : booléen 
    """
    piece = found_piece_color(board, i_origine, j_origine)  # On utilise ici la fonction found_piece_color pour determiner la couleur de la piece 
    piece_clic = board[j_clic][i_clic]
    if board[j_clic][i_clic] != ' ': 
        if piece == "b":
            if piece_clic == board[i_origine-1][j_origine-1].upper() or board[i_origine+1][j_origine-1].upper(): # Si la piece sur laquelle on clique est un piece noire alors False 
                return True
        elif piece == "w":
            if piece_clic == board[i_origine-1][j_origine+1].upper() or board[i_origine+1][j_origine+1].upper(): # Si la piece sur laquelle on clique est un piece noire alors False 
                return True
    return False    # Sinon on return False    
