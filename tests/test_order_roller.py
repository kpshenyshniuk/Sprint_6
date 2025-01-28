from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import main_page_data
from pages.main_page import MainPage
from pages.customer_details_page import CustomerDetailsPage
from pages.rent_details_page import RentDetailsPage
import customer_details_page_data
from conftest import tomorrow_date


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
        main_page = MainPage(setup_driver)
        customer_details_page = CustomerDetailsPage(setup_driver)
        rent_details_page = RentDetailsPage(setup_driver)
        setup_driver.get(main_page_data.main_page_link)
        WebDriverWait(setup_driver, 10).until(lambda d: setup_driver.execute_script("return document.readyState") == "complete")
        WebDriverWait(setup_driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'rcc-confirm-button'))).click()
        main_page.click_on_order_button(order_button_locator)
        WebDriverWait(setup_driver, 10).until(expected_conditions.visibility_of_element_located((customer_details_page.about_customer_title)))
        customer_details_page.set_data_for_name_field(customer_details_page_data.name)
        customer_details_page.set_data_for_surname_field(customer_details_page_data.surname)
        customer_details_page.set_address_for_address_field(customer_details_page_data.address)
        customer_details_page.click_on_metro_station_field()
        customer_details_page.choose_on_metro_station_field(station)
        customer_details_page.set_data_for_number_field(customer_details_page_data.phone_number)
        customer_details_page.click_on_next_button()
        WebDriverWait(setup_driver, 10).until(expected_conditions.visibility_of_element_located(rent_details_page.about_rent_title))
        rent_details_page.set_delivery_date(tomorrow_date)
        rent_details_page.set_rent_duration(days)
        rent_details_page.set_color_for_roller(roller_color)
        rent_details_page.set_coment_for_courier(customer_details_page_data.comment)
        rent_details_page.click_on_confirm_button()
        WebDriverWait(setup_driver, 10).until(expected_conditions.element_to_be_clickable(rent_details_page.yes_button)).click()
        assert WebDriverWait(setup_driver, 10).until(expected_conditions.visibility_of_element_located(rent_details_page.successfull_order_message))



