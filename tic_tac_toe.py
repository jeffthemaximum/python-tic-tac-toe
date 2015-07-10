import sys
import pudb

class Game(object):
	def __init__(self, board, player1, player2):
		self.board = board
		self.players = [player1, player2]
		self.turn = 0

	def greet_user(self, currplayer):
		print "It's your turn player " + currplayer.symbol

	def play(self):
		flag = False

		while flag == False:
			#GAME NEEDS TO GET BOARD.. HOW DO I DO THIS!!!!
			#set first player to first element in self.players list
			currplayer = self.players[self.turn]
			#print board
			self.board.print_board()
			#great user
			self.greet_user(currplayer)
			#ask for move
			move = Move(self.board, currplayer)
			player_move = move.ask_for_move()
			#move - switch board number to player symbol
			self.board.tiles[player_move] = currplayer.symbol
			#checks for a win
			winner = self.check_win(currplayer.symbol)
			#if win, declare win and break loop
			if winner != False:
				self.game_over(winner)
				flag = True
			#else, switch turns by flipping index in self.players array
			else:
				self.turn = 1 - self.turn

	def check_win(self, player_symbol):
		tiles = self.board.tiles

		for i in range(3):
			if tiles[i] == player_symbol and tiles[i+3] == player_symbol and tiles[i+6] == player_symbol: #check for vertical win
				return player_symbol
			elif tiles[(i*3)] == player_symbol and tiles[(i*3) + 1] == player_symbol and tiles[(i*3) + 2] == player_symbol: #check for horizontal win
				return player_symbol

			#check for diagonal wins
			if tiles[0] == player_symbol and tiles[4] == player_symbol and tiles[8] == player_symbol:
				return player_symbol
			elif tiles[2] == player_symbol and tiles[4] == player_symbol and tiles[6] == player_symbol:
				return player_symbol

    #if no wins, return false
		return False

	def game_over(self, player_symbol):
			print "It's over! Player " + player_symbol + "wins!"

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

	def ask_for_move(self):
		flag = False 
		possible_moves = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

		while (flag != True):
			move = raw_input("Please enter the number where you wanna move your " + self.player.symbol + ":")
			
			#check to see if user entered a number 0-8, if so, convert to int.
			#try to refactor this out
			if move in possible_moves:
				move = int(move)
			else:
				print "please enter valid move"
				return self.ask_for_move()

			#check to see if tile user wants to use is empty, or if someone has already played a piece there.
			#try to refactor this out
			if move != self.board.tiles[move]:
				print "Someone has already moved to that spot. Silly! Move to an open tile."
				return self.ask_for_move()

			return move
				

player1 = HumanPlayer("X")
player2 = HumanPlayer("O")
my_board = Board()
my_game = Game(my_board, player1, player2)
my_game.play()