
from _pytest.capture import CaptureFixture

from src.class_product import Product


def test_class_mixing(capsys:CaptureFixture):
    product = Product('test_name', 'test_description', 55.55, 25)
    check_out = capsys.readouterr()
    assert check_out.out == 'Product ("test_name", test_description, 55.55, 25)\n'
    assert str(product) == 'test_name , 55 руб. Остаток: 25 шт'
    product.quantity = 0


def test_repr(repr_cls_mixing):
    expected_repr = 'Product ("test_name_1", test_description_1, 100.0, 15)'
    actual_repr = repr(repr_cls_mixing)
    assert actual_repr == expected_repr
