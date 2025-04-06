import roi

def identification(i, j):
    print("La pièce est une dame")
    
def move_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    if i_origine == i_clic :
        if roi.echec(board,player_turn, i_origine,j_origine):
                return 'echec'
        elif roi.echec_et_mat(board,player_turn,i_origine,j_origine,i_clic,j_clic):
            return 'echec_et_mat'
        elif roi.pat(board,player_turn,i_origine,j_origine,i_clic,j_clic):
            return 'pat'
        return True
    elif j_origine == j_clic:
        if roi.echec(board,player_turn, i_origine,j_origine):
                return 'echec'
        elif roi.echec_et_mat(board,player_turn,i_origine,j_origine,i_clic,j_clic):
            return 'echec_et_mat'
        elif roi.pat(board,player_turn,i_origine,j_origine,i_clic,j_clic):
            return 'pat'
        return True    
    elif abs(i_origine - i_clic) == abs(j_origine - j_clic):
        if roi.echec(board,player_turn, i_origine,j_origine):
                return 'echec'
        elif roi.echec_et_mat(board,player_turn,i_origine,j_origine,i_clic,j_clic):
            return 'echec_et_mat'
        elif roi.pat(board,player_turn,i_origine,j_origine,i_clic,j_clic):
            return 'pat'
        return True
    else:
        return False

def piece_in_move_vertical(board, j_origine, i_origine, j_clic, i_clic): # board, ydep, xdep, yar, ydep     
    print('Déplacement vertical')
    variation = (j_origine - j_clic)                        # variation = ydep - yar (plus petit ou plus grand que 0)
    if variation < 0:                                       # si la variation est plus petite que 0 
        for i in range(abs(variation)-1):                   # pour le nombre de abs(variation) - 1 pour pas vérifier la dérnière case 
            if board[j_origine+(i)][i_origine] != " ":      # si sur le board au coordonnées [ydep]
                print(board[j_origine+(i)][i_origine])
                print('Il y a une pièce !')
                return False
        return True
    else:
        for i in range(variation-1):
            if board[j_origine+(i)][i_origine] != " ":
                print(board[j_origine+(i)][i_origine])
                print('Il y a une pièce !')
                return False
        return True


def piece_in_move_horizontal(board, j_origine, i_origine, j_clic, i_clic):
    print('Déplacement horizontal')
    variation = (i_origine - i_clic)
    if variation < 0:
        for i in range(abs(variation)-1):
            if board[j_origine][i_origine-(i+1)] != " ":
                print(board[j_origine][i_origine-(i+1)])
                print('Il y a une pièce !')
                return False
        return True
    else:
        for i in range(variation-1):
            if board[j_origine][i_origine-(i+1)] != " ":
                print(board[j_origine][i_origine-(i+1)])
                print('Il y a une pièce !')
                return False
        return True

