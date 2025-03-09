def menu():
    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")
    print("Taco Palace Menu")
    print("1. Tacos - $5.00")
    print("2. Burrito - $7.50")
    print("3. Nachos - $4.00")
    print("4. Soft Drink - $1.50")
    print("5. Quit")

def results():
    order = []
    prices = [5.00, 7.50, 4.00, 1.50]
    total = 0
    while True:
        options = input("Enter the menu number of the item you'd like to order (or 'quit' to finish): ")
        if options.lower() == 'quit':
            break
        elif options.isdigit() and 1 <= int(options) <= 4:
            item = int(options) - 1
            order.append(item)
            total += prices[item]
        elif options.isdigit() and int(options) == 5:
            break
        else:
            print("Invalid selection. Please try again.")
    return order, total

def print_receipt(order, total):
    menu_items = ["Tacos", "Burrito", "Nachos", "Soft Drink"]
    if order:
        item_names = []
        for item in order:
            item_names.append(menu_items[item])
        print(f"\nYou ordered a {', '.join(item_names)}. Your total is ${total:.2f}")
    else:
        print("You didn't order anything. Your total is $0.00")

menu()
order, total = results()
print_receipt(order, total)


