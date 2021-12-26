from consolemenu import *
from consolemenu.items import *
import Main

# menu of my project

# Create the menu
menu = ConsoleMenu("Family Tree Menu", ">>>Choose one of the options<<<")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem(
    "Open File", Main.create_or_use_database,
)

function_item_2 = FunctionItem(
    "Creat Person ", Main.add_person
)

function_item_3 = FunctionItem(
    "Set Name", Main.get_name_person
)

function_item_4 = FunctionItem(
    "Set Id", Main.get_id_person
)

function_item_5 = FunctionItem(
    'Set Gender', Main.get_gender
)

function_item_6 = FunctionItem(
    'Add To Tree', Main.add_tree_to_db
)

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu([])
selection_menu.append_item(function_item_2)
selection_menu.append_item(function_item_3)
selection_menu.append_item(function_item_4)
selection_menu.append_item(function_item_5)


# marital status menu :)


# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Person Menu", selection_menu, menu)
# Once we're done creating them, we just add the items to the menu

married_selection_menu = SelectionMenu(['Single'])
married_sub_menu = SubmenuItem('Marital Status', married_selection_menu, menu)
function_item_is_married = FunctionItem(
    'Married', Main.get_id_spouse
)


married_selection_menu.append_item(function_item_is_married)
selection_menu.append_item(married_sub_menu)
selection_menu.append_item(function_item_6)
menu.append_item(function_item)
menu.append_item(submenu_item)
menu.show()
