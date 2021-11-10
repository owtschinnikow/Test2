import pygame
from enum import Enum

FPS = 60
CELL_SIZE = 50

class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Класс игрока содержащий тип значков и имя.
    """
    def __init__(self, name, cell_type):
        self.name = name  # запоминает имя
        self.cell_type = cell_type  # запоминает тип значка для игрока


class GameFild:
    """
    Класс отвечающий за модель поля
    """
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID] * self.width for i in range(self.height)]


class GameFieldView:
    """
    Класс отвечающий за отображение поля.
    Отображает поле на экране.
    Выясняет место клика.
    """
    def __init__(self, field):
        # загрузить картинки значков клеток
        # отобразить первое состояние поля
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):  # нарисовать поле
        pass

    def check_coords_correst(self, x, y):  # проверяет что координаты в поле
        return True  # TODO: self._height учесть

    def get_coords(self, x, y):  # вычисление координат клика в поле
        return 0, 0  # TODO: реально вычислить



class GameRoundManager:
    """
    Менеджер игрыб запускающий все процессы.
    """

    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]  # определение списка игроков
        self.current_player = 0  # определение текущего игрока
        self.field = GameFild()

    def handle_click(self, i, j):
        player = self._players[self.current_player]
        # игрок делает клик на поле
        print('handle_click', i, j)


class GameWindow:
    """
    Содержит виджет поля,
    а так же менеджер игрового раунда.
    """

    def __init__(self):
        pygame.init()  # инициализация pygame

        # Window
        self._width = 800  # задание ширины
        self._height = 600  # задание высоты
        self._title = "Crosses & Zeroes"  # задание названия
        self._screen = pygame.display.set_mode((self._width, self._height))  # создание экранного поля
        pygame.display.set_caption(self._title)  # создание названия
        # clock = pygame.time.Clock()

        player1 = Player('Петя', Cell.CROSS)  # хранение игроков и типов
        player2 = Player('Вася', Cell.ZERO)  # хранение игроков и типов
        self._game_manager = GameRoundManager(player1, player2)  # создание менеджера
        self._field_widget = GameFieldView(self._game_manager.field)  # создание поля

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:  # игровой цикл
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # проверка окончания игры
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:  # ловим нажатие мыши
                    mouse_pos = pygame.mouse.get_pos()  # ловим координаты мыши
                    x, y = mouse_pos
                    if self._field_widget.check_coords_correst(x, y):  # проверяем находится ли кординаты в поле
                        i, j = self._field_widget.get_coords(x, y)  # вытаскиваем координаты x, y в массиве
                        self._game_manager.handle_click(i, j)
            pygame.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print('Game over!')


if __name__ == '__main__':
    main()
