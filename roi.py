import pion
import fou
import cavalier
import tour
import dame

def identification(i, j):
    print('La pièce est un roi')

def found_piece_color(board, i_origine, j_origine):
    if board[j_origine][i_origine] == "K":
        piece = "w"
    else:
        piece = "b"
    return piece

def move_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    mvmt_possible = False
    i_variation = i_origine - i_clic
    j_variation = j_origine - j_clic
    if abs(i_variation) <= 1 and abs(j_variation) <= 1:
        mvmt_possible = eat_piece(board,i_origine,j_origine,i_clic,j_clic)
    if mvmt_possible and echec_sur_arrive(board,player_turn, i_origine,j_origine, i_clic,j_clic):
        return True
    else:
        if mvmt_possible == False:
            print('mvmt')
        elif echec_sur_arrive(board,player_turn, i_origine,j_origine, i_clic,j_clic):
            print('echec')

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


                        if i == 'R':
                            if tour.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print('False')
                                return False
                        
                        if i == 'N':
                            if cavalier.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print('False')
                                return False
                            
                        if i == 'B':
                            if fou.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print('False')
                                return False
                        
                        if i == 'Q':
                            if dame.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print('False')
                                return False
                        
                        if i == 'K':
                            if move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print('False')
                                return False

                    elif piece == "w":
                        
                        if i == 'r':
                            if tour.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print('False')
                                return False
                        
                        if i == 'n':
                            if cavalier.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print('False')
                                return False
                            
                        if i == 'b':
                            if fou.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print('False')
                                return False
                        
                        if i == 'q':
                            if dame.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print('False')
                                return False
                        
                        if i == 'k':
                            if move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print('False')
                                return False
    print('True')
    return True
