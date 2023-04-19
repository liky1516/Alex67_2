# C2.3 Реализация игра "Тир"

from random import randint


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

# создадим класс цели, который будет хранить стоимость в очках
class HitMark:
	def __init__(self, cost) -> None:
		self.setCost(cost)

	def setCost(self, cost):
		self.cost = cost

	def getCost(self):
		return self.cost


# класс “прямоугольной” цели, наследуемый от класса прямоугольника и класса цели,
# который включает как форму, так и стоимость
class RectangleHitMark(Rectangle, HitMark):
	def __init__(self, pos, width, height, cost) -> None:
		super().__init__(pos, width, height)
		HitMark.setCost(self, cost)

# создадим отдельный класс сообщений и назовем его GameEvent.
# Он будет служить «коробочкой», в которую будут передаваться сообщения между графикой и логикой.
# У класса GameEvent будут поля тип и данные, а также несколько общих констант, определяющих тип сообщения.
class GameEvent:
	# пустое событие
	Event_None = 0
	# событие таймера
	Event_Tick = 1
	# событие “выстрела” по цели
	Event_Hit = 2
	def __init__(self, type, data) -> None:
		self.type = type
		self.data = data

	def getType(self):
		return self.type

	def getData(self):
		return self.data

# сщздадим класс игровой логики GameLogic. Он будет включать всю внутриигровую логику нашей игры,
# которая состоит всего из двух действий:
# нахождение пересечения клика пользователя с фигурой;
# подсчёт очков.
class GameLogic:
	def __init__(self, w, h) -> None:
		self.gameboard_width = w   # ширина игрового поля
		self.gameboard_height = h  # высота игрового поля
		self.marks = []            # массив активных целей на доске
		self.hitMarks = []         # массив пораженных целей
		self.score = 0             # полученные очки

	# метод обработки сообщений, которые приходят к игровой логике
	def processEvent(self, event):
		# если событие таймер, то добавляем еще одну цель к списку активных целей
		if event.type == GameEvent.Event_Tick:
			# на случайной позиции в пределах игровой доски
			markRandPos = Pos(rnd.randint(20, self.gameboard_width - 20), rnd.randint(20, self.gameboard_height - 20))
			# случайного размера от 10 до 20
			markSize = rnd.randint(10, 20)
			# стоимость цели обратно пропорциональна размеру
			markCost = 30 - markSize
			# случайный цвет цели в формате RGB
			markColor = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
			mark = RectangleHitMark(markRandPos, markSize, markSize, markCost)
			mark.setColor(markColor)
			# добавляем цель на доске
			self.addHitMark(mark)

		# если сообщение “выстрел в цель”, то обрабатываем эту ситуацию
		# используя позицию pos, переданную от интерфейса
		if event.type == GameEvent.Event_Hit:
			self.hit(event.data)

	# метод, который добавляет цель
	def addHitMark(self, mark):
		self.marks.append(mark)

	# метод попадания на доске
	def hit(self, pos):
		# перебираем все цели, и если метод isInside возвращает True
		# добавляем стоимость цели к счету и перемещаем ее из списка активных целей в пораженные
		for markIndex in range(len(self.marks)):
			mark = self.marks[markIndex]
			if mark.isInside(pos.x, pos.y):
				self.score += mark.getCost()
				self.marks.pop(markIndex)
				self.hitMarks.append(mark)
				break

	# метод возвращает все активные цели на доске
	def getBoard(self):
		return self.marks

	# метод возвращает счёт очков
	def getScore(self):
		return self.score


# графический класс
class PyGameGui:
	def __init__(self, w, h, logic) -> None:
		self.w = w   # ширина окна
		self.h = h   # высота окна
		self.logic = logic   # логика игры в виде внутреннего объекта
		self.screen = pygame.display.set_mode([self.main_w, self.main_h])   # окно pygame
		self.font = pygame.font.SysFont("Consolas", 30)   # шрифт для отображения счета

	# метод, который запускает игру
	def run(self):
		running = True
		# устанавливаем таймер pygame на 1 сек
		pygame.time.set_timer(pygame.USEREVENT + GameEvent.Event_Tick, 1000)
		# создаем бесконечный цикл обработки сообщений от пользователя
		while running:
			# если пользователь закрыл окно, то завершаем обработку событий и заканчиваем игру
			# иначе обрабатываем сообщение
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				else:
					self.processEvent(event)
			# выполняем отрисовку
			self.draw()

	# метод обработки сообщений от интерфейса
	def processEvent(self, event):
		# если событие таймера, то переделываем событие pygame в события нашей игры GameEvent
		if (event.type >= pygame.USEREVENT) and (event.type < pygame.NUMEVENTS):
			myevent = GameEvent()
			myevent.type = event.type - pygame.USEREVENT
			self.logic.processEvent(myevent)

		# если событие клик мышкой, то передаём позицию клика в сообщении Hit
		if event.type == pygame.MOUSEBUTTONDOWN:
			pypos = event.pos
			myevent = GameEvent(GameEvent.Event_Hit, Pos(pypos[0], pypos[1]))
			self.logic.processEvent(myevent)

# метод отрисовки доски
def draw(self):
	# заполняем фон
	self.screen.fill((255, 255, 255))
	# получаем все активные цели на доске и отрисовываем их в виде прямоугольников соответствующего цвета
	marks = self.logic.getBoard()
	for mark in marks:
		pygame.draw.rect(self.screen,mark.getColor(), pygame.Rect(mark.getPos().x, mark.getPos().y, mark.getWidth(), mark.getHeight()))

	# получаем текущие очки
	score = self.logic.getScore()
	# отображаем счёт на окне
	self.screen.blit(self.font.render(f'score:{score}', True, (0, 0, 0)), (32, 48))

	pygame.display.flip()


	# Запуск
	if __name__ == "__main__":
		pygame.init()
		width = 800
		height = 600
		gui = PyGameGui(width, height, GameLogic(width, height))
		gui.run()
		pygame.quit()


