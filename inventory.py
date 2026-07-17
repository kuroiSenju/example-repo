# ========The beginning of the class==========
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


# ===========Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# Write shoe_list to inventory.txt
def _write_to_file():
    try:
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country}, {shoe.code}, {shoe.product},"
                           f"{shoe.cost}, {shoe.quantity}\n")

    except Exception as e:
        print(f"\nFailed to update inventory file: {e}\n")


# ==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file
    represents data to create one object of shoes.
    You must use the try-except in this function for error handling.
    Remember to skip the first line using your code.
    '''
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # This skips the first line of the file
            for line in file:
                line = line.strip()
                if not line:
                    continue  # This skips any empty lines in the file
                parts = line.split(",")
                country = parts[0]
                code = parts[1]
                product = parts[2]
                cost = parts[3]
                quantity = parts[4]
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
        print(f"\n {len(shoe_list)} shoes loaded from the inventory. \n")
    except FileNotFoundError:
        print("The file inventory.txt not found."
              "Please verify the file path.\n")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}\n")


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
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
    shoe_list.append(shoe)
    print(f"\n'{product}' added successfully.\n")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    if not shoe_list:
        print("\nNo shoes in inventory.\n")
        return

    print("\n ---- Shoe Inventory ----")
    for i, shoe in enumerate(shoe_list, 1):  # Starts numbering from 1
        print(f"\n[{i}]")
        print(shoe)
        print("-" * 40)


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    if not shoe_list:
        print("\nNo shoes in inventory to restock.\n")
        return

    # Find the shoe with the lowest quantity
    lowest = min(shoe_list, key=lambda s: s.get_quantity())

    print("\n---- Restock Alert ----\n")
    print(f"Lowest stock: {lowest.get_product()}"
          f"({lowest.get_quantity()} units)")

    answer = input(
        "Would you like to restock this item? (yes/no): :").strip().lower()
    if answer != "yes":
        print("Restock cancelled.\n")
        return

    try:
        add_quantity = int(input("How many units to add? ").strip())
    except ValueError:
        print("Please enter a valid number.\n")
        return

    lowest.quantity += add_quantity
    print(f"\n{lowest.get_product()} restocked.\n"
          f"New quantity: {lowest.get_quantity()} units.\n")

    # Write the updated quantities back to inventory.txt
    _write_to_file()


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    print("\n---- Search Shoe by Code ----")
    code = input("Enter shoe code: ").strip().upper()

    for shoe in shoe_list:
        if shoe.code.upper() == code:
            print("\nShoe found:\n")
            print(shoe)
            print()
            return

    print(f"\nNo shoe found with code '{code}'.\n")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    if not shoe_list:
        print("\nNo shoes available.\n")
        return

    print("\n---- Value per Item ----")
    print(f"{'Product':<25} {'Cost':>8} {'Quantity':>6} {'Total Value':>12}")
    print("-" * 55)

    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product:<25} R{shoe.get_cost():>7.2f} "
              f"{shoe.get_quantity():>6} R{value:11.2f}")
        print()


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    if not shoe_list:
        print("\nNo shoes loaded.\n")
        return

    highest = max(shoe_list, key=lambda s: s.get_quantity())
    print("\n---- Highest Stock Item ----\n")
    print(f" ON SALE:   {highest.get_product()}))")
    print(f" Code:      {highest.code()}")
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
