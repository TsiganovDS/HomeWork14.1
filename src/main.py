from src.category import Category, Product

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(f"Наименование product1:  {product1.name}")
    print(f"Описание product1: {product1.description}")
    print(f"Цена product1: {product1.price}")
    print(f"Количество в наличии product1: {product1.quantity}")

    print(f"Наименование product2:  {product2.name}")
    print(f"Описание product2: {product2.description}")
    print(f"Цена product2: {product2.price}")
    print(f"Количество в наличии product2: {product2.quantity}")

    print(f"Наименование product3:  {product3.name}")
    print(f"Описание product3: {product3.description}")
    print(f"Цена product3: {product3.price}")
    print(f"Количество в наличии product3: {product3.quantity}")

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(f"category1.name: {category1.name}")
    print(f"category1.description: {category1.description}")
    print(f"Количество category1: {len(category1.products)}")
    print(f"category1.category_count: {category1.category_count}")
    print(f"category1.product_count: {category1.product_count}")

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(f"category2.name:   {category2.name}")
    print(f"category2.description: {category2.description}")
    print(f"Количество category2: {len(category2.products)}")
    print(f"category2.products: {category2.products}")

    print(f"Category.category_count: {category2.category_count}")
    print(f"Category.product_count: {category2.product_count}")

