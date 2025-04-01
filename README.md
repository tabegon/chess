# chess
## Cahier des charges de la reine

Pièce : Reine

- Comportement de la pièce
    
    La pièce de la Reine peut se déplacer verticalement, horizontalement, et diagonalement. Elle ne peut pas sauter une pièce (de sa propre équipe comme de l’autre) et est donc obliger de s’arrête avant son pion ou avant le pion adverse si le joueur ne désire pas manger. 
    
    Pour manger, la Reine doit donc avoir dans son rayon d’action une pièce de l’équipe adverse (sans obstacles devant). Il lui suffit donc d’aller sur sa case afin de la manger, l’éliminer. La Reine ne peut donc pas manger une pièce se situant derrière une autre pièce.
    
- Gestion du plateau à faire
    
    La pièce de la Reine est limité par le périmètre du plateau soit 8*8. Elle ne peut donc pas sortir de cette zone. Ainsi, si la Reine se situe dans un angle, elle se voit contraint de se déplacer seulement dans la direction “libre” soit vers le plateau.
    
- Interaction avec les autres composants
    
    La Reine est vulnérable, elle peut comme toutes les pièces (sauf le roi)  se faire manger si elle se situe en “danger”. Elle peut donc se déplacer dans un zone “dangereuse”, contrôlé par une pièce adverse sans en être contraint.
    
- Fonction
