from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    faq_1_question = (By.ID, 'accordion__heading-0')
    faq_1_answer = (By.ID, 'accordion__panel-0')
    faq_2_question = (By.ID, 'accordion__heading-1')
    faq_2_answer = (By.ID, 'accordion__panel-1')
    faq_3_question = (By.ID, 'accordion__heading-2')
    faq_3_answer = (By.ID, 'accordion__panel-2')
    faq_4_question = (By.ID, 'accordion__heading-3')
    faq_4_answer = (By.ID, 'accordion__panel-3')
    faq_5_question = (By.ID, 'accordion__heading-4')
    faq_5_answer = (By.ID, 'accordion__panel-4')
    faq_6_question = (By.ID, 'accordion__heading-5')
    faq_6_answer = (By.ID, 'accordion__panel-5')
    faq_7_question = (By.ID, 'accordion__heading-6')
    faq_7_answer = (By.ID, 'accordion__panel-6')
    faq_8_question = (By.ID, 'accordion__heading-7')
    faq_8_answer = (By.ID, 'accordion__panel-7')


    def click_on_faq_questions(self, faq_question):
        self.driver.find_element(*faq_question).click()

    def get_faq_answer_text(self, faq_answer):
        return self.driver.find_element(*faq_answer).text
