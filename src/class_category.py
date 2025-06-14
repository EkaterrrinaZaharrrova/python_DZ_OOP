from src.class_product import Product


class Category:
    name: str
    description: str
    category_count: int = 0
    product_count: int = 0
    __products: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]):
        """Инициализация класса категории"""

        self.name = name
        self.description = description
        self.__products = products
        self.category_count += 1
        self.product_count += len(products) if products else 0



    def add_product(self, product: Product) -> None:

        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1

        else:
            raise TypeError



    @property
    def products(self):
        product_info = ""
        for elem in self.__products:
            product_info += f"{elem.name}, {elem.price} руб. Остаток: {elem.quantity} шт.\n"
        return product_info

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            if self.name:
                total_quantity += product.quantity
        return f"{self.name},  количество продуктов: {total_quantity} шт"