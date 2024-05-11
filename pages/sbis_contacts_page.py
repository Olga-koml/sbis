import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links
from pages.base_page import BasePage


class SbisContactsPage(BasePage):

    PAGE_URL = Links.SBIS_CONTACTS_PAGE
    CURRENT_REGION = (
        By.CSS_SELECTOR,
        '.sbisru-Contacts__relative .sbis_ru-Region-Chooser__text'
    )
    PARTNERS_LIST = (By.CSS_SELECTOR, 'div.sbisru-Contacts-List__item')
    REGION_FIELD = (By.CSS_SELECTOR, 'input.controls-Field')
    # REGION_KAMCHATSKIY = (By.XPATH, '//span[@title="Камчатский край"]')
    REGION_KAMCHATSKIY = (By.CSS_SELECTOR, 'span[title="Камчатский край"]')

    @allure.step('Find current region')
    def find_current_region(self):
        '''Find current region.'''
        region = self.wait.until(
            EC.visibility_of_element_located(self.CURRENT_REGION),
            message=(f'Element by locator {self.CURRENT_REGION[1]}'
                     f' not visibile')
        )
        regtion_text = region.text
        self.logger.info(f'Get current region: {regtion_text}')
        return regtion_text

    @allure.step('Find section partners list')
    def find_partners_list(self):
        '''Find section partners list'''
        partners = self.wait.until(
            EC.presence_of_all_elements_located(self.PARTNERS_LIST),
            message=(f'Partners by locator {self.PARTNERS_LIST[1]}'
                     f' not found')
        )
        # for partner in partners:
        #     title_element = partner.find_element(
        #         By.CSS_SELECTOR,
        #         '.sbisru-Contacts-List__name')
        #     title = title_element.get_attribute('title')

        self.logger.info(
            f'Get number partners in curr region: {len(partners)}'
        )
        return partners

    @allure.step('Click on current region link')
    def click_current_region_link(self):
        '''Click on current region link.'''
        self.wait.until(
            EC.element_to_be_clickable(self.CURRENT_REGION),
            message=f'Link {self.CURRENT_REGION[1]} not found'
            ).click()
        self.logger.info(f'Click on {(self.CURRENT_REGION[1])}')

    @allure.step('Change ragion on page contacts.')
    def change_region(self):
        '''Change region on page contacts.'''
        self.wait.until(
            EC.visibility_of_element_located(self.REGION_KAMCHATSKIY),
            message=(f'Field by locator {self.REGION_KAMCHATSKIY[1]}'
                     f' not visibile')
        ).click()
        self.logger.info(f'Click on {(self.REGION_KAMCHATSKIY[1])}')
