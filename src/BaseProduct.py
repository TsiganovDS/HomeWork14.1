from abc import ABC, abstractmethod
from typing import Any

class BaseProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер для цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой."""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: Any) -> "BaseProduct":
        """Принимает на вход параметры товара в словаре
        и возвращает созданный объект класса BaseProduct"""
        pass


class Mixin:
    def __init__(self, *args, **kwargs) -> None:
        self.class_name = self.__class__.__name__
        self.params = ', '.join(repr(arg) for arg in args)
        super().__init__()

    def __repr__(self):
        return f"{self.class_name}({self.params})"
