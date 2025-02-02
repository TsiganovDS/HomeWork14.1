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


def test_middle_price_no_products():
    """Тест для случая, когда в категории нет товаров."""
    category = Category(name="Тестовая категория", description="Описание", products=[])
    assert category.middle_price() == 0.0


def test_middle_price_one_product():
    """Тест для случая, когда в категории один товар."""
    product = Product(name="Товар 1", description="Описание товара 1", price=100.0, quantity=1)
    category = Category(name="Тестовая категория", description="Описание", products=[product])
    category.add_product(product)
    assert category.middle_price() == 100.0


def test_middle_price_multiple_products():
    """Тест для случая, когда в категории несколько товаров."""
    product1 = Product(name="Товар 1", description="Описание товара 1", price=100.0, quantity=1)
    product2 = Product(name="Товар 2", description="Описание товара 2", price=200.0, quantity=2)
    product3 = Product(name="Товар 3", description="Описание товара 3", price=300.0, quantity=3)

    category = Category(name="Тестовая категория", description="Описание", products=[product1, product2, product3])
    category.add_product(product1)
    category.add_product(product2)
    category.add_product(product3)

    expected_average_price = round((100.0 + 200.0 + 300.0) / 3, 2)
    assert category.middle_price() == expected_average_price
