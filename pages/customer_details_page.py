from selenium.webdriver.common.by import By

class CustomerDetailsPage:
    name_field = (By.XPATH, '//input[@placeholder="* Имя"]')
    surname_field = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    delivery_address_field = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    metro_station_field = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    phone_number_for_courier_field = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    next_button = (By.XPATH, '//button[text()="Далее"]')
    station_Borisovo = (By.XPATH,'.//div[@class="select-search__select"]//*[text()="Борисово"]')
    station_Sokolniki = (By.XPATH,'.//div[@class="select-search__select"]//*[text()="Сокольники"]')
    about_customer_title = (By.XPATH, './/div[text()="Для кого самокат"]')

    def __init__(self, driver):
        self.driver = driver


    def set_data_for_name_field(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def set_data_for_surname_field(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    def set_address_for_address_field(self, address):
        self.driver.find_element(*self.delivery_address_field).send_keys(address)

    def click_on_metro_station_field(self):
        self.driver.find_element(*self.metro_station_field).click()

    def choose_on_metro_station_field(self, station):
        self.driver.find_element(*station).click()

    def set_data_for_number_field(self, phone_number):
        self.driver.find_element(*self.phone_number_for_courier_field).send_keys(phone_number)

    def click_on_next_button(self):
        self.driver.find_element(*self.next_button).click()
