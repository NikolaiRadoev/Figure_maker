import unittest
from Field import Field
from Figure import Figure


class Edit(unittest.TestCase):
    def test_change_menu_with_input_10_10(self):
        field = Field(9, 9, "+")
        field.resize_field(10, 10)
        self.assertEqual(field.get_field(), [['+', '+', '+', '+', '+', '+', '+', '+', '+'],
                                             ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
                                             ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
                                             ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
                                             ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
                                             ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
                                             ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
                                             ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
                                             ['+', '+', '+', '+', '+', '+', '+', '+', '+']])

    def test_edit_rectangle_from_field(self):
        field = Field(9, 9, 'n')

        Figure(field).create_new_rectangle(0, 0, 3, 3, "-")
        #  For this test enter 1 and 2, 1, 4, 6, +
        Figure(field).edit_figure_from_field()

        self.assertEqual(field.get_field(), [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', '+', '+', '+', '+', '+', '+', 'n'],
                                             ['n', '+', '+', '+', '+', '+', '+', 'n'],
                                             ['n', '+', '+', '+', '+', '+', '+', 'n'],
                                             ['n', '+', '+', '+', '+', '+', '+', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']])

    def test_edit_triangle_from_field(self):
        field = Field(9, 9, 'n')

        Figure(field).create_new_triangle(0, 0, 3, "+")
        #  For this test enter 1 and 2, 1, 4, -
        Figure(field).edit_figure_from_field()

        self.assertEqual(field.get_field(), [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', '-', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', '-', '-', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', '-', '-', '-', 'n', 'n', 'n', 'n'],
                                             ['n', '-', '-', '-', '-', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                                             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']])


if __name__ == '__main__':
    unittest.main()
