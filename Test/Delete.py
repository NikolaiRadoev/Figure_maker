import unittest

from Field import Field
from Figure import Figure


class Delete(unittest.TestCase):

    def test_delete_rectangle(self):
        field = Field(9, 9, "n")

        rp = {"height": 4, "width": 6, "symbol": '+'}
        field.create_figure("Rectangle", 0, 3, rp)
        field.delete_figure_from_field(1)

        self.assertEqual(field.get_field(), [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']])

    def test_delete_triangle(self):
        field = Field(9, 9, "n")

        rp = {"height": 4, "symbol": '+'}
        field.create_figure("Triangle", 0, 0, rp)
        field.delete_figure_from_field(1)

        self.assertEqual(field.get_field(), [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']])


if __name__ == '__main__':
    unittest.main()
