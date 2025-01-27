from src.product import Product


class CategoryIterator:
    def __init__(self, category) -> None:
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> "Product":
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
