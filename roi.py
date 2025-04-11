"""
Code créer par Antoine Borries, Guillaume, Charles, Albert et moi-même Théo
Nous n'avons pas pu faire le roque et le pat car nous avons priorisé les spécifications
Nous avons du changer du code dans chess.py pour pouvoir appeller la fonction echec et
    echet et mat à chaque fin de tour
Le code est un peu répétitif à certains endroits car nous n'avons pas trouver comment nous pourrions
    faire des boucles à ces certains endroits
"""

import pion
import fou
import cavalier
import tour
import dame
# on importe les move_piece de chaque piece pour l'échec, le pat et l'echec et mate
# En esperant que les autres groupes aient fait du bon boulot
bouger = False


def identification(i, j):
    print() 
    print('La pièce est un roi')
    print(i, j)

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

def find_adverse_king(board, piece):
    """
    trouve les coordonées du roi adverse
    @param board : plateau de jeu en tant que matrice
    @param piece : variable contenant 'w' ou 'b'
    @return i, j : coordonnés du roi adverse y, x
    """
    if piece == "b":                            # Si la piece est noir alors le roi adverse est le 'K' majuscule  
        roi_adverse = 'K'
    elif piece == "w":                          # Si la piece est blanche alors le roi adverse est le 'k' minuscule 
        roi_adverse = 'k'
    for j in range(8):
        for i in range(8):                      # On parcourt toute les cases du plateau 
            if board[j][i] == roi_adverse:      # Si les coordonnées j, i sont égale au 'k' ou 'K' alors
                return i, j                     # On retourne les coordonnées 
            
def find_rook(board, piece, i_clic, j_clic):
    """
    trouve les coordonées du roi adverse
    @param board : plateau de jeu en tant que matrice
    @param piece : variable contenant 'w' ou 'b'
    @return i, j : coordonnés du roi adverse y, x
    """
    if piece == "b":                            # Si la piece est noir alors le roi adverse est le 'K' majuscule  
        rook = 'r'
    elif piece == "w":                          # Si la piece est blanche alors le roi adverse est le 'k' minuscule 
        rook = 'R'

    for j in range(8):
        for i in range(8):                      # On parcourt toute les cases du plateau 
            print(board[j][i])
            if board[j][i] == rook and (j_clic and i_clic == i and j) :      # Si les coordonnées j, i sont égale au 'k' ou 'K' alors
                return i, j                     # On retourne les coordonnées 
    return None, None

def move_piece(board,player_turn,i_origine,j_origine,i_clic,j_clic):
    """
    décide si le roi est autorisé a bouger suivant tout un tas de condition 
    @param board : plateau de jeu en tant que matrice 
    @param player_turn : booléen blanc ou noir 
    @param i_origine, j_origine : coordonnée y, x de la pièce sélectionnée compris entre 0 et 7 inclu
    @param i_clic, j_clic : coordonnée y, x de la où on veut faire aller la piece compris entre 0 et 7 inclu
    @return : booléen True/False qui conditionne la validation du coup 
    """
    global bouger                                                                          # utile pour le roque
    piece = found_piece_color(board, i_origine, j_origine)
    i_rook, j_rook = find_rook(board, piece, i_clic, j_clic)
    print(piece, i_rook, j_rook, '\n', i_clic, j_clic)
    if i_clic == i_rook and j_clic == j_rook:
        return roque(board, player_turn, i_origine,j_origine,i_clic,j_clic)

    condition1 = mouvement_possible(i_origine,j_origine,i_clic,j_clic)    
    condition2 = echec_sur_arrive(board,player_turn, i_origine,j_origine, i_clic,j_clic)
    condition3 = eat_piece(board,i_origine,j_origine,i_clic,j_clic)
    if condition1 and condition2 and condition3:               # Si les 3 conditions pour bouger sont True 
        if turn(board, player_turn, i_origine, j_origine):     # Si c'est le tour du joueur 
            bouger = True                                      # On met 'bouger' a True qui empeche le roque 
            return True                                        # on retourne True qui fait bouger la piece
    return False  # Si un des 3 trois conditions ne sont pas remplies ou que ce n'est pas le tour du joueur, on empeche le déplacement  

def mouvement_possible(i_origine,j_origine,i_clic,j_clic):
    """
    détermine si le roi a le droit de faire ce déplacement en fonction de la variation de ces coordonnées 
    @return : booléen 
    """
    i_variation = i_origine - i_clic        
    j_variation = j_origine - j_clic
    if abs(i_variation) <= 1 and abs(j_variation) <= 1: # Si le x et le y varie de 0 ou 1 alors on return 'True' 
        return True
    return False

def eat_piece(board, i_origine,j_origine,i_clic,j_clic):
    """
    détermine si on a le droit de manger la pièce suivant sa couleur 
    @return : booléen 
    """
    piece = found_piece_color(board, i_origine, j_origine)  # On utilise ici la fonction found_piece_color pour determiner la couleur de la piece 
    piece_clic = board[j_clic][i_clic]
    if board[j_clic][i_clic] != ' ': 
        if piece == "b":
            if board[j_clic][i_clic] == piece_clic.lower(): # Si la piece sur laquelle on clique est un piece noire alors False 
                return False
        elif piece == "w":
            if board[j_clic][i_clic] == piece_clic.upper(): # Si la piece sur laquelle on clique est un piece blanche alors False 
                return False
    return True    # Sinon on return False 

