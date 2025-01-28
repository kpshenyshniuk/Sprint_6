import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class RentDetailsPage:
    about_rent_title = (By.XPATH, '//div[text()="Про аренду"]')
    delivery_date_date_picker = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    rent_time_field = (By.XPATH, '//div[@class="Dropdown-control"]')
    four_days_option = (By.XPATH, '//div[text()="четверо суток"]')
    six_days_option = (By.XPATH, '//div[text()="шестеро суток"]')
    roller_black_color_checkbox = (By.XPATH, '//label[@for="black" and contains(text(), "чёрный жемчуг")]')
    roller_gray_color_checkbox = (By.XPATH, '//label[@for="grey" and contains(text(), "серая безысходность")]')
    comment_for_courier_field = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    order_button = (By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]')
    yes_button = (By.XPATH,'//button[text()="Да"]')
    successfull_order_message = (By.XPATH,'//div[contains(@class, "Order_ModalHeader") and contains(text(), "Заказ оформлен")]')


    def __init__(self, driver):
        self.driver = driver

    def set_delivery_date(self, date):
        self.driver.find_element(*self.delivery_date_date_picker).send_keys(date + Keys.ENTER)

    def set_rent_duration(self, days):
        self.driver.find_element(*self.rent_time_field).click()
        time.sleep(1)
        self.driver.find_element(*days).click()

    def set_color_for_roller(self, color):
        self.driver.find_element(*color).click()

    def set_coment_for_courier(self, comment):
        self.driver.find_element(*self.comment_for_courier_field).send_keys(comment)

    def click_on_confirm_button(self):
        self.driver.find_element(*self.order_button).click()

    def click_on_confirmation_order_button(self):
        self.driver.find_element(*self.yes_button).click()

    def find_element(self, element):
        self.driver.find_element(*element)
