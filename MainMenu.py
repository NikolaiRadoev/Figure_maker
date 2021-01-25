from Figure import Figure


class MainMenu:

    def __init__(self, field):
        self.field = field

    def start(self):
        choice = 0
        while True:
            self.display_menu()
            choice = int(input())
            if choice <= 0:
                print("Have a nice day ;D")
                break
            self.redirect(choice)

    def display_menu(self):
        print("FIGURE-MAKER")
        print("MAIN MENU")
        print("1:Change size")
        print("2:Add new rectangle")
        print("3:Add new triangle")
        print("4:Show list with all figures and their attributes")
        print("5:Delete figure")
        print("6:Edit figure")
        print("7:Draw")
        print("8:Automation set")
        print("0:End")

    def redirect(self, choice):
        """switch = {
            1: ChangeMenu().change_size(self.field),#self.field.change_size(self.field),#"method for 1 option",
            2: CreateFigure(self.field).create_new_rectangle(),#self.field.create_new_rectangle(self.field),#"method for 2 option",
            3: CreateFigure(self.field).create_new_triangle(),#"method for 3 option",
            4: "method for 4 option",
            5: "method for 5 option",
            6: "method for 6 option",
            7: "method for 7 option",
            8: "method for 8 option"
        }
        output = switch.get(choice, Exception("Invalid Number"))
        print(output)"""
        if choice == 1:
            self.field.resize_field()
            print('\n')
        elif choice == 2:
            Figure(self.field).create_new_rectangle()
            self.field.print_field()
            print('\n')
        elif choice == 3:
            Figure(self.field).create_new_triangle()
            self.field.print_field()
            print('\n')
        elif choice == 4:
            Figure(self.field).show_list_with_all_figures()
            print('\n')
        elif choice == 5:
            Figure(self.field).delete_figure_from_field()
            print('\n')
        elif choice == 6:
            Figure(self.field).edit_figure_from_field()
            print('\n')
        elif choice == 7:
            self.field.print_field()
            print('\n')
        elif choice == 8:
            Figure(self.field).auto_set()
            print('\n')
        else:
            print("Invalid Number")
            print('\n')
