from src.BaseProduct import Mixin
from src.product import Product


class Smartphone(Product, Mixin):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


    def __str__(self) -> str:
        return f"{self.name}; {self.description}; {self.price}; {self.quantity} шт."
