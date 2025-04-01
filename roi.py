import pion as P
import fou as B
import cavalier as N
import tour as R
import dame as Q

def identification(i, j):
    print('La pièce est un roi')

def found_piece_color(board, i_origine, j_origine):
    if board[j_origine][i_origine] == "K":
        piece = "w"
    else:
        piece = "b"
    return piece

def move_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    i_variation = i_origine - i_clic
    j_variation = j_origine - j_clic
    if abs(i_variation) <= 1 and abs(j_variation) <= 1:
        mvmt_possible = eat_piece(board,i_origine,j_origine,i_clic,j_clic)
    if mvmt_possible and echec_sur_arrive(board,player_turn, i_origine,j_origine, i_clic,j_clic):
        return True
        

def eat_piece(board,i_origine,j_origine,i_clic,j_clic):
    piece = found_piece_color(board, i_origine, j_origine)
    piece_clic = board[j_clic][i_clic]
    if board[j_clic][i_clic] != ' ': 
        if piece == "b":
            if board[j_clic][i_clic] == piece_clic.lower():
                return False
        elif piece == "w":
            if board[j_clic][i_clic] == piece_clic.upper():
                return False
    return True

def echec_sur_arrive(board,player_turn, i_origine,j_origine, i_clic,j_clic):
    nb_ligne = -1
    nb_colonne = -1
    piece = found_piece_color(board, i_origine,j_origine)
    if piece == "b":
        chaine = "RBNQKP"
    elif piece == "w":
        chaine = "rbnqkp"
    for i in chaine:
        print(i)
        for ligne in board:
            nb_ligne += 1
            nb_colonne = -1
            for case in ligne:
                nb_colonne += 1
                if case == i:
                    if piece == "b":
                        if i.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('False')
                            return False
                    elif piece == "w":
                        z = i.upper()
                        if z.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('False')
                            return False
    print('True')
    return True
