# ========The beginning of the class==========
from pathlib import Path

# Path to the inventory file next to this script
INVENTORY_PATH = Path(__file__).resolve().parent / "inventory.txt"


class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return (f"Country:  {self.country}\n"
                f"Code:     {self.code}\n"
                f"Product:  {self.product}\n"
                f"Cost:     R{self.cost:.2f}\n"
                f"Quantity: {self.quantity}")


# ===========Shoes list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoes_list = []


# Write shoes_list to inventory.txt
def _write_to_file():
    """
    This function writes the current shoes_list to
    the inventory.txt file, overwriting its contents. It also handles
    exceptions that may occur during the file writing process.
    """
    try:
        with INVENTORY_PATH.open("w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoes_list:
                file.write(f"{shoe.country}, {shoe.code}, {shoe.product}, "
                           f"{shoe.cost}, {shoe.quantity}\n")

    except Exception as e:
        print(f"\nFailed to update inventory file: {e}\n")


# ==========Functions outside the class==============
def read_shoes_data():
    '''
    This function loads data from the inventory.txt file and stores it
    inside the shoes_list.

    The function reads the file line by line (skipping the first line),
    separates each line into its components, creates a Shoe object for
    each line and appends it to the shoes_list.

    The function also handles exceptions for file not found and other
    errors that may arise during file reading.
    '''
    try:
        with INVENTORY_PATH.open("r") as file:
            next(file)  # This skips the first line of the file
            for line in file:
                line = line.strip()
                if not line:
                    continue  # This skips any empty lines in the file
                parts = line.split(",")
                country = parts[0].strip()
                code = parts[1].strip()
                product = parts[2].strip()
                cost = parts[3].strip()
                quantity = parts[4].strip()
                shoe = Shoe(country, code, product, cost, quantity)
                shoes_list.append(shoe)
        print(f"\n {len(shoes_list)} shoes loaded from the inventory. \n")
    except FileNotFoundError:
        print("The file inventory.txt not found."
              "Please verify the file path.\n")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}\n")


def capture_shoes():
    '''
    This function prompts the user to input details for a new shoe,
    creates a Shoe object with the details provided, and appends it to
    the shoes_list.

    There's also error handling to ensure that the cost and quantity
    are valid numbers.
    '''
    print("\n ---- Add New Shoe ----")
    country = input("Country: ").strip()
    code = input("Code (e.g. SKU12345): ").strip()
    product = input("Product: ").strip()

    try:
        cost = float(input("Cost (R): ").strip())
        quantity = int(input("Quantity: ").strip())
    except ValueError:
        print("\nCost and quantity must be numbers. Shoe not added.\n")
        return

    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)
    print(f"\n'{product}' added successfully.\n")

    # Write the updated shoes_list to inventory.txt
    _write_to_file()


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    if not shoes_list:
        print("\nNo shoes in inventory.\n")
        return

    print("\n ---- Shoe Inventory ----")
    for i, shoe in enumerate(shoes_list, 1):  # Starts numbering from 1
        print(f"\n[{i}]")
        print(shoe)
        print("-" * 40)


def re_stock():
    '''
    This function restocks the shoe with the lowest quantity.
    It finds the shoe with the lowest quantity, prompts the user to restock it,
    and updates the quantity. The function also writes the updated
    quantities back to inventory.txt with the 'write_to_file' function.
    '''
    if not shoes_list:
        print("\nNo shoes in inventory to restock.\n")
        return

    # Find the shoe with the lowest quantity
    lowest = min(shoes_list, key=lambda s: s.get_quantity())

    print("\n---- Restock Alert ----\n")
    print(f"Lowest stock: {lowest.product}, "
          f"{lowest.get_quantity()} units left")

    answer = input(
        "Would you like to restock this item? (yes/no): ").strip().lower()
    if answer != "yes":
        print("Restock cancelled.\n")
        return

    try:
        add_quantity = int(input("How many units to add? ").strip())

    except ValueError:
        print("Please enter a valid number.\n")
        return

    lowest.quantity += add_quantity
    print(f"\n{lowest.product} restocked.\n"
          f"New quantity: {lowest.get_quantity()} units.\n")

    # Write the updated quantities back to inventory.txt
    _write_to_file()


def search_shoe():
    '''
    This function finds and displays a shoe by its product code.

    The user is prompted to enter a code, compares it against the codes
    of every shoe in the shoes_list, and if a match is found, it prints
    the details of that shoe, regardless of case.
    If no match is found, it informs the user that the shoe was not
    found.
    '''
    print("\n---- Search Shoe by Code ----")
    code = input("Enter shoe code: ").strip().upper()

    for shoe in shoes_list:
        if shoe.code.upper() == code:
            print("\nShoe found:\n")
            print(shoe)
            print()
            return

    print(f"\nNo shoe found with code '{code}'.\n")


def value_per_item():
    '''
    This function will print the total stock value for every shoe in
    the inventory.

    The total stock value is calculated by multiplying the cost of the
    shoe by the quantity available.

    The results will be displayed in a tabular format, showing the
    product name, cost, quantity and total value for each shoe.
    '''
    if not shoes_list:
        print("\nNo shoes available.\n")
        return

    print("\n---- Value per Item ----")
    print(f"{'Product':<25} {'Cost':>8} {'Quantity':>6} {'Total Value':>12}")
    print("-" * 55)

    for shoe in shoes_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product:<25} R{shoe.get_cost():>7.2f} "
              f"{shoe.get_quantity():>6} R{value:11.2f}")
        print()


def highest_qty():
    '''
    This identifies and displays the shoe with the highest quantity
    in stock.
    '''
    if not shoes_list:
        print("\nNo shoes loaded.\n")
        return

    highest = max(shoes_list, key=lambda s: s.get_quantity())
    print("\n---- Highest Stock Item ----\n")
    print(f"ON SALE:    {highest.product}")
    print(f"Code:       {highest.code}")
    print(f"Quantity:   {highest.get_quantity()} units\n")


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''


def main_menu():
    read_shoes_data()  # Load data drom inventory.txt on startup

    menu = """
    ---- Nike Shoe Inventory System ----
    1. View all Shoes
    2. Add a new shoe
    3. Restock lowest item
    4. Search by code
    5. Value per item
    6. Highest quantity item
    0. Exit
    """

    while True:
        print(menu)
        choice = input("Select an option: ").strip().lower()

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose from the menu.\n")


if __name__ == "__main__":
    main_menu()
