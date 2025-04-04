import pion
import fou
import cavalier
import tour
import dame

def identification(i, j):
    print() 
    print('La pièce est un roi')
    print(i, j)

def found_piece_color(board, i_origine, j_origine):
    if board[j_origine][i_origine] == "K":
        piece = "w"
    else:
        piece = "b"
    return piece

def move_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    condition1 = mouvement_possible(board,player_turn,i_origine,j_origine,i_clic,j_clic)
    condition2 = echec_sur_arrive(board,player_turn, i_origine,j_origine, i_clic,j_clic)
    condition3 = eat_piece(board,i_origine,j_origine,i_clic,j_clic)
    if condition1 and condition2 and condition3:
        return True
    return False

def mouvement_possible(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    i_variation = i_origine - i_clic
    j_variation = j_origine - j_clic
    if abs(i_variation) <= 1 and abs(j_variation) <= 1:
        print('la menace')
        return True
    return False

def eat_piece(board,i_origine,j_origine,i_clic,j_clic):
    print('je mange')
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
        nb_ligne = -1
        for ligne in board:
            nb_ligne += 1
            nb_colonne = -1
            for case in ligne:
                nb_colonne += 1
                if case == i:

                    if i == 'R':
                        if tour.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('la tour menace')
                            return False
                    
                    if i == 'N':
                        if cavalier.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('le cavaliver menace')
                            return False
                        
                    if i == 'B':
                        if fou.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('la tour menace')
                            return False
                    
                    if i == 'Q':
                        if dame.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            print('la reine menace a partir de', nb_ligne , nb_colonne, 'sur : ', i_clic,j_clic)
                            print(i_clic, j_clic)
                            return False
                    
                    if i == 'K':
                        print(mouvement_possible(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic))
                        if mouvement_possible(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            print('le roi menace')
                            return False
                    
                    if i == 'P':
                        if pion.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('le pion menace')
                            return False

                    
                    if i == 'r':
                        if tour.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('la tour menace')
                            return False
                    
                    if i == 'n':
                        if cavalier.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('le cavalier menace')
                            return False
                        
                    if i == 'b':
                        if fou.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('le fou menace')
                            return False
                    
                    if i == 'q':
                        if dame.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('la dame menace')
                            return False
                    
                    if i == 'k':
                        if mouvement_possible(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('le roi menace')
                            return False

                    if i == 'p':
                        if pion.move_piece(board, player_turn, nb_ligne, nb_colonne, i_clic, j_clic):
                            print('le pion menace')
                            return False
    
    return True
