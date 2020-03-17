import pytest
from pages.product_page import ProductPage
import time

URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.parametrize('offers', [f'?promo=offer{offer}' for offer in range(10) if offer != 7] + [
    pytest.param('?promo=newYear2019', marks=pytest.mark.skip),
    pytest.param('?promo=offer7', marks=pytest.mark.xfail)
])
def test_guest_can_add_product_to_basket(browser, offers):
    page = ProductPage(browser, URL+offers)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.are_prices_equal_on_success()
    page.are_names_equal_on_success()

@pytest.mark.smoke
def test_guest_cant_see_after_adding_product_to_basket(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.smoke
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.smoke
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.add_to_basket()
    page.should_not_dissappear_success_alert()
