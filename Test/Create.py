import unittest

from Field import Field
from Figure import Figure


class Create(unittest.TestCase):

    #  For this test enter 2, 1, 4, 6, +
    def test_create_rectangle(self):
        field = Field(9, 9, "n")
        Figure(field).create_new_rectangle(2, 1, 4, 6, "+")
        self.assertEqual(field.get_field(), [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', '+', '+', '+', '+', '+', '+', 'n'],
                                             ['n', '+', '+', '+', '+', '+', '+', 'n'],
                                             ['n', '+', '+', '+', '+', '+', '+', 'n'],
                                             ['n', '+', '+', '+', '+', '+', '+', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']])

    #  For this test enter 0, 0, 3, -
    def test_create_triangle(self):
        field = Field(9, 9, "n")
        Figure(field).create_new_triangle(0, 0, 3, "-")
        self.assertEqual(field.get_field(), [['-', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['-', '-', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['-', '-', '-', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']])

    def test_auto_set(self):
        field = Field(9, 9, "n")
        Figure(field).auto_set()
        self.assertEqual(field.get_field(), [['x', 'x', 'x', 'x', 'x', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['x', 'x', 'x', 'x', 'x', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['x', 'x', 'x', 'x', 'x', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['x', 'x', 'x', 'x', 'xr', 'r', 'r', 'r', 'r', 'r', 'r', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['x', 'x', 'x', 'x', 'xr', 'r', 'r', 'r', 'r', 'r', 'r', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'd', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'd', 'd', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'd', 'd', 'd', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']])


if __name__ == '__main__':
    unittest.main()
