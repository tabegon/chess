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
    if board[j_origine][i_origine] == board[j_origine][i_origine].upper():
        piece = "w"
    else:
        piece = "b"
    return piece

def find_adverse_king(board, piece):
    if piece == "b":
        roi_adverse = 'K'
    elif piece == "w":
        roi_adverse = 'k'
    for j in range(8):
        for i in range(8):
            if board[j][i] == roi_adverse:
                return i, j

def move_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    global bouger
    condition1 = mouvement_possible(board,player_turn,i_origine,j_origine,i_clic,j_clic)
    condition2 = echec_sur_arrive(board,player_turn, i_origine,j_origine, i_clic,j_clic)
    condition3 = eat_piece(board,i_origine,j_origine,i_clic,j_clic)
    if condition1 and condition2 and condition3:
        if turn(board, player_turn, i_origine, j_origine):
            bouger = True
            return True
    return False

def mouvement_possible(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    i_variation = i_origine - i_clic
    j_variation = j_origine - j_clic
    if abs(i_variation) <= 1 and abs(j_variation) <= 1:
        return True
    return False

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

def turn(board, player_turn, i_origine, j_origine):
    piece = found_piece_color(board, i_origine, j_origine)
    if player_turn == piece:
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
        for ligne in board:
            nb_ligne += 1
            nb_colonne = -1
            for case in ligne:
                nb_colonne += 1
                if case == i:

                    if i == 'R':
                        if tour.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False
                    
                    if i == 'N':
                        if cavalier.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False
                        
                    if i == 'B':
                        if fou.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False
                    
                    if i == 'Q':
                        if dame.mouvement_possible(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            print('dame menace')
                            return False
                    
                    if i == 'K':
                        if mouvement_possible(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False
                    
                    if i == 'P':
                        if pion.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False

                    
                    if i == 'r':
                        if tour.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False
                    
                    if i == 'n':
                        if cavalier.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False
                        
                    if i == 'b':
                        if fou.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False
                    
                    if i == 'q':
                        if dame.mouvement_possible(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False
                    
                    if i == 'k':
                        if mouvement_possible(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False

                    if i == 'p':
                        if pion.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False
    
    return True

def echec(board,player_turn, i_origine,j_origine):
    return not echec_sur_arrive(board, player_turn, i_origine, j_origine, i_origine, j_origine) # Renvoie True quand le roi adverse est en echec

def echec_et_mat(board,player_turn,i_origine,j_origine):
    if echec(board,player_turn, i_origine,j_origine):
        liste_i = [abs(i_origine+1), abs(i_origine-1), i_origine]
        liste_j = [abs(j_origine+1), abs(j_origine-1), j_origine]
        if eat_piece(board,i_origine,j_origine,liste_i[0], liste_j[2]) and echec_sur_arrive(board, player_turn, i_origine, j_origine, liste_i[0], liste_j[2]):
            return False
        elif eat_piece(board,i_origine,j_origine,liste_i[1], liste_j[2]) and echec_sur_arrive(board, player_turn, i_origine, j_origine, liste_i[1], liste_j[2]):
            return False
        
        elif eat_piece(board,i_origine,j_origine,liste_i[2], liste_j[0]) and echec_sur_arrive(board, player_turn, i_origine, j_origine, liste_i[2], liste_j[0]):
            return False
        elif eat_piece(board,i_origine,j_origine,liste_i[2], liste_j[1]) and echec_sur_arrive(board, player_turn, i_origine, j_origine, liste_i[2], liste_j[1]):
            return False
        
        elif eat_piece(board,i_origine,j_origine,liste_i[0], liste_j[0]) and echec_sur_arrive(board, player_turn, i_origine, j_origine, liste_i[0], liste_j[0]):
            return False
        elif eat_piece(board,i_origine,j_origine,liste_i[1], liste_j[1]) and echec_sur_arrive(board, player_turn, i_origine, j_origine, liste_i[1], liste_j[1]):
            return False
        
        elif eat_piece(board,i_origine,j_origine,liste_i[1], liste_j[0]) and echec_sur_arrive(board, player_turn, i_origine, j_origine, liste_i[1], liste_j[0]):
            return False
        elif eat_piece(board,i_origine,j_origine,liste_i[0], liste_j[1]) and echec_sur_arrive(board, player_turn, i_origine, j_origine, liste_i[0], liste_j[1]):
            return False
        else:
            return True

    else:
        return False
