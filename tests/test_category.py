import pytest

from src.category import Category
from src.product import Product


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
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("Смартфоны", "Описание категории", [product1, product2, product3])

    assert category.product_count == 9


def test_add_product() -> None:
    product3 = Product("Товар 3", "Описание категории", 7, 3)
    category = Category("Смартфоны", "Описание категории", [product3])

    category.add_product(product3)

    assert len(category.products) == 2
    assert Category.product_count == 11


def test_add_invalid_product() -> None:
    product3 = Product("Товар 3", "Описание категории", 7, 3)
    category = Category("Смартфоны", "Описание категории", [product3])
    with pytest.raises(TypeError):
        category.add_product("product")


def test_str_method() -> None:
    product3 = Product("Товар 3", "Описание категории", 7, 3)
    category = Category("Смартфоны", "Описание категории", [product3])
    assert str(category) == "Смартфоны, 3 шт."

def test_category_class_attributes() -> None:

    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product3 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    category1 = Category("Смартфоны", "Описание", [product1, product2, product3])
    category2 = Category("Гаджеты", "Описание", [product4])

    assert Category.category_count == 9
    assert Category.product_count == 17

    assert category1.product_count == 17
    assert category2.product_count == 17

