from src.smartphone import Smartphone


def test_smartphone_initialization() -> None:
    smartphone = Smartphone("iPhone", "Latest model", 999.99, 10, 1.5, "iPhone 13", 256, "Black")

    assert smartphone.name == "iPhone"
    assert smartphone.description == "Latest model"
    assert smartphone.price == 999.99
    assert smartphone.quantity == 10
    assert smartphone.efficiency == 1.5
    assert smartphone.model == "iPhone 13"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"
