class Field:
	def __init__(self):
		self.field = [['O'] * 6 for i in range(1,7)]

	def show_field(self):
		print()
		print('    | 1 | 2 | 3 | 4 | 5 | 6 |')
		print('    _________________________')
		for i, j in enumerate(self.field):
			row_str = f"  {i + 1} | {' | '.join(j)} | "
			print(row_str)
			print('    _________________________')
		print()


if __name__ == "__main__":
	fil = Field()
	fil.show_field()