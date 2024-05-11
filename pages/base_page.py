from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging
import allure
from allure_commons.types import AttachmentType


class BasePage:
    '''Base class for pages.'''

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def open(self):
        '''Open page.'''
        with allure.step(f'Open {self.PAGE_URL} page'):
            self.driver.get(self.PAGE_URL)
            self.logger.info(f'Page {self.PAGE_URL} opened')

    def is_opened(self):
        '''Check that open main url of page.'''
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))
            self.logger.info(f'Current page {self.PAGE_URL} is opened')

    def switch_to_window(self, win_number):
        '''Switch to window by window number.'''
        with allure.step(f"Swith to widow number {win_number}"):
            return self.driver.switch_to.window(
                self.driver.window_handles[win_number]
                )

    @allure.step('Get title of current page')
    def current_title(self):
        '''Get title of current page.'''
        title = self.driver.title
        self.logger.info(f'Current title page: {title}')
        return title

    @allure.step('Get url of current page.')
    def current_url(self):
        '''Get url of current page.'''
        current_url = self.driver.current_url
        self.logger.info(f'Current url page: {current_url}')
        return current_url

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
        self.logger.info(f'Maked screenshot {screenshot_name}')
