import json
import os


class Product:
    name: str
    price: float
    description: str
    quantity: int
    product_count = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity



class Category:
    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.products)

    @classmethod
    def reset_counts(self):
        self.category_count = 0
        self.product_count = 0



    @classmethod
    def load_data_from_json(self, file_path: str):
        file_path = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            categories = []

            for category_data in data:
                products = []
                for product_data in category_data['products']:
                    product = Product(
                        name=product_data['name'],
                        description=product_data['description'],
                        price=product_data['price'],
                        quantity=product_data['quantity']
                    )
                    products.append(product)

                category = Category(
                    name=category_data['name'],
                    description=category_data['description'],
                    products=products
                )
                categories.append(category)

            return categories

        except FileNotFoundError:
            print(f"Ошибка: файл '{file_path}' не найден.")
            return None  # Возвращаем None, если файл не найден
        except json.JSONDecodeError:
            print("Ошибка: неправильно отформатированный JSON.")
            return None  # Возвращаем None, если JSON некорректен
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None


file_path = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")
categories = Category.load_data_from_json(file_path)

if categories:
    for category in categories:
        print(
            f'Категория: {category.name}, Описание: {category.description}, Количество продуктов: {len(category.products)}')
        for product in category.products:
            print(
                f'Продукт: {product.name}, Описание: {product.description}, Цена: {product.price}, Количество: {product.quantity}')
