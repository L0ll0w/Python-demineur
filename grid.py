from random import sample

class Grid:
    def __init__(self, niveau):
        self.niveau = niveau
        self.rows, self.cols, self.mines = self.get_dimensions_and_mines()
        self.tableau = []
        self.creer_tableau()

    def get_dimensions_and_mines(self):
        if self.niveau == "Easy":
            return 9, 9, 10
        elif self.niveau == "Medium":
            return 16, 16, 40
        elif self.niveau == "Hard":
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
        except ValueError as e:
            print(e)
            print("Veuillez recommencer.")


if __name__ == "__main__":
    jeu = Game()
    jeu.demarrer()