def roque(board, player_turn, i_origine,j_origine,i_clic,j_clic):
    if bouger == False and tour.bouger_rook == False:
        piece = found_piece_color(board, i_origine, j_origine)
        i_rook, j_rook = find_rook(board, piece, i_clic, j_clic)
        i = i_origine
        while i != i_rook:
            if eat_piece(board,i_origine,j_origine,i_origine, i) and not echec_sur_arrive(board, player_turn, i_origine, i, i_clic, j_clic):
                return False
            if i_origine > i_rook:
                i -= 1
            else:
                i += 1
        if i_origine > i_rook:
            #  Déplacement de la pièce à l'endroit du clic
            board[j_clic][i_clic+1] = board[j_origine][i_origine]
            #  Suppression de la pièce de son ancien emplacement
            board[j_origine][i_origine] = ' '


            #  Déplacement de la tour à l'endroit du clic
            board[j_origine][i_origine-1] = board[j_clic][i_clic]
            #  Suppression de la tour de son ancien emplacement
            board[j_rook][i_rook] = ' '

        else:
            #  Déplacement de la pièce à l'endroit du clic
            board[j_clic][i_clic-2] = board[j_origine][i_origine]
            #  Suppression de la pièce de son ancien emplacement
            board[j_origine][i_origine] = ' '


            #  Déplacement de la tour à l'endroit du clic
            board[j_origine][i_origine+1] = board[j_clic][i_clic]
            #  Suppression de la tour de son ancien emplacement
            board[j_rook][i_rook] = ' '
        return False
        



def turn(board, player_turn, i_origine, j_origine):
    """
    determine si c'est le tour du joueur 
    @return : booléen 
    """
    piece = found_piece_color(board, i_origine, j_origine)  
    if player_turn == piece:    #Si le tour est celui de la piece cliquée, on return True
        return True

def echec_sur_arrive(board,player_turn, i_origine,j_origine, i_clic,j_clic):
    """
    détermine si la case sur laquelle le joueur a cliqué est menacé par une pièce ou pas 
    @return : booléen renseignant sur la possibilité pour le roi d'aller sur cette case 
                    (et non s'il est en echec à l'arrivée, ce qui est contre-intuitif)
    """
    nb_ligne = -1
    nb_colonne = -1
    piece = found_piece_color(board, i_origine,j_origine)
    if piece == "b":
        chaine = "RBNQKP"   #Si la piece est noire alors on verifiera toutes les pieces blanches sous forme de string  
    elif piece == "w":
        chaine = "rbnqkp"   # Idem si la piece est blanche 
    for i in chaine:        # Pour chaque piece dans le string 
        nb_ligne = -1       
        for ligne in board:
            nb_ligne += 1       # On ajoute 1 pour etre a la premiere ligne 
            nb_colonne = -1     
            for case in ligne: 
                nb_colonne += 1 # On ajoute 1 pour etre a la premiere colonne 
                if case == i:

                    if i == 'R':    # si le caractere de la case est 'R' 
                        if tour.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False  # Alors on regarde si la tour peut aller sur cette case et, si oui on retourne False 
                    
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
                        if mouvement_possible(nb_colonne, nb_ligne, i_clic, j_clic):
                            return False
                    
                    if i == 'P':
                        if pion.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False

                    
                    if i == 'r':    # Pareil mais pour les pieces noires 
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
                        if mouvement_possible(nb_colonne, nb_ligne, i_clic, j_clic):
                            return False

                    if i == 'p':
                        if pion.move_piece(board, player_turn, nb_colonne, nb_ligne, i_clic, j_clic):
                            return False
    
    return True     # si aucune des pieces ne menace la case alors on return True 

def echec(board,player_turn, i_origine,j_origine):
    """
    Détermine si la case du roi est menacé par une autre pièce adverse
    @param board : plateau de jeu en tant que matrice 
    @param player_turn : booléen blanc ou noir 
    @param i_origine, j_origine : coordonnée y, x de la pièce sélectionnée compris entre 0 et 7 inclu
    @return : booléen True/False qui détermine si le roi est en échec 
    """
    return not echec_sur_arrive(board, player_turn, i_origine, j_origine, i_origine, j_origine) # Renvoie True quand le roi adverse est en echec

def echec_et_mat(board,player_turn,i_origine,j_origine):
    """
    Détermine si le roi est en échec et mat, c'est à dire qu'il est en échec et ne peut plus bouger
    @param board : plateau de jeu en tant que matrice 
    @param player_turn : booléen blanc ou noir 
    @param i_origine, j_origine : coordonnée y, x de la pièce sélectionnée compris entre 0 et 7 inclu
    @return : booléen True/False qui détermine si le roi est en échec et mat
    """
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
