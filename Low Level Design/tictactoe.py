class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        
    def display(self):
        for row in self.grid:
            print("\n".join("|".join(row) for row in self.grid))
            print("-" * (2 * self.size - 1))

    def place_move(self, row, col, symbol):
        if self.grid[row][col] == ' ':
            self.grid[row][col] = symbol
            return True
        return False
    
    def check_win(self, symbol):
        n = self.size

        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True
            
        for col in range(n):
            if all(self.grid[row][col] == symbol for row in range(n)):
                return True
            
        if all(self.grid[i][i] == symbol for i in range(n)):
            return True
    
        if all(self.grid[i][n - i - 1] == symbol for i in range(n)):
            return True
        
        return False
    
    def is_full(self):
        return all(cell != " " for row in self.grid for cell in row)
    
class Game:
    def __init__(self, player1, player2, size = 3):
        self.board = Board(size)
        self.players = [player1, player2]
        self.current_turn = 0

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_turn]
            print(f"{current_player.name}'s turn ({current_player.symbol})")

            row, col = map(int, input("Enter row and col(0 indexed):").split())

            if not self.board.place_move(row, col, current_player.symbol):
                print("Invalid move")
                continue

            if self.board.check_win(current_player.symbol):
                self.board.display()
                print(f"{current_player.name} wins!")
                break
            
            if self.board.is_full():
                self.board.display()
                print("Its a draw")
                break

            self.switch_turn()

if __name__ == "__main__":
    p1 = Player("Alice", "X")
    p2 = Player("Bob", "O")
    game = Game(p1, p2, size = 3)
    game.play()


'''
TRACING :

for a tic tac toe game, we need three classes - 
Player
Board
Game

For Player, the states are name and symbol

For Board, the states are grid and size(default 3)
and the behaviours that we need are 
1. Display the board whenever we want to see the state of the board
2. Place the player's move on the board
3. Check if there is a winner by checking the row, column, diagonal and anti-diagonal
4. Check if the board is full to see if there is a draw

For Game, the states are board, players[] and currentTurn
and the behaviours are 
1. Play, to commence the game
2. Switching turns
'''
