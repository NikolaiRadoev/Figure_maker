class Figure(object):
    def __init__(self, field):
        self.field = field

    def create_new_rectangle(self, start_coord_x=None, start_coord_y=None, height=None, width=None, symbol=None):
        if start_coord_x is not None and start_coord_y is not None and height is not None and width is not None and symbol is not None:
            start_coord_x = start_coord_x
            start_coord_y = start_coord_y
            height = height
            width = width
            symbol = symbol
        else:
            start_coord_x = int(input("Enter start X point of rectangle: "))
            start_coord_y = int(input("Enter start Y point of rectangle: "))
            height = int(input("Enter HEIGHT of rectangle: "))
            width = int(input("Enter WIDTH of rectangle: "))
            symbol = input("Enter SYMBOL for visualization: ")

        self.add_rectangle_to_list("Rectangle", start_coord_x, start_coord_y, height, width, symbol)

        for i in range(height):
            for j in range(width):
                if self.field.get_symbol(start_coord_x + i, start_coord_y + j) == self.field.char:
                    self.field.set_cell_symbol(start_coord_x + i, start_coord_y + j,
                                               symbol)  # self.field.field[(start_coord_x + i, start_coord_y + j)] = symbol  # 'Field' object does not support item assignment
                else:
                    self.field.set_cell_symbol(start_coord_x + i, start_coord_y + j,
                                               self.field.get_symbol(start_coord_x + i, start_coord_y + j) + symbol)
        #self.field.print_field()

    def create_new_triangle(self, start_coord_x=None, start_coord_y=None, height=None, symbol=None):
        if start_coord_x is not None and start_coord_y is not None and height is not None and symbol is not None:
            start_coord_x = start_coord_x
            start_coord_y = start_coord_y
            height = height
            symbol = symbol
        else:
            start_coord_x = int(input("Enter start X point of triangle: "))
            start_coord_y = int(input("Enter start Y point of triangle: "))
            height = int(input("Enter HEIGHT of triangle: "))
            symbol = input("Enter SYMBOL for visualization: ")

        self.add_triangle_to_list("Triangle", start_coord_x, start_coord_y, height, symbol)

        for i in range(height):
            for j in range(i + 1):
                if self.field.get_symbol(start_coord_x + i, start_coord_y + j) == self.field.char:
                    self.field.set_cell_symbol(start_coord_x + i, start_coord_y + j, symbol)
                else:
                    self.field.set_cell_symbol(start_coord_x + i, start_coord_y + j,
                                               self.field.get_symbol(start_coord_x + i, start_coord_y + j) + symbol)
        #self.field.print_field()

    def show_list_with_all_figures(self):
        if len(self.field.all_figures) == 0:
            print("There are NO items in the list")
        else:
            print(self.field.all_figures)

    def add_rectangle_to_list(self, name, x, y, h, w, s):
        self.field.counter += 1
        self.field.all_figures[self.field.counter] = [name, x, y, h, w, s]

    def add_triangle_to_list(self, name, x, y, h, s):
        self.field.counter += 1
        self.field.all_figures[self.field.counter] = [name, x, y, h, s]

    def delete_figure_from_field(self, choice=None):
        if len(self.field.all_figures) == 0:
            print("There are NO items to DELETE in the list")
        else:
            self.show_list_with_all_figures()

            if choice is not None:
                choice = choice
            else:
                choice = int(input("Enter number of element which you want to DELETE: "))

            if choice > 0 or choice <= self.field.counter:
                self.field.remove_figure(choice)
                self.field.remove_figure_from_list(choice)
                self.show_list_with_all_figures()
            else:
                print("Invalid Number")

    def edit_figure_from_field(self):
        if len(self.field.all_figures) == 0:
            print("There are NO items to EDIT in the list")
        else:
            self.show_list_with_all_figures()

            choice = int(input("Enter number of element which you want to EDIT: "))

            if choice > 0 or choice <= self.field.counter:
                self.field.edit_figure(choice)
                self.show_list_with_all_figures()
            else:
                print("Invalid Number")

    def auto_set(self):
        self.field.resize_field(20, 20)
        self.create_new_rectangle(0, 0, 5, 5, "x")
        self.create_new_rectangle(3, 4, 2, 7, "r")
        self.create_new_triangle(10, 10, 3, "d")
        self.field.print_field()