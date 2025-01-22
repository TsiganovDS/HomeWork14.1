import json

import pytest

from src.category import Category, Product


def test_product_in_itialization():
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Описание категории", [product1, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category.products) == 2
    assert category.products[0].name == "Samsung Galaxy S23 Ultra"
    assert category.products[1].name == "Iphone 15"


def test_category_count():
    Category.reset_counts()
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category1 = Category("Смартфоны", "Описание категории", [product1, product2])
    category2 = Category("Телевизоры", "Описание телевизоров", [])

    assert Category.category_count == 2
    assert Category.product_count == 2


def test_product_count():
    Category.reset_counts()
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны", "Описание категории", [product1, product2, product3]
    )

    assert Category.product_count == 3

"""Пример корректного JSON"""
valid_json = '''[
    {
        "name": "Category 1",
        "description": "Description 1",
        "products": [
            {
                "name": "Product 1",
                "description": "Product 1 description",
                "price": 100,
                "quantity": 10
            },
            {
                "name": "Product 2",
                "description": "Product 2 description",
                "price": 200,
                "quantity": 5
            }
        ]
    }
]'''

"""Пример некорректного JSON"""
invalid_json = '''[
    {
        "name": "Category 1",
        "description": "Description 1",
        "products": [
            {
                "name": "Product 1",
                "description": "Product 1 description",
                "price": 100,
                "quantity": 10
            },
            {
                "name": "Product 2",
                "description": "Product 2 description",
                "price": "некорректное значение",
                "quantity": 5
            }
        ]
    }
]'''


@pytest.fixture
def mock_json_file(tmp_path):
    """Создаёт временный файл с JSON-данными."""
    valid_file = tmp_path / "valid.json"
    invalid_file = tmp_path / "invalid.json"

    valid_file.write_text(valid_json)
    invalid_file.write_text(invalid_json)

    return valid_file, invalid_file


def test_load_data_from_json_valid(mock_json_file):
    valid_file = mock_json_file
    product1 = Product(name="Телевизор Samsung", description="Умный телевизор 55 дюймов", price=50000, quantity=10)
    product2 = Product(name="Телевизор LG", description="OLED телевизор 65 дюймов", price=70000, quantity=5)
    products = [product1, product2]
    instance = Category("Телевизор", "Большой", products=products)

    categories = instance.load_data_from_json(valid_file)

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 3
    assert categories[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[0].products[1].price == 210000.0


def test_load_data_from_json_invalid(mock_json_file):
    product1 = Product(name="Телевизор Samsung", description="Умный телевизор 55 дюймов", price=50000, quantity=10)
    product2 = Product(name="Телевизор LG", description="OLED телевизор 65 дюймов", price=70000, quantity=5)
    products = [product1, product2]
    instance = Category("Телевизор", "Большой", [])

    with pytest.raises(Exception):
        instance.load_data_from_json(mock_json_file)


def test_load_data_from_json_file_not_found():
    product1 = Product(name="Телевизор Samsung", description="Умный телевизор 55 дюймов", price=50000, quantity=10)
    product2 = Product(name="Телевизор LG", description="OLED телевизор 65 дюймов", price=70000, quantity=5)
    products = [product1, product2]
    instance = Category("Телевизор", "Большой", products=products)

    result = instance.load_data_from_json("not_existing_file.json")

    assert result is None

if __name__ == "__main__":
    pytest.main()
