class Field:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
        self.field = {}
        self.all_figures = {}
        self.counter = 0

        for i in range(x):
            for j in range(y):
                coord = (i, j)
                self.field[coord] = self.char

    def set_cell_symbol(self, x, y, symbol):
        self.field[(x, y)] = symbol

    def print_field(self):
        for i in range(self.x):
            print()
            for j in range(self.y):
                print(self.field[(i, j)], end=" ")

    def get_field(self):
        n = [[self.field[(i, j)] for j in range(self.y - 1)] for i in range(self.x - 1)]
        return n

    def resize_field(self, size_x, size_y):
        old_f = {}
        old_x = self.x
        old_y = self.y

        for i in range(old_x):
            for j in range(old_y):
                old_f[(i, j)] = self.char

        for i1 in range(old_x):
            for j1 in range(old_y):
                old_f[(i1, j1)] = self.field[(i1, j1)]

        self.x = size_x
        self.y = size_y

        self.field.clear()
        for i2 in range(self.x):
            for j2 in range(self.y):
                self.field[(i2, j2)] = self.char
        for x1 in range(old_x):
            for y1 in range(old_y):
                self.field[(x1, y1)] = old_f[(x1, y1)]

        print("Successful resizing: %s" % self.x, self.y)
        return self.x, self.y

    def create_figure(self, name_of_choice_figure, start_coord_x, start_coord_y, rp):
        if name_of_choice_figure == "Triangle":
            self.create_triangle(
                start_coord_x, start_coord_y, rp["height"], rp["symbol"]
            )
            self.add_triangle_to_list(
                name_of_choice_figure,
                start_coord_x,
                start_coord_y,
                rp["height"],
                rp["symbol"],
            )
        elif name_of_choice_figure == "Rectangle":
            self.create_rectangle(
                start_coord_x, start_coord_y, rp["height"], rp["width"], rp["symbol"]
            )
            self.add_rectangle_to_list(
                name_of_choice_figure,
                start_coord_x,
                start_coord_y,
                rp["height"],
                rp["width"],
                rp["symbol"],
            )
        else:
            print("I don't know how to draw this figure")

    def create_triangle(self, start_coord_x, start_coord_y, height, symbol):
        for i in range(height):
            for j in range(i + 1):
                if self.get_symbol(start_coord_x + i, start_coord_y + j) == self.char:
                    self.set_cell_symbol(start_coord_x + i, start_coord_y + j, symbol)
                else:
                    self.set_cell_symbol(
                        start_coord_x + i,
                        start_coord_y + j,
                        self.get_symbol(start_coord_x + i, start_coord_y + j) + symbol,
                    )

    def create_rectangle(self, start_coord_x, start_coord_y, height, width, symbol):
        for i in range(height):
            for j in range(width):
                if self.get_symbol(start_coord_x + i, start_coord_y + j) == self.char:
                    self.set_cell_symbol(start_coord_x + i, start_coord_y + j, symbol)
                else:
                    self.set_cell_symbol(
                        start_coord_x + i,
                        start_coord_y + j,
                        self.get_symbol(start_coord_x + i, start_coord_y + j) + symbol,
                    )

    def add_rectangle_to_list(
        self, name_of_choice_figure, start_coord_x, start_coord_y, height, width, symbol
    ):
        self.counter += 1
        self.all_figures[self.counter] = [
            name_of_choice_figure,
            start_coord_x,
            start_coord_y,
            height,
            width,
            symbol,
        ]

    def add_triangle_to_list(
        self, name_of_choice_figure, start_coord_x, start_coord_y, height, symbol
    ):
        self.counter += 1
        self.all_figures[self.counter] = [
            name_of_choice_figure,
            start_coord_x,
            start_coord_y,
            height,
            symbol,
        ]

    def delete_figure_from_field(self, num_of_delete):
        if 0 < num_of_delete <= self.counter:
            self.remove_figure(num_of_delete)
            self.remove_figure_from_list(num_of_delete)
            self.show_list_with_all_figures()
        else:
            print("Invalid Number")

    def remove_figure(self, choice):
        element = self.all_figures.get(choice)
        if element[0] == "Rectangle":
            for i in range(element[3]):
                for j in range(element[4]):
                    self.set_cell_symbol(element[1] + i, element[2] + j, self.char)
        elif element[0] == "Triangle":
            for i in range(element[3]):
                for j in range(i + 1):
                    self.set_cell_symbol(element[1] + i, element[2] + j, self.char)
        else:
            print("Wrong num of delete")

    def remove_figure_from_list(self, choice):
        self.all_figures.pop(choice)

    def edit_figure_from_field(
        self, num_of_edit, start_coord_x, start_coord_y, input_for_edit
    ):
        if 0 < num_of_edit <= self.counter:
            self.edit_figure(num_of_edit, start_coord_x, start_coord_y, input_for_edit)
            self.show_list_with_all_figures()
        else:
            print("Invalid Number")

    def edit_figure(self, choice, start_coord_x, start_coord_y, input_for_edit):
        self.remove_figure(choice)
        element = self.all_figures.get(choice)
        if element[0] == "Rectangle":
            element[1] = start_coord_x
            element[2] = start_coord_y
            element[3] = input_for_edit["height"]
            element[4] = input_for_edit["width"]
            element[5] = input_for_edit["symbol"]

            for i in range(element[3]):
                for j in range(element[4]):
                    self.set_cell_symbol(element[1] + i, element[2] + j, element[5])
        elif element[0] == "Triangle":
            element[1] = start_coord_x
            element[2] = start_coord_y
            element[3] = input_for_edit["height"]
            element[4] = input_for_edit["symbol"]

            for i in range(element[3]):
                for j in range(i + 1):
                    self.set_cell_symbol(element[1] + i, element[2] + j, element[4])
        else:
            print("I don't know which figure to edit")

    def get_symbol(self, x, y):
        return self.field[(x, y)]

    def show_list_with_all_figures(self):
        if len(self.all_figures) == 0:
            print("There are NO items in the list")
        else:
            print(self.all_figures)

    def name_of_figure_from_list(self, choice):
        if len(self.all_figures) == 0:
            print("There are NO items in the list")
        else:
            element = self.all_figures.get(choice)
            return element[0]

    def auto_set(self):
        self.resize_field(20, 20)
        self.create_rectangle(0, 0, 5, 5, "x")
        self.create_rectangle(3, 4, 2, 7, "r")
        self.create_triangle(10, 10, 3, "d")
        self.print_field()

    def __str__(self):
        return str(self.field)
