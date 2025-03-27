shopping_list = {
    'piekarnia': ['chleb', 'bułki', 'pączek'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

print("Lista zakupów")

for shop, products in shopping_list.items():
    shop = shop.capitalize()
    products = [product.capitalize() for product in products]
    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {products}.")

products_qty = sum(len(produkty) for produkty in shopping_list.values())
print(f"W sumie kupuję {products_qty} produktów.")
