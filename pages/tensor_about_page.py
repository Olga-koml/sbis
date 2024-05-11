import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links
from pages.base_page import BasePage


class TensorAboutPage(BasePage):

    PAGE_URL = Links.TENSOR_ABOUT_PAGE
    WORKER_BLOCK = (
        By.CSS_SELECTOR,
        'div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3'
    )

    @allure.step('Return images from page')
    def get_images(self):
        '''Get images from tensor/about page worker block.'''
        block = self.wait.until(
            EC.visibility_of_element_located(self.WORKER_BLOCK),
            message=f'Block by locator ({self.WORKER_BLOCK[1]}) not visibility'
        )
        images = block.find_elements(By.TAG_NAME, 'img')
        self.logger.info(f'Get images by locator {self.WORKER_BLOCK[1]}')
        return images
