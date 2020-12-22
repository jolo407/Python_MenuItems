def print_menu():
    print("*" * 30)
    print("  Welcome to PyWarehouse  ")
    print("*" * 30)

    print("[1] Register Product")
    print("[2] View Catalog")
    print("[3] Display out of stock")
    print("[4] Total stock value")
    print('')

    print('[a] Calculate age')
    print('[b] Calculate the tip (15%)')
    print('')

    print("[X] Close the system")

def print_header(header_text):
    clear()
    print('-' *40)
    print(header_text)
    print('-' *40)

def clear():
    print("\n\n\n\n\n")

def print_line():
    print('-' * 25)

def print_product(prod):
    print(
        str(prod.id)
        + " | " + prod.title 
        + " | " + prod.category
        + " | " + str(prod.stock)
        + " | " + str(prod.price)
    )

