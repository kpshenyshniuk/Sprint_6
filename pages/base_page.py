from selenium.webdriver.common.by import By

class BasePage:
    top_order_button = (By.XPATH,"//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button') and text()='Заказать']")
    bottom_order_button = (By.XPATH, "//div[contains(@class, 'Header')]/button[contains(@class, 'Button_Button') and text()='Заказать']")
    yandex_dzen_logo = (By.XPATH, '//a[contains(@class, "Header_LogoYandex") and contains(@href, "yandex.ru")]')
    roller_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]/img[@src='/assets/scooter.svg' and @alt='Scooter']")

    def __init__(self, driver):
        self.driver = driver
    def click_on_order_button(self, locator):
        element = self.driver.find_element(*locator)
        element.click()
