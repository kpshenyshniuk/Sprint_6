import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.main_page import MainPage
from pages.customer_details_page import CustomerDetailsPage
from pages.rent_details_page import RentDetailsPage
from data import customer_details_page_data, main_page_data
from conftest import tomorrow_date
from pages.base_page import BasePage


@pytest.mark.usefixtures("setup_driver")
class TestOrderPage:
    @pytest.mark.parametrize(
        "order_button_locator, roller_color, station, days",
        [
            (MainPage.top_order_button, RentDetailsPage.roller_black_color_checkbox, CustomerDetailsPage.station_Borisovo, RentDetailsPage.four_days_option),
            (MainPage.bottom_order_button, RentDetailsPage.roller_gray_color_checkbox, CustomerDetailsPage.station_Sokolniki, RentDetailsPage.six_days_option)
        ]
    )
    def test_successfull_roller_oder(self, setup_driver, tomorrow_date, order_button_locator, roller_color, station, days):
        """
        Проверка успешного сценария заказа самоката с разными данными
        """
        customer_details_page = CustomerDetailsPage(setup_driver)
        rent_details_page = RentDetailsPage(setup_driver)
        setup_driver.get(main_page_data.main_page_link)
        customer_details_page.wait_for_page_load()
        customer_details_page.wait_for_element_is_clickable(customer_details_page.coockie_confirm_button)
        customer_details_page.click_on_order_button(order_button_locator)
        customer_details_page.wait_for_visibility(customer_details_page.about_customer_title)
        customer_details_page.set_data_for_name_field(customer_details_page_data.Name)
        customer_details_page.set_data_for_surname_field(customer_details_page_data.Surname)
        customer_details_page.set_address_for_address_field(customer_details_page_data.Address)
        customer_details_page.click_on_metro_station_field()
        customer_details_page.choose_on_metro_station_field(station)
        customer_details_page.set_data_for_number_field(customer_details_page_data.Phone_number)
        customer_details_page.click_on_next_button()
        customer_details_page.wait_for_visibility(rent_details_page.about_rent_title)
        rent_details_page.set_delivery_date(tomorrow_date)
        rent_details_page.set_rent_duration(days)
        rent_details_page.set_color_for_roller(roller_color)
        rent_details_page.set_coment_for_courier(customer_details_page_data.Comment)
        rent_details_page.click_on_confirm_button()
        customer_details_page.wait_for_element_is_clickable(rent_details_page.yes_button)
        customer_details_page.wait_for_visibility(rent_details_page.successfull_order_message)
        element = WebDriverWait(setup_driver, 10).until(expected_conditions.visibility_of_element_located((rent_details_page.successfull_order_message)))
        assert element.is_displayed()
