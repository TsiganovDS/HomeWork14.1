import json
import os
from typing import Any

from src.category import Product, Category


def load_data_from_json(file_path: str) -> list[Any]:
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


file_path = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")

categories = load_data_from_json(file_path)
if categories:
    for category in categories:
        print(
            f"Категория: {category.name}, Описание: {category.description},"
            f"Количество продуктов: {len(category.products)}"
        )
        for product in category.products:
            print(
                f"Продукт: {product.name}, Описание: {product.description}, Цена: {product.price},"
                f"Количество: {product.quantity}"
            )
