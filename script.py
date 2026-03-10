def main():
    products = ['apple', 'banana']
    prices = [1.2, 0.8]
    quantities = [10, 20]
    inv = create_inventory(products, prices, quantities)
    print(get_product_info(inv, 'banana'))
    print(calculate_total_inventory_value(inv))
    bulk_update_quantities(inv, {'apple': 5, 'banana': 10})
    print(inv)
    remove_product(inv, 'banana')
    print(inv)
    apply_discount(inv, 10)
    print(inv)

def create_inventory(products, prices, quantities):
    inv = {}
    for product, price, qty in zip(products, prices, quantities): #zip wurde von pycharm vorgeschlagen
        inv[product] = {
            'id': f"{product}_{len(inv)+1:03}",
            'price': price,
            'quantity': qty
        }
    return inv

def get_product_info(inventory, product_name):
    try:
        return inventory[product_name]
    except:
        print('Error: Product not found')

def calculate_total_inventory_value(inventory):
    value = 0
    for i in inventory:
        value += inventory[i]['price']
    return value

def remove_product(inventory, product_name):
    try:
        del inventory[product_name]
        return inventory
    except:
        print('Error: Product not found')

def apply_discount(inventory, percentage):
    for item in inventory:
        inventory[item]['price'] *= (1 - percentage/100)

def low_stock_alert(inventory, threshold):
    low_stock = []
    for item in inventory:
        if inventory[item]['quantity'] < threshold:
            low_stock.append(item)
    return low_stock

def bulk_update_quantities(inventory, quantities):
    for name in quantities:
        try:
            inventory[name]['quantity'] = quantities[name]
        except:
            print(f'Error: {name} not found')

if __name__ == "__main__":
    main()