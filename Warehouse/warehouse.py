#imports
from menu import print_menu, print_header, clear, print_line, print_product
from homework import calculate_age, calculate_tip
from product import Product

#global vars
catalog = []



#functions





def register_product():
    try:
        # title, category, stock, price
        print_header(" Register a new Product")
        title = input("Please provide the Title ")
        category = input("Please provide the Category: ")
        stock = int(input("Please provide the Stock: "))
        price = float(input("Please provide the Price: "))

        # create object
        the_product = Product(0, title, category, stock, price)
        



        #add obj to a list
        catalog.append(the_product)

        print_line()
        print("** Product Registered!!")

    except:
        print_line()
        print("** Error: verify values and try again!")


def print_catalog():
    print_header(" Current Catalog ")

    for prod in catalog: 
        print_product(prod)


def out_of_stock():
    print_header("Currently Out of Stock")

    for prod in catalog:
        if(prod.stock == 0):
            print_product(prod)


def total_stock():
    print_header(" Total Stock Value ")
    total=0

    for prod in catalog:
        total = total + (prod.stock * prod.price)

    print(total)






    
        
    


    

    







#instructions

opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input("PLease choose an option: ")

    if(opc == '1'):
        register_product()

    elif(opc == '2'):
        print_catalog()

    elif(opc == '3'):
        out_of_stock()

    elif(opc == '4'):
        total_stock()

    

    elif(opc =='a'):
        calculate_age()
    elif(opc =='b'):
        calculate_tip()

    input("Press Enter to continue...")



print("Good bye!!")
