import numpy as np


class Board:
    def __init__(self):
        self.field = np.array([(-1, -1, -1), (-1, -1, -1), (-1, -1, -1)])
        self.placing_X = True
        self.field_state = "playing"

    def show_self(self):
        print("    1 2 3")
        abc = "ABC"
        for i in self.field:
            print(abc[0], "[", end=" ")
            abc = abc[1:]
            for k in i:
                if k == -1:
                    print("_", end=" ")
                if k == 0:
                    print("O", end=" ")
                if k == 1:
                    print("X", end=" ")
            print("]")

    def make_move(self, c):
        # check for correct formatting:
        if len(c) == 2:
            if ("A" in c[0] or "B" in c[0] or "C" in c[0]) and ("1" in c[1] or "2" in c[1] or "3" in c[1]) :
                # translating to usable coordinates
                # x:
                if c[0] == "A":
                    x = 0
                if c[0] == "B":
                    x = 1
                if c[0] == "C":
                    x = 2
                # y:
                if c[1] == "1":
                    y = 0
                if c[1] == "2":
                    y = 1
                if c[1] == "3":
                    y = 2
                # placing an X or O on the board:
                if self.field[x][y] == -1 and self.field_state == "playing":
                    if self.placing_X:
                        self.field[x][y] = 1
                    else:
                        self.field[x][y] = 0
                    self.placing_X = not self.placing_X
                self.check_game_state()

    def get_player(self):
        return "X" if self.placing_X == True else "O"

    def check_game_state(self):
        # check for row win:
        if [1, 1, 1] in self.field.tolist():
            self.field_state = "X won (row)"
        if [0, 0, 0] in self.field.tolist():
            self.field_state = "O won (row)"
        # check for columns  win:
        if [1, 1, 1] in self.field.T.tolist():
            self.field_state = "X won (column)"
        if [0, 0, 0] in self.field.T.tolist():
            self.field_state = "O won (column)"
        # check for diagonal  win:
        if np.diag(self.field).tolist() == [0, 0, 0] or np.diag(np.fliplr(self.field)).tolist() == [0, 0, 0]:
            self.field_state = "O won (diagonal)"
        if np.diag(self.field).tolist() == [1, 1, 1] or np.diag(np.fliplr(self.field)).tolist() == [1, 1, 1]:
            self.field_state = "X won (diagonal)"
