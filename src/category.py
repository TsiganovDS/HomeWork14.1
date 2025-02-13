from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self) -> list[Product]:
        return self.__products

    def add_product(self, new_product: Product) -> None:
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def product(self) -> list:
        """Формируем список строк с информацией о каждом продукте"""
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def __str__(self) -> str:
        counter = 0
        for product in self.__products:
            counter += product.quantity
        return f"{self.name}, {counter} шт."

    def middle_price(self) -> float:
        """Подсчитывает среднюю цену всех товаров в категории."""
        if not self.__products:
            return 0.0

        total_price = sum(product.price for product in self.__products)
        average = round(total_price / len(self.__products), 2)
        return average

    def __repr__(self) -> str:
        counter = sum(product.quantity for product in self.__products)
        return f"{self.name}, {counter} шт."
