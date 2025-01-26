import json
from typing import Any

from config import file_path
from src.category import Category
from src.product import Product


def load_data_from_json(file_path: str) -> list[Any]:
    """Функция читает файл и создает объекты классов."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        categories = []
        for category_data in data:
            products = []
            for product_data in category_data.get("products", []):
                price = product_data.get("price")
                if not isinstance(price, (int, float)):
                    raise ValueError(f"Некорректная цена: {price}")
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=price,
                    quantity=product_data["quantity"],
                )
                products.append(product)

            category = Category(
                name=category_data["name"], description=category_data["description"], products=products
            )
            categories.append(category)

    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return None
    except ValueError as e:
        raise ValueError(f"Ошибка данных: {e}")
    return categories


categories = load_data_from_json(file_path)
if categories:
    for category in categories:
        print(
            f"Категория: {category.name}, Описание: {category.description}."
            f" Количество продуктов: {len(category.products)}"
            
        )
        for product in category.products:
            if isinstance(product, Product):
                print(product.name)
            else:
                print(f"Неверный формат продукта: {product}")
