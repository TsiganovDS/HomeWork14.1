from typing import Any

from src.BaseProduct import BaseProduct, Mixin


class Product(Mixin, BaseProduct):

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirmation = input(f"Вы уверены, что хотите понизить цену с {self.price} до {value}? (y/n): ")
            if confirmation.lower() == "y":
                self.__price = value
                print(f"Цена успешно понижена до {value}.")
            else:
                print("Изменение цены отменено.")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: Any) -> "Product":
        """Принимает на вход параметры товара в словаре
        и возвращает созданный объект класса Product"""
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    def __add__(self, other: "Product") -> float:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать продукты разных типов.")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __repr__(self) -> str:
        return f"{self.name}; {self.description}; {self.price}; {self.quantity} шт."

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
