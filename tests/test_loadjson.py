import json
from pathlib import Path
from typing import Tuple, Any

import pytest

from src.category import Product, Category
from src.loadjson import load_data_from_json, file_path


@pytest.fixture
def mock_json_file(tmp_path: str) -> tuple[Any, Any]:
    """Создаёт временный файл с JSON-данными."""
    valid_file = tmp_path / "valid.json"
    invalid_file = tmp_path / "invalid.json"

    valid_json = [
        {
            "name": "Category 1",
            "description": "Description 1",
            "products": [
                {
                    "name": "Product 1",
                    "description": "Product 1 description",
                    "price": 100,
                    "quantity": 10,
                },
                {
                    "name": "Product 2",
                    "description": "Product 2 description",
                    "price": 200,
                    "quantity": 5,
                },
            ],
        }
    ]

    invalid_json = [
        {
            "name": "Category 1",
            "description": "Description 1",
            "products": [
                {
                    "name": "Product 2",
                    "description": "Product 1 description",
                    "price": "100",
                    "quantity": 10,
                },
                {
                    "name": "Product 2",
                    "description": "Product 2 description",
                    "price": 122,
                    "quantity": 5,
                },
            ],
        }
    ]

    # Записываем данные в формате JSON
    valid_file.write_text(json.dumps(valid_json))
    invalid_file.write_text(json.dumps(invalid_json))

    return valid_file, invalid_file


def test_load_data_from_json_valid(mock_json_file: str) -> None:
    valid_file = mock_json_file[0]  # Получаем валидный файл
    product1 = Product(
        name="Телевизор Samsung",
        description="Умный телевизор 55 дюймов",
        price=50000,
        quantity=10,
    )
    product2 = Product(
        name="Телевизор LG",
        description="OLED телевизор 65 дюймов",
        price=70000,
        quantity=5,
    )
    products = [product1, product2]
    Category("Телевизор", "Большой", products=products)

    categories = load_data_from_json(valid_file)

    assert len(categories) == 1
    assert categories[0].name == "Category 1"
    assert len(categories[0].products) == 2
    assert categories[0].products[0].name == "Product 1"
    assert categories[0].products[1].price == 200.0


def test_load_data_from_json_invalid(mock_json_file: str) -> None:
    invalid_file = mock_json_file[1]
    with pytest.raises(ValueError, match="Некорректная цена: 100"):
        load_data_from_json(invalid_file)


def test_load_data_from_json_file_not_found() -> None:
    product1 = Product(
        name="Телевизор Samsung",
        description="Умный телевизор 55 дюймов",
        price=50000,
        quantity=10,
    )
    product2 = Product(
        name="Телевизор LG",
        description="OLED телевизор 65 дюймов",
        price=70000,
        quantity=5,
    )
    products = [product1, product2]
    Category("Телевизор", "Большой", products=products)

    result = load_data_from_json("valid_file")

    assert result is None


if __name__ == "__main__":
    pytest.main()
