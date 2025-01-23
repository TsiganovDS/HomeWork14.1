import json

import pytest

from src.category import Category, Product
from src.loadjson import load_data_from_json


def test_product_in_itialization() -> None:
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Описание категории", [product1, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category.products) == 2
    assert category.products[0].name == "Samsung Galaxy S23 Ultra"
    assert category.products[1].name == "Iphone 15"


def test_category_count() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category1 = Category("Смартфоны", "Описание категории", [product1, product2])
    category2 = Category("Телевизоры", "Описание телевизоров", [])

    assert Category.category_count == 11
    assert Category.product_count == 20


def test_product_count() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("Смартфоны", "Описание категории", [product1, product2, product3])

    assert Category.product_count == 23


"""Пример корректного JSON"""
