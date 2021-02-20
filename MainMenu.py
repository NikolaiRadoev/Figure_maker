from Figure import Figure


class MainMenu(object):
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
            try:
                self.redirect(choice)
            except ValueError as e:
                print("An error occured: %s" % e)

    def display_menu(self):
        print("FIGURE-MAKER")
        print("MAIN MENU")
        print("1:Change size")
        print("2:Add new figure")
        print("3:Show list with all figures and their attributes")
        print("4:Delete figure")
        print("5:Edit figure")
        print("6:Draw")
        print("7:Automation set")
        print("0:End")

    def show_field_figures(self):
        if not self.field.all_figures:
            print("Field is empty")
        else:
            print(self.field.all_figures)

    def redirect(self, choice):
        if choice == 1:
            print("Current size x/y: %s" % self.field.x, self.field.y)
            new_start_coord_x = int(input("Enter new x coord: "))
            new_start_coord_y = int(input("Enter new y coord: "))
            self.field.resize_field(new_start_coord_x, new_start_coord_y)
            print("\n")

        elif choice == 2:
            figure_name = input("What you want to draw: ")
            if figure_name not in Figure.get_figure_map():
                raise ValueError(
                    "Can't find this figure. Possible options are: %s"
                    % Figure.get_figure_map().keys()
                )
            x = int(input("Enter x coord of %s: " % figure_name))
            y = int(input("Enter y coord of %s: " % figure_name))
            rp = self.collect_figure_input(figure_name)
            self.field.create_figure(figure_name, x, y, rp)

        elif choice == 3:
            self.show_field_figures()
            print("\n")

        elif choice == 4:
            if len(self.field.all_figures) == 0:
                print("There are NO items to DELETE in the list")
            else:
                self.show_field_figures()
                num_of_delete = int(input("Enter num of figure to delete: "))
                self.field.delete_figure(num_of_delete)
                print("\n")

        elif choice == 5:
            if len(self.field.all_figures) == 0:
                print("There are NO items to EDIT in the list")
            else:
                self.show_field_figures()
                num_of_edit = int(input("Enter num of figure to edit: "))

                if not self.field.has_figure(num_of_edit):
                    print("Invalid number")
                    return

                figure = self.field.get_figure(num_of_edit)
                name = figure.name
                x = int(input("Enter x coord: "))
                y = int(input("Enter y coord: "))
                input_for_edit = self.collect_figure_input(name)
                self.field.edit_figure(num_of_edit, x, y, input_for_edit)
                print("\n")

        elif choice == 6:
            self.field.print_field()
            print("\n")

        elif choice == 7:
            self.field.auto_set()
            self.field.print_field()
            print("\n")

        else:
            print("Invalid Number")
            print("\n")

    def collect_figure_input(self, name_of_figure):
        return {
            field_name: field_type(
                input("Enter %s of %s: " % (field_name, name_of_figure))
            )
            for field_name, field_type in Figure.get_required_fields(name_of_figure)
        }
