import allure

from pages.base_test import BaseTest
from config.links import Links


@allure.feature("Functionality page from sbis.ru to tensor/about")
class TestSbisToTensor(BaseTest):

    TEXT_CHECK = 'Сила в людях'

    @allure.title("Page sbis functionality")
    @allure.severity("Critical")
    def test_sbis_page_to_tensor_page(self):

        self.sbis_page.open()
        self.sbis_page.click_section_contact()
        self.sbis_page.click_tensor_banner()
        self.sbis_page.switch_to_window(1)
        self.tensor_page.is_opened()

    @allure.title("Page tensor.ru functionality")
    @allure.severity("Critical")
    def test_tensor_page_to_tensor_about_page(self):

        self.tensor_page.open()  # открываю на случай если первый тест упадет
        self.tensor_page.find_block()
        text = self.tensor_page.find_block_text()
        assert self.TEXT_CHECK in text, (f'{self.TEXT_CHECK} not in {text}')
        self.tensor_page.click_detail_link()
        current_url = self.tensor_page.current_url()
        assert current_url == Links.TENSOR_ABOUT_PAGE, (
            f'Opened page {current_url} expected: {Links.TENSOR_ABOUT_PAGE}'
        )

    @allure.title("Page tensor/about page functionality check block images")
    @allure.severity("Critical")
    def test_images_on_tensor_about_page(self):
        self.tensor_about_page.open()  # на случай если выше тесты упадут
        images = self.tensor_about_page.get_images()
        width_img = images[0].get_attribute('width')
        height_img = images[0].get_attribute('height')
        for num, img in enumerate(images):
            width = img.get_attribute('width')
            height = img.get_attribute('height')
            assert width == width_img, (
                f'Width of pic № {num} - {width} differents than'
                f' first pic width {width_img}'
            )
            assert height == height_img, (
                f'Height of pic {num} - {height} defferents than'
                f' first pic height {height_img}'
            )
