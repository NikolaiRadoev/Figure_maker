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

        rp = {"height": 4, "width": 6, "symbol": '-'}
        field.create_figure("Rectangle", 0, 0, rp)
        #  For this test enter 1 and 2, 1, 4, 6, +
        input_for_edit = {"height": 4, "width": 6, "symbol": '+'}
        field.edit_figure(1, 2, 1, input_for_edit)

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

        rp = {"height": 4, "symbol": '+'}
        field.create_figure("Triangle", 0, 0, rp)
        #  For this test enter 1 and 2, 1, 4, -
        input_for_edit = {"height": 4, "symbol": '-'}
        field.edit_figure(1, 2, 1, input_for_edit)

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
