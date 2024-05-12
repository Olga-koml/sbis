import allure

from pages.base_test import BaseTest


@allure.feature("Functionality of download file on sbis page")
class TestDownloadPage(BaseTest):

    EXPECTED_SIZE_FILE_MB = 7.12

    @allure.title("Download zip file process")
    @allure.severity("Critical")
    def test_download_local_version_sbis(self):
        self.sbis_page.open()
        self.download_page.click_download_local_sbis()
        old_url = self.download_page.current_url()
        self.download_page.wait_until_change_url(old_url)
        self.download_page.click_on_plugin()
        self.download_page.click_on_window_section()
        dw_href = self.download_page.download_file_and_get_link()
        dw_file_name = self.download_page.get_downloaded_file_name(dw_href)
        self.download_page.wait_to_download(dw_file_name)

    @allure.title("Сheck downloaded size file")
    @allure.severity("Critical")
    def test_downloaded_file_size(self):
        is_dir_exist = self.download_page.check_dir_is_exist()
        assert is_dir_exist is True, (
            'Directory is not exist'
        )
        is_dir_is_not_empty = self.download_page.is_dir_not_empty()
        assert is_dir_is_not_empty is True, (
            'Directory is empty'
        )
        downloaded_file_size = self.download_page.get_first_file_size()
        assert downloaded_file_size == self.EXPECTED_SIZE_FILE_MB, (
            f'Downloaded file size {downloaded_file_size} Mb, '
            f' expected: {self.EXPECTED_SIZE_FILE_MB} Mb'
        )
