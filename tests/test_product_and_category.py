import pytest

from src.class_category import Category
from src.class_product import LawnGrass, Product, Smartphone


def test_class_product(product_fixture):
    product_fixture.name = "Iphone 15"
    product_fixture.description = "512GB, Gray space"
    product_fixture.price = 210000.0
    product_fixture.quantity = 8


def test_class_category(category_fixture):
    assert category_fixture.name == "phones"
    assert category_fixture.description == "new"
    assert category_fixture.products == 'iphone, 13658 руб. Остаток: 7 шт.\nsamsung, 12467 руб. Остаток: 9 шт.\n'


def test_new_product():
    assert (
        Product.new_product({"name": "Zeekr 001 FR", "description": "256GB", "price": 6_250_000, "quantity": 1}).name
        == "Zeekr 001 FR"
    )


def test_counters(count_category_fixture) -> None:
    """Тест счётчиков класса Category"""

    old_categories_counter = Category.category_count
    old_products_counter = Category.product_count

    products = []
    for row in count_category_fixture:
        products.append(Product(**row))

    Category("phones", "new", products)
    Category("phones", "new", products)

    assert Category.product_count == old_categories_counter
    assert Category.product_count == old_products_counter


def test_price():
    prod = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    prod.price = 125
    assert prod.price == 125


def test_add_product_type(product_fixture):
    assert isinstance(product_fixture, Product)


def test_str_product(product_fixture):
    assert product_fixture.__str__() == "Iphone 15 , 210000 руб. Остаток: 8 шт"


def test__add__product():
    p1 = Product("phones", "black, 1024GB", 5900.0, 13)
    p2 = Product("phones", "black, 1024GB", 5100.0, 23)
    assert Product.__add__(p1, p2) == 194000.0


def test_str_category(category_fixture):
    assert category_fixture.__str__() == "phones,  количество продуктов: 16 шт"


def test_class_phone(smartphone: Smartphone, grass: LawnGrass) -> None:
    assert smartphone.color == "Серый"
    assert Smartphone.__add__(smartphone, smartphone) == 1800000.0
    with pytest.raises(TypeError):
        assert Smartphone.__add__(smartphone, grass) == TypeError


def test_class_grass(smartphone: Smartphone, grass: LawnGrass) -> None:
    assert grass.price == 450.0
    assert LawnGrass.__add__(grass, grass) == 13500.0
    with pytest.raises(TypeError):
        assert LawnGrass.__add__(grass, smartphone) == TypeError


def test_add_product() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    assert Category.add_product(category1, product3) is None


