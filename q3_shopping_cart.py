
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))          # ['apple']
print(add_item("banana"))         # ['apple', 'banana']
print(add_item("milk", ["bread"]))# ['bread', 'milk']
print(add_item("eggs"))           # ['apple', 'banana', 'eggs']


def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart



def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}

def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})

def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price 
    except TypeError as e:
        print("Error:", e)

def calculate_total(cart):
    total = sum(i["price"] * i["qty"] for i in cart["items"])
    return total * (1 - cart["discount"] / 100)


cart1 = create_cart("Aarav", 10)
cart2 = create_cart("Diya")

add_to_cart(cart1, "Laptop", 50000)
add_to_cart(cart1, "Mouse", 500, 2)

add_to_cart(cart2, "Book", 300, 3)

print(cart1)
print("Total:", calculate_total(cart1))

print(cart2)
print("Total:", calculate_total(cart2))

update_price((100,), 200)

