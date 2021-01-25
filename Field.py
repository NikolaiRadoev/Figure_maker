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
        n = [
            [self.field[(i, j)] for j in range(self.y-1)]
            for i in range(self.x-1)
        ]
        return n

    def resize_field(self, size_x=None, size_y=None):
        old_f = {}
        old_x = self.x
        old_y = self.y

        for i in range(old_x):
            for j in range(old_y):
                old_f[(i, j)] = self.char

        for i1 in range(old_x):
            for j1 in range(old_y):
                old_f[(i1, j1)] = self.field[(i1, j1)]

        print("Current size x/y: %s" % self.x, self.y)
        if size_x is not None and size_y is not None:
            self.x = size_x
            self.y = size_y
        else:
            self.x = int(input("Enter new x size: "))
            self.y = int(input("Enter new y size: "))

        self.field.clear()
        for i2 in range(self.x):
            for j2 in range(self.y):
                self.field[(i2, j2)] = self.char
        for x1 in range(old_x):
            for y1 in range(old_y):
                self.field[(x1, y1)] = old_f[(x1, y1)]

        print("Successful resizing: %s" % self.x, self.y)
        return self.x, self.y

    def remove_figure(self, choice):
        element = self.all_figures.get(choice)
        if element[0] == 'Rectangle':
            for i in range(element[3]):
                for j in range(element[4]):
                    self.set_cell_symbol(element[1] + i, element[2] + j, self.char)
        else:
            for i in range(element[3]):
                for j in range(i + 1):
                    self.set_cell_symbol(element[1] + i, element[2] + j, self.char)

    def remove_figure_from_list(self, choice):
        self.all_figures.pop(choice)

    def edit_figure(self, choice):
        self.remove_figure(choice)
        element = self.all_figures.get(choice)
        if element[0] == 'Rectangle':
            element[1] = int(input("Enter new X of Rectangle: "))
            element[2] = int(input("Enter new Y of Rectangle: "))
            element[3] = int(input("Enter new HEIGHT of Rectangle: "))
            element[4] = int(input("Enter new WIDTH of Rectangle: "))
            element[5] = input("Enter new SYMBOL of Rectangle: ")

            for i in range(element[3]):
                for j in range(element[4]):
                    self.set_cell_symbol(element[1] + i, element[2] + j, element[5])
        else:
            element[1] = int(input("Enter new X of Triangle: "))
            element[2] = int(input("Enter new Y of Triangle: "))
            element[3] = int(input("Enter new HEIGHT of Triangle: "))
            element[4] = input("Enter new SYMBOL of Triangle: ")

            for i in range(element[3]):
                for j in range(i + 1):
                    self.set_cell_symbol(element[1] + i, element[2] + j, element[4])

    def get_symbol(self, x, y):
        return self.field[(x, y)]

    def __str__(self):
        return str(self.field)
