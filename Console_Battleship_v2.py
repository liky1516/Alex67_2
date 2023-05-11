from enum import Enum
import random


# ________________________________________________________________
class CellState(Enum):
	EMPTY = 0
	MISS = 1
	HIT = 2
	SHIP = 3


# ________________________________________________________________
class Player:
	def __init__(self, name):
		self.name = name


# ________________________________________________________________

class User(Player):
	pass


class Computer(Player):
	pass


class Dot:
	def __init__(self, x, y, state=CellState.EMPTY):
		self.x = x
		self.y = y
		self.state = state

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __str__(self):
		if self.state == CellState.EMPTY:
			return '0'
		elif self.state == CellState.HIT:
			return 'X'
		elif self.state == CellState.SHIP:
			return '■'
		else:
			return '.'
# def __str__(self):
# 	return f" {self.x}, {self.y}"


# ________________________________________________________________
class Ship:
	def __init__(self, x, y, size, turn, state=CellState.SHIP):
		self.x = x
		self.y = y
		self.size = size
		self.turn = turn # поворот корабля: 0 - горизонтально, 1 - вертикально
		self.state = state
		self.dots = []
		self.lives = size

	def get_ship_dots(self):
		return self.dots

	def ship_dots(self):
		for i in range(self.size):
			self.dots.append([Dot(self.x + i, self.y, CellState.SHIP)]) if self.turn == 0 \
				else self.dots.append([Dot(self.x, self.y + i, CellState.SHIP)])


# class Field:
# 	def __init__(self):
# 		self.cells = [[Dot(x, y, state=CellState.EMPTY) for x in range(1, 7)] for y in range(1, 7)]
# 		self.ships = Field.list_ships
#
# 	# self.list_ships()
# 	@staticmethod
# 	def list_ships():
# 		ships = [
# 			Ship(random.randint(1, 6), random.randint(1, 6), 3, random.randint(0, 1)),
# 			Ship(random.randint(1, 6), random.randint(1, 6), 2, random.randint(0, 1)),
# 			Ship(random.randint(1, 6), random.randint(1, 6), 2, random.randint(0, 1)),
# 			Ship(random.randint(1, 6), random.randint(1, 6), 1, 0),
# 			Ship(random.randint(1, 6), random.randint(1, 6), 1, 0),
# 			Ship(random.randint(1, 6), random.randint(1, 6), 1, 0),
# 			Ship(random.randint(1, 6), random.randint(1, 6), 1, 0)
# 		]
#
# 	def show_field(self):
# 		print()
# 		print('    | 1 | 2 | 3 | 4 | 5 | 6 |')
# 		print('    _________________________')
# 		for i, row in enumerate(self.cells):
# 			row_str = f"  {i + 1} | {' | '.join(map(str, row))} | "
# 			print(row_str)
# 			print('    _________________________')
#
# 	def add_ship(self, ship):
# 		pass


# ________________________________________________________________

s = Ship(1, 1, 3, 0)
s.ship_dots()
# print(tuple(map(str, s.get_dots())))

# if __name__ == "__main__":
# 	fil = Field()
# 	fil.show_field()
