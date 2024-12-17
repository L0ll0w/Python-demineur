from random import sample


class Grid:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.tableau = self.creer_tableau()
        self.mettre_a_jour_grille()

    def creer_tableau(self):
        """
        Crée une grille vide avec des mines placées aléatoirement.
        Les mines sont représentées par 'B'.
        """
        tableau = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        mines_positions = sample([(i, j) for i in range(self.rows) for j in range(self.cols)], self.mines)
        for i, j in mines_positions:
            tableau[i][j] = 'B'
        return tableau

    def mettre_a_jour_grille(self):
        """
        Met à jour la grille pour que chaque case contienne le nombre de mines adjacentes.
        Les cases contenant des mines restent inchangées ('B').
        """
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(self.rows):
            for j in range(self.cols):
                if self.tableau[i][j] == 'B':
                    continue

                # Compter les mines adjacentes
                mines_adjacentes = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < self.rows and 0 <= nj < self.cols and self.tableau[ni][nj] == 'B':
                        mines_adjacentes += 1

                # Mettre à jour la case si aucune mine n'est adjacente
                if mines_adjacentes > 0:
                    self.tableau[i][j] = mines_adjacentes

    def indice_mine(self):
        """
        Retourne les coordonnées des mines dans la grille.
        """
        return [(i, j) for i in range(self.rows) for j in range(self.cols) if self.tableau[i][j] == 'B']

    def sauvegarder_grille(self, chemin):
        """
        Sauvegarde la grille actuelle dans un fichier pour pouvoir la recharger plus tard.
        """
        with open(chemin, 'w') as f:
            for ligne in self.tableau:
                f.write(' '.join(str(cell) for cell in ligne) + '\n')