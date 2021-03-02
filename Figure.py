class Figure(object):
    @property
    def name(self):
        return self.__class__.__name__

    def __repr__(self):
        return "%s(%s)" % (
            self.name,
            ", ".join(
                [
                    "%s=%s" % (arg_name, getattr(self, arg_name))
                    for arg_name, arg_type in self._required_fields()
                ]
            ),
        )

    @classmethod
    def get_figure_map(cls):
        return {subclass.__name__: subclass for subclass in cls.__subclasses__()}

    @classmethod
    def create_figure(cls, figure_name, kw_args):
        figure_map = cls.get_figure_map()
        assert figure_name in figure_map, "Figure not found"

        subclass = figure_map[figure_name]
        return subclass(**kw_args)

    @classmethod
    def get_required_fields(cls, figure_name):
        figure_class = cls.get_figure_map()[figure_name]
        return figure_class._required_fields()


class Triangle(Figure):
    def __init__(self, symbol, height):
        self.symbol = symbol
        self.height = height
        self.width = height

    def area(self, x1, y1, x2, y2, x3, y3):
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

    def is_inside(self, x1, y1, x2, y2, x3, y3, x, y):
        # Calculate area of triangle ABC
        A = self.area(x1, y1, x2, y2, x3, y3)

        # Calculate area of triangle PBC
        A1 = self.area(x, y, x2, y2, x3, y3)

        # Calculate area of triangle PAC
        A2 = self.area(x1, y1, x, y, x3, y3)

        # Calculate area of triangle PAB
        A3 = self.area(x1, y1, x2, y2, x, y)

        # Check if sum of A1, A2 and A3
        # is same as A
        return A == A1 + A2 + A3

    @staticmethod
    def _required_fields():
        return [
            ("height", int),
            ("symbol", str),
        ]

    def get_symbol(self, x, y):
        # 1 0 0
        # 1 1 0
        # 1 1 1
        if self.is_inside(
                x1=self.height - 1,
                y1=0,
                x2=0,
                y2=0,
                x3=self.height - 1,
                y3=self.height - 1,
                x=x,
                y=y,
        ):
            return self.symbol
        # 1 1 1
        # 0 1 1
        # 0 0 1
        """if self.is_inside(
            x1=0,
            y1=0,
            x2=0,
            y2=self.height - 1,
            x3=self.height - 1,
            y3=self.height - 1,
            x=x,
            y=y,
        ):
            return self.symbol"""


class Rectangle(Figure):
    def __init__(self, symbol, height, width):
        self.symbol = symbol
        self.height = height
        self.width = width

    @staticmethod
    def _required_fields():
        return [
            ("height", int),
            ("width", int),
            ("symbol", str),
        ]

    def get_symbol(self, x, y):
        # 1 1 1
        # 1 1 1
        # 1 1 1
        if 0 <= x < self.height and 0 <= y < self.width:
            return self.symbol


class Circle(Figure):
    def __init__(self, symbol, radius):
        self.symbol = symbol
        self.radius = radius
        self.height = radius * 2 + 1
        self.width = radius * 2 + 1

    @staticmethod
    def _required_fields():
        return [
            ("radius", int),
            ("symbol", str),
        ]

    def get_symbol(self, x, y):
        coords = set()

        width, height = self.width, self.height
        a, b = self.radius, self.radius
        r = self.radius
        EPSILON = 2.2

        # draw the circle
        for _y in range(height):
            for _x in range(width):
                # see if we're close to (x-a)**2 + (y-b)**2 == r**2
                if abs((_x - a) ** 2 + (_y - b) ** 2 - r ** 2) < EPSILON ** 2:
                    coords.add((_x, _y))

        if (x, y) in coords:
            return self.symbol
