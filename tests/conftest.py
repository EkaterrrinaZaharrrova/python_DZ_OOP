import pytest

from src.class_category import Category
from src.class_product import Product, Smartphone, LawnGrass


@pytest.fixture
def product_fixture():
    """Фикстура для класса продукт."""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_fixture():
    """Фикстура для класса категории."""
    prod_1 = Product("iphone", "16 S max", 13_658, 7)
    prod_2 = Product("samsung", "A 564", 12_467, 9)

    return Category("phones", "new", [prod_1, prod_2])

@pytest.fixture
def count_category_fixture() -> list:

    return [
        {"name": "Zeekr 001 FR", "description": "256GB", "price": 6_250_000, "quantity": 1},
        {"name": "Voyah Free", "description": "256GB", "price": 4_360_000, "quantity": 3},
        {"name": "Geely Monjaro", "description": "256GB", "price": 3_230_000, "quantity": 14},
        {"name": "Staria", "description": "256GB", "price": 5_250_000, "quantity": 10},
        {"name": "Lixiang L9", "description": "256GB", "price": 5_360_000, "quantity": 3},
        {"name": "TANK 700", "description": "256GB", "price": 7_230_000, "quantity": 4},
        {"name": "BMW X7", "description": "256GB", "price": 16_450_777, "quantity": 2},
        {"name": "MB GLS MAY", "description": "256GB", "price": 46_777_777, "quantity": 1},
        {"name": "MB VIANO", "description": "256GB", "price": 6_450_777, "quantity": 6},
        {"name": "Maybach 62", "description": "256GB", "price": 86_777_777, "quantity": 1},
        {"name": "Audi TT", "description": "256GB", "price": 7_450_777, "quantity": 2},
        {"name": "MB GLS ", "description": "256GB", "price": 26_757_757, "quantity": 3}
    ]


@pytest.fixture
def smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def grass():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
