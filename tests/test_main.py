from src.category import Category, Product


def test_product_initialization() -> None:
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization() -> None:
    # Создаем несколько продуктов
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )

    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category.products) == 2
    assert category.products[0].name == "Iphone 15"  # Проверяем первый продукт в категории
    assert category.products[1].name == "Xiaomi Redmi Note 11"  # Проверяем второй продукт в категории


def test_category_class_attributes() -> None:

    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product3 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    category1 = Category("Смартфоны", "Описание", [product1, product2, product3])
    category2 = Category("Гаджеты", "Описание", [product4])

    assert Category.category_count == 12
    assert Category.product_count == 24

    assert category1.product_count == 24
    assert category2.product_count == 24    
