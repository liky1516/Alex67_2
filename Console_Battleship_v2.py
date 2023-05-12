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

	def __eq__(self, other_x, other_y):
		return self.x == other_x and self.y == other_y

	def __str__(self):
		if self.state == CellState.EMPTY:
			return '0'
		elif self.state == CellState.HIT:
			return 'X'
		elif self.state == CellState.SHIP:
			return '■'
		else:
			return '.'


# ________________________________________________________________
class Ship:
	def __init__(self, x, y, size, turn, state=CellState.SHIP):
		self.x = x
		self.y = y
		self.size = size
		self.turn = turn  # поворот корабля: 0 - горизонтально, 1 - вертикально
		self.state = state
		self.dots = []
		self.lives = size

	# def __getitem__(self, item):
	# 	for i in range(self.dots):
	# 		return self.dots[i]

	def ship_dots(self):
		for i in range(self.size):
			self.dots.append(Dot(self.x + i, self.y, CellState.SHIP)) if self.turn == 0 \
				else self.dots.append(Dot(self.x, self.y + i, CellState.SHIP))


class Field:
	def __init__(self, hid=True, living_ships=7):
		self.hid = hid
		self.living_ships = living_ships
		self.cells = [[Dot(x, y, state=CellState.EMPTY) for x in range(1, 7)] for y in range(1, 7)]
		self.ships = Field.list_ships(self)
		for i in self.ships:
			i.ship_dots()




	def list_ships(self):
		return [
			Ship(random.randint(1, 6), random.randint(1, 6), 3, random.randint(0, 1)),
			Ship(random.randint(1, 6), random.randint(1, 6), 2, random.randint(0, 1)),
			Ship(random.randint(1, 6), random.randint(1, 6), 2, random.randint(0, 1)),
			Ship(random.randint(1, 6), random.randint(1, 6), 1, 0),
			Ship(random.randint(1, 6), random.randint(1, 6), 1, 0),
			Ship(random.randint(1, 6), random.randint(1, 6), 1, 0),
			Ship(random.randint(1, 6), random.randint(1, 6), 1, 0)
		]

	def show_field(self):
		print()
		print('    | 1 | 2 | 3 | 4 | 5 | 6 |')
		print('    _________________________')
		for i, row in enumerate(self.cells):
			row_str = f"  {i + 1} | {' | '.join(map(str, row))} | "
			print(row_str)
			print('    _________________________')

	def add_ship(self):
		for dot in self.ships:
			# if (dot.y - 1) < 1 or (dot.y - 1) > 6 \
			# 	or (dot.x - 1) < 1 or (dot.x - 1) > 6:
			# 	raise ValueError ('Invalid ship location')
			# if dot.turn == 0 and dot.x + (dot.size - 1) > 6:
			# 	raise ValueError("Ship goes out of bounds")
			# if dot.turn == 1 and dot.y + (dot.size - 1) > 6:
			# 	raise ValueError("Ship goes out of bounds")

			self.cells[dot.y - 1][dot.x - 1].state = CellState.SHIP




# ________________________________________________________________
# s = Ship(1, 1, 3, 0)
# s.ship_dots()
# print(s.get_ship_dots())
# print(tuple(map(str, s.get_dots())))

if __name__ == "__main__":
	fil = Field()
	fil.add_ship()
	fil.show_field()
	# fil.add_ship()




# s = Ship(1, 1, 3, 0)
# print(tuple(map(str, s.get_dots())))
