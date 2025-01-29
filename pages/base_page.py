from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    top_order_button = (By.XPATH,"//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button') and text()='Заказать']")
    bottom_order_button = (By.XPATH, "//div[contains(@class, 'Header')]/button[contains(@class, 'Button_Button') and text()='Заказать']")
    yandex_dzen_logo = (By.XPATH, '//a[contains(@class, "Header_LogoYandex") and contains(@href, "yandex.ru")]')
    roller_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]/img[@src='/assets/scooter.svg' and @alt='Scooter']")
    coockie_confirm_button = (By.ID, 'rcc-confirm-button')
    def __init__(self, driver):
        self.driver = driver
    def click_on_order_button(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def wait_for_page_load(self, timeout=10):
        """Ожидание полной загрузки страницы"""
        WebDriverWait(self.driver, timeout).until(lambda d: self.driver.execute_script("return document.readyState") == "complete")

    def wait_for_element_is_clickable(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((element))).click()

    def wait_for_visibility(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element))

    def wait_for_current(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    def find_element(self, element):
        self.driver.find_element(*element)