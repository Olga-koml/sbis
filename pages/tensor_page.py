import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links
from pages.base_page import BasePage


class TensorPage(BasePage):

    PAGE_URL = Links.TENSOR_PAGE
    STRENGH_IN_PEOPLE_BLOCK = (By.CLASS_NAME, 'tensor_ru-Index__block4-bg')
    DETAIL_LINK = (
        By.CSS_SELECTOR,
        f'.{STRENGH_IN_PEOPLE_BLOCK[1]} .tensor_ru-Index__link'
    )
    WORKER_BLOCK = (
        By.CSS_SELECTOR,
        'div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3'
    )

    @allure.step('Check presence block "Сила в людях" on page')
    def find_block(self):
        '''Find block "Сила в людях" on tensor pase.'''
        self.wait.until(
            EC.presence_of_element_located(self.STRENGH_IN_PEOPLE_BLOCK),
            message=(f'Block by locator ({self.STRENGH_IN_PEOPLE_BLOCK[1]})'
                     f' not found')
        )
        self.logger.info(
            f'Block {self.STRENGH_IN_PEOPLE_BLOCK[1]}'
            f' presense on page'
        )

    @allure.step('Text of block "Сила в людях"')
    def find_block_text(self):
        '''Get text of block'''
        element = self.wait.until(
            EC.visibility_of_element_located(self.STRENGH_IN_PEOPLE_BLOCK),
            message=(f'Element by locator {self.STRENGH_IN_PEOPLE_BLOCK[1]}'
                     f' not visibile')
        )
        self.logger.info(
            f'return from locator {self.STRENGH_IN_PEOPLE_BLOCK[1]}'
            f' images {element.text}'
        )
        return element.text

    @allure.step('Click on link "Подробнее"')
    def click_detail_link(self):
        '''Click on link "Подробнее".'''
        # кликнуть через click() не получилось
        # self.wait.until(EC.element_to_be_clickable(self.DETAIL_LINK)).click()
        self.driver.execute_script(
            "arguments[0].click();",
            self.wait.until(
                EC.element_to_be_clickable(self.DETAIL_LINK),
                message=(f'Element by locator {self.DETAIL_LINK[1]}'
                         f' not clickable')
            )
        )
        self.logger.info(f'Click on link by locator {self.DETAIL_LINK[1]}')
