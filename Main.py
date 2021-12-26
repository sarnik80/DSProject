from Person import Person
from Person import Gender
from consolemenu import *
from consolemenu.items import *
from DataBase import data_base

all_person = []


def get_name_of_db():
    return input('Enter name of db : ')


def create_db():
    while True:
        try:
            nameDB = get_name_of_db()
            my_bd = data_base(name_db=nameDB)
        except TypeError as err:
            print(err)
        else:
            return my_bd


def create_or_use_database():
    my_bd = create_db()
    global all_person
    all_person = my_bd.find_all_person()
    # create tree with all person function


def add_person():
    name = input('enter name of person : ')


# Create the menu
menu = ConsoleMenu("Family Tree", "Choose one of the options : ")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem(
    "Open File", create_or_use_database,
)

function_item_2 = FunctionItem(
    "add Person", add_person
)

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu([])
selection_menu.append_item(function_item_2)

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Person Menu", selection_menu, menu)
# Once we're done creating them, we just add the items to the menu

menu.append_item(function_item)
menu.append_item(function_item_2)
menu.append_item(submenu_item)
menu.show()
