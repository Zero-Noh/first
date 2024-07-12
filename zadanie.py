import requests

response = requests.get("https://fakestoreapi.com/products/categories")
categories = response.json()
print("Категории товаров:")
for category in categories:
    print(category)

chosen_category = input("Введите категорию товаров: ")
response = requests.get(f"https://fakestoreapi.com/products/category/{chosen_category}")
products = response.json()

print(f"Товары в категории '{chosen_category}':")
for product in products:
    print(f"Название: {product['title']}")
    print(f"Цена: {product['price']}")
    print(f"Описание: {product['description']}")