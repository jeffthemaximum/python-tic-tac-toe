import sys
import pudb

class Game(object):
	def __init__(self, board, player1, player2):
		self.board = board
		self.players = [player1, player2]
		self.turn = 0

	def instructions():
		pass

	def play(self):
		pass
		#GAME NEEDS TO GET BOARD.. HOW DO I DO THIS!!!!
		#set first player to first element in self.players list
		currplayer = self.players[self.turn]
		#print board
		self.board.print_board()
		#ask for move
		move = Move(self.board, currplayer)
		move.greet_user()
		player_move = move.ask_for_move()
		#move
		#switch player
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
		move = 0
		while (move == 0):
			print("It's your move player " + self.symbol)

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
	def __init__(self, board, player):
		self.board = board
		self.player = player

	def greet_user(self):
		print "It's your turn player " + self.player.symbol

	def ask_for_move(self):
		flag = False 
		possible_moves = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

		while (flag != True):
			move = raw_input("Please enter the number where you wanna move your " + self.player.symbol + ":")
			
			if move in possible_moves:
				move = int(move)
			else:
				print "please enter valid move"
				self.ask_for_move()

			#check to see if tile user wants to use is empty

			flag = True
			
				

	#has valid move checker function
	pass

player1 = HumanPlayer("X")
player2 = HumanPlayer("O")
my_board = Board()
my_game = Game(my_board, player1, player2)
my_game.play()