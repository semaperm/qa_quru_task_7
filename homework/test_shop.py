"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product
from homework.models import Cart



@pytest.fixture
def book():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def pencile():
    return Product("pencile", 15.50, "This is a pencile", 60)

@pytest.fixture
def cart():
    return Cart()

buy_product_count = 15
buy_product_count_2 = 7

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, book):
        # TODO напишите проверки на метод check_quantity

        assert book.check_quantity(book.quantity)
        assert book.check_quantity(book.quantity - 1)
        assert not book.check_quantity(book.quantity + 1)

    def test_product_buy(self, book):
        # TODO напишите проверки на метод buy
        quantity_before = book.quantity
        required_quantity = 1000
        book.buy(required_quantity)
        assert book.quantity == quantity_before - required_quantity

    def test_product_buy_more_than_available(self, book):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            book.buy(book.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_in_cart(self, cart, book):

        cart.add_product(book, buy_product_count)
        cart.add_product(book, buy_product_count + 35)
        assert cart.products[book] == 50
        assert book in cart.products.keys()

    def test_remove_product(self, cart, book, pencile):

        cart.add_product(book, buy_product_count)
        cart.add_product(pencile, buy_product_count_2)
        assert book, pencile in cart.products.keys()
        cart.remove_product(book)
        cart.remove_product(pencile)
        assert book, pencile not in cart.products.keys()

    def test_remove_product_partially(self, cart, book, pencile):

        cart.add_product(book, buy_product_count)
        cart.add_product(pencile, buy_product_count_2)
        assert book, pencile in cart.products.keys()
        cart.remove_product(book, 5)
        cart.remove_product(pencile, 3)
        assert cart.products[book] == 10
        assert cart.products[pencile] == 4

    def test_clear_cart(self, cart, book, pencile):

        cart.add_product(book, buy_product_count)
        cart.add_product(pencile, buy_product_count_2)
        cart.clear()
        assert not cart.products

    def test_get_total_price(self, cart, book, pencile):

        cart.add_product(book, buy_product_count)
        cart.add_product(pencile, buy_product_count_2)
        assert cart.get_total_price() > 0

    def test_buy(self, cart, book, pencile):

        cart.add_product(book, buy_product_count)
        cart.add_product(pencile, buy_product_count_2)
        cart.buy()
        assert not cart.products

    def test_buy_error(self, cart, book, pencile):
        with pytest.raises(ValueError):
            cart.add_product(book, 1001)
            cart.add_product(pencile, 61)
            cart.buy()