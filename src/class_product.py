class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация класса продукт."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, new_product: dict):
        """Метод создания нового объекта Product"""
        new_pro = cls(**new_product)
        return new_pro


    @property
    def price(self):
        """Геттер"""

        return self.__price

    @price.setter
    def price(self, set_price: float) -> None:
        """Сеттер, значения цены"""

        if set_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = set_price
