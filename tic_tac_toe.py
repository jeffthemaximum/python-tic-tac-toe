import sys

class Game(object):
	def __init__(self, board):
	#has board, player, turns
		pass

	def instructions():
		pass

	def play():
		pass
		#GAME NEEDS TO GET BOARD.. HOW DO I DO THIS!!!!
		#print board
		#sets current player
		#ask for move
		#checks is move is legal
		#checks for a win

	def game_over():
		pass

class Player(object):
	#can have human or computer players
	pass

class HumanPlayer(Player):
	#an instance of the player class

	def __init__(self, symbol):
		self.symbol = symbol

	def get_move():
		#ask player for move
		pass

class ComputerPlayer(Player):
	#an instance of the player class
	pass

class Board(object):
	#has a list of tiles
	def __init__(self):
		self.tiles = range(9)

	def arrange_board(self):
		board = [self.tiles[0], self.tiles[1], self.tiles[2]], [self.tiles[3], self.tiles[4], self.tiles[5]], [self.tiles[6], self.tiles[7], self.tiles[8]]
		return board

	def print_board(self):
		board = self.arrange_board()
		for row in board:
			sys.stdout.write("|")
			for tile in row:
				sys.stdout.write(str(tile) + "|")
			sys.stdout.write("\n")

class Move(object):
	#has symbol and tile
	#has valid move checker function
	pass
	
player1 = HumanPlayer("X")
player2 = HumanPlayer("O")
my_board = Board();
my_board.print_board()