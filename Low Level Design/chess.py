from abc import ABC, abstractmethod

class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.current_turn = player1
        self.status = "IN PROGRESS"

    def make_move(self, start, end):
        pass

class Board:
    def __init__(self):
        self.squares = [[Square(i, j) for j in range(8)] for i in range(8)]

    def get_square(self, x, y):
        return self.squares[x][y]
    
    def move_piece(self, start, end):
        pass

class Square:
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece

class Piece(ABC):
    def __init__(self, colour):
        self.colour = colour
        self.killed = False

    @abstractmethod
    def can_move(self, board, start, end):
        pass

class Player:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

class Move:
    def __init__(self, player, start, end, piece_moved, piece_killed = None):
        self.player = player
        self.start = start
        self.end = end
        self.piece_moved = piece_moved
        self.piece_killed = piece_killed

class Pawn(Piece):
    def enpassant():
        pass

    def promotion():
        pass

    def can_move(self, board, start, end):
        return super().can_move(board, start, end)

class King(Piece):
    def castle():
        pass

    def can_move(self, board, start, end):
        return super().can_move(board, start, end)

class Queen(Piece):
    
    def can_move(self, board, start, end):
        return super().can_move(board, start, end)

class Knight(Piece):
    def can_move(self, board, start, end):
        return super().can_move(board, start, end)

class Bishop(Piece):
    def can_move(self, board, start, end):
        return super().can_move(board, start, end)

class Rook(Piece):
    def can_move(self, board, start, end):
        return super().can_move(board, start, end)

