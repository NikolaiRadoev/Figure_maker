from Figure import Figure


class Field:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
        self.all_figures = {}
        self.counter = 0

        self.refresh_field()

    def set_cell_symbol(self, x, y, symbol):
        self.field[(x, y)] = symbol

    def refresh_field(self):
        field = {}

        for key in sorted(self.all_figures.keys()):
            figure, x, y = self.all_figures[key]
            for i in range(x, x + figure.height):
                for j in range(y, y + figure.width):
                    symbol = figure.get_symbol(i - x, j - y)
                    if symbol:
                        field[(i, j)] = symbol

        self.field = field

    def print_field(self):
        for i in range(self.x):
            print()
            for j in range(self.y):
                print(self.field.get((i, j), self.char), end=" ")

    def get_field(self):
        n = [[self.field[(i, j)] for j in range(self.y - 1)] for i in range(self.x - 1)]
        return n

    def resize_field(self, size_x, size_y):
        self.x = size_x
        self.y = size_y

        self.refresh_field()

    def get_figure(self, position):
        return self.all_figures[position][0]

    def has_figure(self, position):
        return position in self.all_figures

    def create_figure(self, name, x, y, figure_kwargs, position=None):
        figure = Figure.create_figure(name, figure_kwargs)

        if not position:
            self.counter += 1
            position = self.counter

        self.all_figures[position] = [
            figure,
            x,
            y,
        ]

        self.refresh_field()

    def delete_figure(self, position):
        if position not in self.all_figures:
            raise ValueError("Invalid Number")

        figure = self.all_figures.pop(position)[0]

        self.refresh_field()

        return figure

    def edit_figure(self, position, x, y, figure_kwargs):
        if position not in self.all_figures:
            raise ValueError("Invalid Number")

        deleted_figure = self.delete_figure(position)

        self.create_figure(
            deleted_figure.name,
            x,
            y,
            figure_kwargs,
            position=position,
        )

        self.refresh_field()

    def get_symbol(self, x, y):
        return self.field[(x, y)]

    def name_of_figure_from_list(self, choice):
        if len(self.all_figures) == 0:
            print("There are NO items in the list")
        else:
            element = self.all_figures.get(choice)
            return element[0]

    def auto_set(self):
        self.resize_field(20, 20)

        self.create_figure("Rectangle", 0, 0, {"width": 5, "height": 5, "symbol": "x"})
        self.create_figure("Rectangle", 3, 4, {"width": 2, "height": 7, "symbol": "r"})
        self.create_figure("Triangle", 10, 10, {"height": 3, "symbol": "d"})
        self.create_figure("Circle", 5, 5, {"radius": 5, "symbol": "A"})

    def __str__(self):
        return str(self.field)
