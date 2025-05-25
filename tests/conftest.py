import pytest

from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def product_fixture():
    """Фикстура для класса продукт."""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_fixture():
    """Фикстура для класса категории."""
    return Category("Смартфоны",
                         "Смартфоны - средство получения дополнительных функций для удобства жизни", [])
