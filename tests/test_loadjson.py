import json
from unittest.mock import mock_open, patch

import pytest

from src.loadjson import load_data_from_json

valid_json_data = json.dumps(
    [
        {
            "name": "Категория 1",
            "description": "Описание категории 1",
            "products": [
                {"name": "Продукт 1", "description": "Описание продукта 1", "price": 100, "quantity": 10},
                {"name": "Продукт 2", "description": "Описание продукта 2", "price": 200.5, "quantity": 5},
            ],
        }
    ]
)

invalid_json_data = json.dumps(
    [
        {
            "name": "Категория 1",
            "description": "Описание категории 1",
            "products": [
                {
                    "name": "Продукт 1",
                    "description": "Описание продукта 1",
                    "price": "некорректная цена",
                    "quantity": 10,
                }
            ],
        }
    ]
)


def test_load_data_from_json_valid() -> None:
    with patch("builtins.open", mock_open(read_data=valid_json_data)):
        categories = load_data_from_json("fake_path.json")
        assert len(categories) == 1
        assert categories[0].name == "Категория 1"
        assert len(categories[0].products) == 2
        assert categories[0].products[0].price == 100
        assert categories[0].products[1].price == 200.5


def test_load_data_from_json_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        categories = load_data_from_json("fake_path.json")
        assert categories is None


def test_load_data_from_json_invalid_price() -> None:
    with patch("builtins.open", mock_open(read_data=invalid_json_data)):
        with pytest.raises(ValueError, match="Некорректная цена"):
            load_data_from_json("fake_path.json")
