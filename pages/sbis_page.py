import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links
from pages.base_page import BasePage


class SbisPage(BasePage):

    PAGE_URL = Links.SBIS_PAGE
    CONTACTS_BUTTON = (By.LINK_TEXT, 'Контакты')
    TENSOR_BUNNER = (By.CSS_SELECTOR, 'a.sbisru-Contacts__logo-tensor')

    @allure.step('Click on section contacts')
    def click_section_contact(self):
        '''Click on section contact on sbis page.'''
        self.wait.until(
            EC.element_to_be_clickable(self.CONTACTS_BUTTON),
            message=f'Section {self.CONTACTS_BUTTON} not found'
            ).click()
        self.logger.info(f'Click on {(self.CONTACTS_BUTTON)}')

    @allure.step('Click on tensor banner')
    def click_tensor_banner(self):
        '''Click on tensor banner on sbis page.'''
        self.wait.until(
            EC.element_to_be_clickable(self.TENSOR_BUNNER),
            message=f'Section {self.TENSOR_BUNNER} not found').click()
        self.logger.info(f'Click on {(self.TENSOR_BUNNER)}')
