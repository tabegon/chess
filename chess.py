import tkinter as tk
import pion
import fou
import cavalier
import tour
import dame
import roi


class Game():
    """
    La classe game permet :
    - d'afficher le plateau
    - de demander les coups
    - de déplacer les pièces
    """
    def __init__(self):
        
        self.LARGEUR, self.HAUTEUR = 640, 640 #Largeur et hauteur sont des constantes qui donnent la taille de l'échiquier graphique
        # le dictionnaire Symbols permet de convertir les pièces en leur symbole unicode
        self.SYMBOLS = {'K': '\u2654',
                        'Q': '\u2655',
                        'R': '\u2656',
                        'B': '\u2657',
                        'N': '\u2658',
                        'P': '\u2659',
                        'k': '\u265A',
                        'q': '\u265B',
                        'r': '\u265C',
                        'b': '\u265D',
                        'n': '\u265E',
                        'p': '\u265F',
                        ' ': ' '}
        # La liste de strings Pieces permet de placer les pièces en début de partie
        self.PIECES = ['RNBKQBNR',
                       'PPPPPPPP',
                       '        ',
                       '        ',
                       '        ',
                       '        ',
                       'pppppppp',
                       'rnbkqbnr']
        # La variable board est une liste de listes qui permet de savoir où sont disposées les pièces sur l'échiquier
        self.board = self.place_pieces(self.PIECES)

        """ Elements anticipés pour les élèves """
        self.selected_piece = None  # Variable pour stocker les coordonnées de la pièce sélectionnée
        self.player_turn = 'w'  # Variable pour stocker la couleur du joueur actif
        """ ---------------------------------- """

        self.fenetre = tk.Tk()
        self.grille = tk.Canvas(self.fenetre, height=self.HAUTEUR, width=self.LARGEUR, background='white')
        self.grille.pack()

    def place_pieces(self, disposition: [str]): # type: ignore
        """
        Permet d'initialiser le plateau de jeu à une certaine position (type : position initiale)
        données : disposition est une liste de str
        résultat : board est une liste de listes
        """
        board = []
        for no_ligne in range(len(self.PIECES)):
            ligne = []
            for no_colonne in range(len(self.PIECES[no_ligne])):
                ligne.append(self.PIECES[no_ligne][no_colonne])
            board.append(ligne)
        print(board)
        return board

    def show_board(self):
        """
        IHM : Permet d'afficher le plateau de jeu dans le shell
        données : On utilise self.board
        résultat : Aucun, le plateau est affiché
        """
        print("-"*(4*8+1))
        for line in self.board:
            line_to_show = "|"
            for case in line:
                line_to_show += ' '+self.SYMBOLS[case] + ' |'
            print(line_to_show)
            print("-"*(4*8+1))

    def draw_board(self):
        """
        IHM : Permet d'afficher le plateau de jeu en mode graphique
        données : On utilise self.board
        résultat : Aucun, le plateau est affiché
        """
        largeur = self.LARGEUR // len(self.board)
        hauteur = self.HAUTEUR // len(self.board[0])
        colors = '#739552', '#EBECD0'
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                color_code = (i+j) % 2

                # Vérifier si la case est la pièce sélectionnée.
                if (i, j) == self.selected_piece:
                    # Utiliser une couleur de surbrillance pour la pièce sélectionnée.
                    fill_color = '#BACB43'
                else:
                    fill_color = colors[color_code]

                #On dessine la grille en traçant des rectangles :
                self.grille.create_rectangle(largeur*i, hauteur*j, largeur*(i+1), hauteur*(j+1), fill=fill_color)
                #On utilise les symboles Unicodes pour représenter les pièces :
                self.grille.create_text(largeur*(i+0.5), hauteur*(j+0.5), text=self.SYMBOLS[self.board[j][i]], font='Pecita 48')

    def choix_piece(self, event):
        """
        IHM : Permet d'afficher le plateau de jeu dans le shell
        données : event donne les coordonnées du clic de la souris
        résultat : Aucun, le plateau est affiché
        """
        #print(event.__dict__)
        i_clic = event.x * 8 // self.LARGEUR
        j_clic = event.y * 8 // self.HAUTEUR

        if self.selected_piece is None:
            # Si aucune pièce n'a été sélectionnée, enregistrez les coordonnées de la pièce.
            self.selected_piece = (i_clic, j_clic)
            # On identifie de quelle pièce il s'agit
            piece = self.board[j_clic][i_clic]
            if piece in 'Rr':
                tour.identification(i_clic, j_clic)
            if piece in 'Nn':
                cavalier.identification(i_clic, j_clic)
            if piece in 'Bb':
                fou.identification(i_clic, j_clic)
            if piece in 'Qq':
                dame.identification(i_clic, j_clic)
            if piece in 'Kk':
                roi.identification(i_clic, j_clic)
            if piece in 'Pp':
                pion.identification(i_clic, j_clic)
        else:
            i_origine, j_origine = self.selected_piece
            # Si une pièce a déjà été sélectionnée, c'est le moment de déplacer la pièce.
            resultat = False  # Par défaut, si on a cliqué sur une case vide par exemple
            if self.board[j_origine][i_origine] in 'Rr':
                # Appel de la fonction de test de déplacement de la tour
                resultat = tour.move_piece(self.board,
                                           self.player_turn,
                                           i_origine,
                                           j_origine,
                                           i_clic,
                                           j_clic)
            if self.board[j_origine][i_origine] in 'Nn':
                # Appel de la fonction de test de déplacement du cavalier
                resultat = cavalier.move_piece(self.board,
                                           self.player_turn,
                                           i_origine,
                                           j_origine,
                                           i_clic,
                                           j_clic)
            if self.board[j_origine][i_origine] in 'Bb':
                # Appel de la fonction de test de déplacement du fou
                resultat = fou.move_piece(self.board,
                                           self.player_turn,
                                           i_origine,
                                           j_origine,
                                           i_clic,
                                           j_clic)
            if self.board[j_origine][i_origine] in 'Qq':
                # Appel de la fonction de test de déplacement de la dame
                resultat = dame.move_piece(self.board,
                                           self.player_turn,
                                           i_origine,
                                           j_origine,
                                           i_clic,
                                           j_clic)
            if self.board[j_origine][i_origine] in 'Kk':
                # Appel de la fonction de test de déplacement du roi
                resultat = roi.move_piece(self.board,
                                           self.player_turn,
                                           i_origine,
                                           j_origine,
                                           i_clic,
                                           j_clic)
            if self.board[j_origine][i_origine] in 'Pp':
                # Appel de la fonction de test de déplacement du pion
                resultat = pion.move_piece(self.board,
                                           self.player_turn,
                                           i_origine,
                                           j_origine,
                                           i_clic,
                                           j_clic)
                
            if resultat:  # Rappel : resultat vaut True après les test du module Pion
                print("Le déplacement est autorisé")
                #  Déplacement de la pièce à l'endroit du clic
                self.board[j_clic][i_clic] = self.board[j_origine][i_origine]
                #  Suppression de la pièce de son ancien emplacement
                self.board[j_origine][i_origine] = ' '
                #  Changement de joueur
                if self.player_turn == 'w':
                    self.player_turn = 'b' 
                elif self.player_turn == 'b':
                    self.player_turn = 'w'
                else :
                    raise Exception("Un problème avec player_turn")
                print("Player_turn : ",self.player_turn)
            elif resultat == "echec":
                print("échec")
            elif resultat == "pat":
                print("pat")
            elif resultat == "echec_et_mat":
                print("échec et mat")
            else:
                print("Le déplacement est refusé")

            #  Quelque soit la situation (bon coup ou mauvais coup), on
            #   annule la pièce sélectionnée
            self.selected_piece = None

        #  Refraichissement du plateau
        self.draw_board()


partie = Game()
partie.show_board()

partie.draw_board()

partie.fenetre.bind("<Button-1>", partie.choix_piece)

partie.fenetre.mainloop()
