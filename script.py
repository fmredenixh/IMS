def main():
    products = ['apple', 'banana']
    prices = [1.2, 0.8]
    quantities = [10, 20]
    inv = create_inventory(products, prices, quantities)
    print(get_product_info(inv, 'appple'))

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


if __name__ == "__main__":
    main()