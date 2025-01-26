from io import StringIO
from unittest.mock import patch

from src.category import Category, Product


def test_product_itialization() -> None:
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_count() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию и добавляем продукты
    category = Category("Смартфоны", "Описание категории", [product1, product2, product3])

    # Проверяем количество продуктов в категории
    assert category.product_count == 20


def test_price_setter_positive() -> None:
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = 150.0
    assert product.price == 150.0


def test_price_setter_zero_or_negative() -> None:
    product = Product("Товар", "Описание", 100.0, 10)
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        product.price = 0
        assert "Цена не должна быть нулевая или отрицательная" in mock_stdout.getvalue()


def test_price_setter_lower() -> None:
    product = Product("Товар", "Описание", 100.0, 10)

    with patch("builtins.input", return_value="y"):
        product.price = 80.0
    assert product.price == 80.0


def test_price_setter_lower_cancel() -> None:
    product = Product("Товар", "Описание", 100.0, 10)

    with patch("builtins.input", return_value="n"):
        product.price = 80.0
    assert product.price == 100.0


def test_new_product() -> None:
    product_data = {"name": "Товар", "description": "Описание", "price": 100.0, "quantity": 10}
    product = Product.new_product(product_data)
    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 100.0
    assert product.quantity == 10


def test_repr() -> None:
    product = Product("Товар", "Описание", 100.0, 10)
    assert repr(product) == "Товар, 100.0 руб. Остаток: 10 шт."
