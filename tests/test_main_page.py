from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import main_page_data
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.main_page import MainPage
import customer_details_page_data
from pages.customer_details_page import CustomerDetailsPage


@pytest.mark.usefixtures("setup_driver")
class TestMainPageFAQ:

    @pytest.mark.parametrize('faq_question_locator, faq_answer_locator, faq_answer_text', [
        (MainPage.faq_1_question, MainPage.faq_1_answer, main_page_data.faq_1_answer_text),
        (MainPage.faq_2_question, MainPage.faq_2_answer, main_page_data.faq_2_answer_text),
        (MainPage.faq_3_question, MainPage.faq_3_answer, main_page_data.faq_3_answer_text),
        (MainPage.faq_4_question, MainPage.faq_4_answer, main_page_data.faq_4_answer_text),
        (MainPage.faq_5_question, MainPage.faq_5_answer, main_page_data.faq_5_answer_text),
        (MainPage.faq_6_question, MainPage.faq_6_answer, main_page_data.faq_6_answer_text),
        (MainPage.faq_7_question, MainPage.faq_7_answer, main_page_data.faq_7_answer_text),
        (MainPage.faq_8_question, MainPage.faq_8_answer, main_page_data.faq_8_answer_text),
    ])
    def test_correct_text_shown_under_FAQ_questions(self, setup_driver, faq_question_locator, faq_answer_locator, faq_answer_text):
        """
        Проверяем, что при клике на каждый вопрос FAQ отображается правильный текст под ним.
        """
        main_page = MainPage(setup_driver)
        setup_driver.get(main_page_data.main_page_link)
        WebDriverWait(setup_driver, 10).until(lambda d: setup_driver.execute_script("return document.readyState") == "complete")
        WebDriverWait(setup_driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'rcc-confirm-button'))).click()
        setup_driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",setup_driver.find_element(*faq_question_locator))
        WebDriverWait(setup_driver, 10).until(lambda driver: driver.execute_script('return arguments[0].getBoundingClientRect().top <= window.innerHeight && arguments[0].getBoundingClientRect().top >= 0',setup_driver.find_element(*faq_question_locator)))
        main_page.click_on_faq_questions(faq_question_locator)
        WebDriverWait(setup_driver, 10).until(expected_conditions.visibility_of_element_located(faq_answer_locator))
        actual_text = main_page.get_faq_answer_text(faq_answer_locator)

        assert actual_text == faq_answer_text, f"Ответ на вопрос {faq_question_locator} неверный. Ожидалось: {faq_answer_text}, получено: {actual_text}"

    def test_redirect_by_roller_logo(self, setup_driver):
        """
        Проверяем, что при клике на лого с самокатом, пользователя редиректит на главную страницу.
        """
        customer_detail_page = CustomerDetailsPage(setup_driver)
        setup_driver.get(customer_details_page_data.customer_details_page_link)
        WebDriverWait(setup_driver, 10).until(lambda d: setup_driver.execute_script("return document.readyState") == "complete")
        WebDriverWait(setup_driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'rcc-confirm-button'))).click()
        WebDriverWait(setup_driver, 10).until(expected_conditions.element_to_be_clickable((customer_detail_page.roller_logo))).click()
        WebDriverWait(setup_driver, 10).until(lambda d: setup_driver.execute_script("return document.readyState") == "complete")
        assert setup_driver.current_url == main_page_data.main_page_link

    def test_redirect_by_yandex_logo(self, setup_driver):
        """
        Проверяем, что при клике на лого с yandex, пользователю открывается новая вкладка с странице яндекс дзена.
        """
        main_page = MainPage(setup_driver)
        customer_detail_page = CustomerDetailsPage(setup_driver)
        setup_driver.get(main_page_data.main_page_link)
        WebDriverWait(setup_driver, 10).until(lambda d: setup_driver.execute_script("return document.readyState") == "complete")
        WebDriverWait(setup_driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'rcc-confirm-button'))).click()
        WebDriverWait(setup_driver, 10).until(expected_conditions.element_to_be_clickable((main_page.yandex_dzen_logo))).click()
        tabs = setup_driver.window_handles
        setup_driver.switch_to.window(tabs[1])
        assert WebDriverWait(setup_driver, 10).until(expected_conditions.url_to_be(main_page_data.yandex_dzen_link))


