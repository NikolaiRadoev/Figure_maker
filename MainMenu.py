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
            self.redirect(choice)

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

    def redirect(self, choice):
        if choice == 1:
            print("Current size x/y: %s" % self.field.x, self.field.y)
            new_start_coord_x = int(input("Enter new x coord: "))
            new_start_coord_y = int(input("Enter new y coord: "))
            self.field.resize_field(new_start_coord_x, new_start_coord_y)
            print("\n")

        elif choice == 2:
            name_of_choice_figure = input("What you want to draw: ")
            if not Figure().list_with_figures.__contains__(name_of_choice_figure):
                print("can't find this figure")
            else:
                start_coord_x = int(
                    input("Enter x coord of %s: " % name_of_choice_figure)
                )
                start_coord_y = int(
                    input("Enter y coord of %s: " % name_of_choice_figure)
                )
                rp = self.collect_figure_input(name_of_choice_figure)
                self.field.create_figure(
                    name_of_choice_figure, start_coord_x, start_coord_y, rp
                )

        elif choice == 3:
            self.field.show_list_with_all_figures()
            print("\n")

        elif choice == 4:
            if len(self.field.all_figures) == 0:
                print("There are NO items to DELETE in the list")
            else:
                self.field.show_list_with_all_figures()
                num_of_delete = int(input("Enter num of figure to delete: "))
                self.field.delete_figure_from_field(num_of_delete)
                print("\n")

        elif choice == 5:
            if len(self.field.all_figures) == 0:
                print("There are NO items to EDIT in the list")
            else:
                self.field.show_list_with_all_figures()
                num_of_edit = int(input("Enter num of figure to edit: "))
                name = self.field.name_of_figure_from_list(num_of_edit)
                start_coord_x = int(input("Enter x coord: "))
                start_coord_y = int(input("Enter y coord: "))
                input_for_edit = self.collect_figure_input(name)
                self.field.edit_figure_from_field(
                    num_of_edit, start_coord_x, start_coord_y, input_for_edit
                )
                print("\n")

        elif choice == 6:
            self.field.print_field()
            print("\n")

        elif choice == 7:
            self.field.auto_set()
            print("\n")

        else:
            print("Invalid Number")
            print("\n")

    def collect_figure_input(self, name_of_figure):
        return {
            field_name: field_type(
                input("Enter %s of %s: " % (field_name, name_of_figure))
            )
            for field_name, field_type in Figure().required_fields(name_of_figure)
        }
