from abc import ABC, abstractmethod

from src.class_mixing import PrintConsoleMixing


class BaseProduct(ABC):

    @abstractmethod
    def info_class(self):
        pass


class Product(PrintConsoleMixing, BaseProduct):
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
        super().__init__()

    def __str__(self):
        return f"{self.name} , {int(self.__price)} руб. Остаток: {self.quantity} шт"

    def __add__(self, other):

        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    def info_class(self) -> str:
        return f"{self.__class__.__name__}"


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


class Smartphone(Product):

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
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color