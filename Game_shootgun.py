# C2.3 Реализация игра "Тир"
from turtle import color, width


# класс позиции элемента
class Pos:
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y

# абстрактный класс - класс произвольной фигуры с полями позиция и цвет
class Figure:
	def __init__(self, pos) -> None:
		self.setPos(pos)
		self.setColor(0)

	def setPos(self, pos):
		self.pos = pos

	def getPos(self):
		return self.pos

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color

	#метод, который намекает на “форму” — при выполнении метода класс возвращает True, если
    #точка, переданная х и у, лежит внутри фигуры и False в противном случае
    #поскольку класс Figure “не имеет” формы, то всегда возвращает False
	def isInside(self, x, y) -> bool:
		return False

# класс прямоугольника с шириной и высотой
class Rectangle(Figure):
	def __init__(self, pos, width, height):
		super().__init__(pos)
		self.width = width
		self.height = height

	# isInside в этом случае возвращает True, если точка лежит между границами прямоугольника
	def isInside(self, x, y) -> bool:
		_pos = super().getPos()
		if (_pos.x < x) and ((_pos.x + self.width) > x) and (_pos.y < y) and ((_pos.y + self.height) > y):
			return True
		else:
			return False


