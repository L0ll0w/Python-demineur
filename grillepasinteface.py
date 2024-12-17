from random import sample
import pygame
import GrilleIG



grille = GrilleIG.niv
grille = 1



class Grid:
    def __init__(self, niveau):
        self.niv = 0
        self.niveau = niveau
        self.rows, self.cols, self.mines = self.get_dimensions_and_mines()
        self.tableau = []
        self.creer_tableau()

    def get_dimensions_and_mines(self):
        if self.niveau == "Easy":
            self.niv =1
            return 10, 10, 10
        elif self.niveau == "Medium":
            self.niv =2
            return 16, 16, 40
        elif self.niveau == "Hard":
            self.niv = 3
            return 30, 16, 99
        else:
            raise ValueError("Veuillez choisir un niveau entre Easy et Medium ou Hard ! ps( celui qui lit sa et bah il est juif ).")

    def creer_tableau(self):

        self.tableau = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        all_positions = [(i, j) for i in range(self.rows) for j in range(self.cols)]
        mine_positions = sample(all_positions, self.mines)

        for i, j in mine_positions:
            self.tableau[i][j] = 'B'

    def afficher_tableau(self):
        for ligne in self.tableau:
            print(' '.join(str(cell) for cell in ligne))
    def indice_mine(self):
        tab_mine_indice = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.tableau[i][j] == 'B':
                    tab_mine_indice.append((i, j))
        print(f"Position des mines :  {tab_mine_indice}")
        return tab_mine_indice




class Game:
    def __init__(self):
        self.niveau = None
        self.grid = None

    def demander_niveau(self):
        self.niveau = input("Saisissez votre difficulté parmi Easy, Medium, Hard : ")

    def demarrer(self):
        try:
            self.demander_niveau()
            self.grid = Grid(self.niveau)
            self.grid.afficher_tableau()
            self.grid.indice_mine()
        except ValueError as e:
            print(e)
            print("Veuillez recommencer.")


if __name__ == "__main__":

    jeu = Game()
    jeu.demarrer()
