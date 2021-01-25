import unittest

from Field import Field
from Figure import Figure


class Delete(unittest.TestCase):

    def test_delete_rectangle(self):
        field = Field(9, 9, "n")

        Figure(field).create_new_rectangle(0, 0, 3, 3, "+")
        Figure(field).delete_figure_from_field(1)

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

        Figure(field).create_new_triangle(0, 0, 3, "-")
        Figure(field).delete_figure_from_field(1)

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
