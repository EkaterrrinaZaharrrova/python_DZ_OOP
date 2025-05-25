from src.class_product import Product


class Category:
    name: str
    description: str
    category_count: int = 0
    product_count: int = 0
    products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]):
        """Инициализация класса категории"""

        self.name = name
        self.description = description
        self.products = products
        self.category_count += 1
        self.product_count += len(products) if products else 0
