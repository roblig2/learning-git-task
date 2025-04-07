shopping_list = {
    'piekarnia': ['chleb', 'bułki', 'pączek'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

print("Lista zakupów")

total_products = 0

for shop, products in shopping_list.items():
    shop = shop.capitalize()
    products = [product.capitalize() for product in products]
    total_products += len(products)
    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {products}.")

print(f"W sumie kupuję {total_products} produktów.")
