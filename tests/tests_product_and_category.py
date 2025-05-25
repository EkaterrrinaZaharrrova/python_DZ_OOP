def test_class_product(product_fixture):
    product_fixture.name = "Iphone 15"
    product_fixture.description = "512GB, Gray space"
    product_fixture.price = 210000.0
    product_fixture.quantity = 8


def test_class_category(category_fixture):
    assert category_fixture.name == "Смартфоны"
    assert category_fixture.description == "Смартфоны - средство получения дополнительных функций для удобства жизни"
    assert category_fixture.products == []
