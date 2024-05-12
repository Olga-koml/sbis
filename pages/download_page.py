import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
import os
import glob
import time


class DownloadPage(BasePage):

    DOWNLOAD_LINK = (By.CSS_SELECTOR, 'a[href="/download"]')
    # DOWNLOAD_LINK = (By.LINK_TEXT, 'скачать локальные версии')
    PLAGIN = (By.CSS_SELECTOR, '[data-id="plugin"]')
    WINDOWS_SECTION = (
        By.XPATH,
        '//div[@data-id="default"]//span[text()="Windows"]'
    )
    DOWNLOAD_ZIP = (By.LINK_TEXT, 'Скачать (Exe 7.12 МБ)')
    DOWNLOAD_DIR = os.path.join(os.getcwd(), 'download_data')

    @allure.step('Click on "Скачать локальные версии"')
    def click_download_local_sbis(self):
        download_link = self.wait.until(
            EC.presence_of_element_located(self.DOWNLOAD_LINK),
            message=(
                f'Element by locator {self.DOWNLOAD_LINK[1]} not clickable'
            )
        )
        self.driver.execute_script("arguments[0].click();", download_link)
        self.logger.info(f'Click on {self.DOWNLOAD_LINK[1]}')

    @allure.step('Click on sbis plugin section')
    def click_on_plugin(self):
        plugin_element = self.wait.until(
            EC.element_to_be_clickable(self.PLAGIN),
            message=(f'Element by locator {self.PLAGIN[1]} not clickable')
        )
        # plugin_element.click()
        self.driver.execute_script("arguments[0].click();", plugin_element)
        self.logger.info(f'Click on {self.PLAGIN[1]}')

    @allure.step('Click on window tab')
    def click_on_window_section(self):

        window_element = self.wait.until(
            EC.element_to_be_clickable(self.WINDOWS_SECTION),
            message=(
                f'Element by locator {self.WINDOWS_SECTION[1]} not clickable'
            )
        )
        self.driver.execute_script("arguments[0].click();", window_element)
        self.logger.info(f'Click on {self.WINDOWS_SECTION[1]}')

    @allure.step('Click to download file and get link')
    def download_file_and_get_link(self):
        file = self.wait.until(
            EC.element_to_be_clickable(self.DOWNLOAD_ZIP),
            message=f'Element by locator {self.DOWNLOAD_ZIP[1]} not clickable'
            )
        file_link = file.get_attribute('href')
        file.click()
        self.logger.info(f'Click to download on {file_link}')
        return file_link

    @allure.step('Check_dir_is_exists')
    def check_dir_is_exist(self):
        if os.path.exists(self.DOWNLOAD_DIR):
            self.logger.info(f'{self.DOWNLOAD_DIR} exists')
            return True
        self.logger.info(f'{self.DOWNLOAD_DIR} doesnt exist')
        return False

    @allure.step('Check is_dir_not_empty')
    def is_dir_not_empty(self):
        if os.listdir(self.DOWNLOAD_DIR):
            self.logger.info(f'{self.DOWNLOAD_DIR} has files')
            return True
        self.logger.info(f'{self.DOWNLOAD_DIR} is empty')
        return False

    @allure.step('Get first file size in directory')
    def get_first_file_size(self):
        files = glob.glob(os.path.join(self.DOWNLOAD_DIR, '*'))
        if files:
            first_file_size_mb = round(
                os.path.getsize(files[0]) / (1024 * 1024),
                2)
            self.logger.info(f'Size of first file is {first_file_size_mb} Mb')
            return first_file_size_mb

    def get_downloaded_file_name(self, href):
        file_name = href.split('/')
        self.logger.info(f'Get downloaded filename: {file_name[-1]}')
        return file_name[-1]

    @allure.step('Wait while file is downloaded')
    def wait_to_download(self, downloaded_file_name):
        self.logger.info(f'Start to download file: {downloaded_file_name}')
        max_wait = 5
        timeout = time.time() + max_wait
        expected_path = os.path.join(self.DOWNLOAD_DIR, downloaded_file_name)
        while time.time() < timeout:
            # print(os.listdir(self.DOWNLOAD_DIR))
            if os.path.isfile(expected_path):
                break
            else:
                time.sleep(.5)
        self.logger.info(f'Dowload file: {downloaded_file_name} complete')
