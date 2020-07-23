import ast
import random
from tree_search import get_groups, get_combinations

class Bcolors:
    VIOLET = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class SwitchesGame:
    """ Each switch changes the state of itself and the adiacent ones (no diagonals) """
    def __init__(self, size, rand):
        self.size = int(size)
        self.values = [-1] * self.size ** 2
        self.rand = True if rand == "y" else False
        if self.rand:
            self.board = random.choices(population=[0, 1], k=self.size**2)
        else:
            self.board = ast.literal_eval(input("Please input the board as a list of 0-1: "))
        print("\nS W I T C H E S")
        self.print_board()
        self.groups = get_groups(self.size)
        get_combinations(self.values, self.board, self.groups)
        self.update_board()
        print("Game solved!")

    def print_board(self):
        space = 4
        print("\n", end="")
        for idx, it in enumerate(self.board):
            if it == 1:
                print(f"{Bcolors.GREEN}|{Bcolors.ENDC}" + " " * space, end="")
            else:
                print(f"{Bcolors.RED}O{Bcolors.ENDC}" + " " * space, end="")
            if (idx + 1) % self.size == 0:
                print("\n")
        print("*" * ((space+1) * (self.size - 1) + 1))

    def update_board(self):
        for idx, it in enumerate(self.values):
            if it == 1:
                group = self.groups[idx+1]
                for it2 in group:
                    self.board[it2-1] = 1 if self.board[it2-1] == 0 else 0
                self.print_board()


if __name__ == "__main__":
    # print(f"{Bcolors.WARNING}Warning: No active frommets remain. Continue?{Bcolors.ENDC}")
    size = input("Board size: ")
    rand = input("Random initial state? (y/n) ")
    sg = SwitchesGame(size, rand)