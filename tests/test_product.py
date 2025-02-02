from io import StringIO
from unittest.mock import patch

import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product


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
    assert category.product_count == 30


def test_price_setter_positive() -> None:
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = 150.0
    assert product.price == 150.0


def test_price_setter_zero_or_negative() -> None:
    product = Product("Товар", "Описание", 100.0, 10)
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        product.price = 0
        assert "Цена не должна быть нулевая или отрицательная" in mock_stdout.getvalue()


def test_new_product() -> None:
    product_data = {"name": "Товар", "description": "Описание", "price": 100.0, "quantity": 10}
    product = Product.new_product(product_data)
    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 100.0
    assert product.quantity == 10


def test_repr() -> None:
    product = Product("Товар", "Описание", 100.0, 10)
    assert repr(product) == "Товар; Описание; 100.0; 10 шт."


def test_add_products() -> None:
    product1 = Product("Товар 1", "Описание", 100, 5)
    product2 = Product("Товар 2", "Описание", 300, 10)

    total_value = product1.__add__(product2)

    assert total_value == 3500


def test_add_invalid_product() -> None:
    product1 = Product("Товар 1", "Описание", 500, 3)
    product2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    with pytest.raises(TypeError, match="Нельзя складывать продукты разных типов."):
        product1.__add__(product2)


@pytest.fixture
def product() -> Product:
    return Product("Товар", "Описание товара", 100.0, 10)


def test_price_setter_lower_value_with_confirmation(product: Product) -> None:
    with patch("builtins.input", side_effect=["y"]):
        product.price = 80.0
        assert product.price == 80.0


def test_price_setter_lower_value_with_out_confirmation(product: Product) -> None:
    with patch("builtins.input", side_effect=["n"]):
        product.price = 80.0
        assert product.price == 100.0  # Цена не должна измениться


def test_add_same_type_products(product: Product) -> None:
    product2 = Product("Товар 2", "Описание товара 2", 200.0, 5)
    total_price = product + product2
    assert total_price == (100.0 * 10) + (200.0 * 5)
