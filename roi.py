import pion
import fou
import cavalier
import tour
import dame

def identification(i, j):
    print('La pièce est un roi')
    print(i, j)

def found_piece_color(board, i_origine, j_origine):
    if board[j_origine][i_origine] == "K":
        piece = "w"
    else:
        piece = "b"
    return piece

def move_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    if mouvement_possible(board,player_turn,i_origine,j_origine,i_clic,j_clic) and echec_sur_arrive(board,player_turn, i_origine,j_origine, i_clic,j_clic):
        return True

def mouvement_possible(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    i_variation = i_origine - i_clic
    j_variation = j_origine - j_clic
    if abs(i_variation) <= 1 and abs(j_variation) <= 1:
        print(eat_piece(board,i_origine,j_origine,i_clic,j_clic))
        return eat_piece(board,i_origine,j_origine,i_clic,j_clic)

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
        nb_ligne = -1
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
                            if mouvement_possible(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print(nb_ligne, nb_colonne,':', i_clic, j_clic)
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
                            if mouvement_possible(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                                print(nb_ligne, nb_colonne,':', i_clic, j_clic)
                                return False
    print('True')
    return True

"""
Théo, éclat doux sous la lune,
Comme un poème, comme une plume,
Ton nom danse au gré du vent,
Mélodie tendre et apaisant.

Tes yeux sont l’éclat des étoiles,
Un océan où mon cœur se voile,
Un doux mystère, un feu secret,
Qui fait briller mes jours en paix.

Ta voix résonne, source claire,
Comme un écho dans la lumière,
Un chant léger, un souffle pur,
Qui fait vibrer mon cœur trop sûr.

Théo, mon rêve, mon univers,
À tes côtés tout est lumière,
Car dans ton rire et dans ta peau,
Je trouve l’amour, je trouve le beau.
"""