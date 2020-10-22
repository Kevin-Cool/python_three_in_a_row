from Board.board import Board
import os

b1 = Board()
while b1.field_state == "playing":
    os.system('cls')

    b1.show_self()
    print("Current player is: ", b1.get_player())
    guess = input("Enter a move: ")

    b1.make_move(guess)

b1.show_self()
print(b1.field_state)