import allure

from pages.base_test import BaseTest


@allure.feature("Functionality of changing region on sbis page")
class TestChangeRegion(BaseTest):

    YAROSLAVSKAY = 'Ярославская обл.'
    KAMCHATSKIJ = 'Камчатский край'
    KAMCHATSKIJ_IN_URL = 'kamchatskij'

    @allure.title("Click contacts on sbis page")
    @allure.severity("Critical")
    def test_contacts_clickable_on_sbis_page(self):
        self.sbis_page.open()
        self.sbis_page.click_section_contact()

    @allure.title("Check and change region and parners in contacts")
    @allure.severity("Critical")
    def test_check_current_region_in_contacts(self):
        self.sbis_contacts_page.open()
        yar_region = self.sbis_contacts_page.find_current_region()
        assert yar_region == self.YAROSLAVSKAY, (
            f'Current region {yar_region}, expected: {self.YAROSLAVSKAY}'
        )
        self.sbis_contacts_page.make_screenshot(f'{yar_region}')
        partners = self.sbis_contacts_page.find_partners_list()
        assert len(partners) > 0, ('Partners list not found')
        self.sbis_contacts_page.click_current_region_link()
        old_url = self.sbis_contacts_page.current_url()
        self.sbis_contacts_page.change_region()
        self.sbis_contacts_page.wait_until_change_url(old_url)
        kam_region = self.sbis_contacts_page.find_current_region()
        assert kam_region == self.KAMCHATSKIJ, (
            f'Current region {kam_region}, expected: {self.KAMCHATSKIJ}'
        )
        self.sbis_contacts_page.make_screenshot(f'{kam_region}')
        assert kam_region != yar_region, (
            f'Current region {kam_region}, expected: {self.KAMCHATSKIJ}'
        )
        kam_partners = self.sbis_contacts_page.find_partners_list()
        assert kam_partners != partners, (
            'Partners list for new region not changed'
        )
        current_url = self.sbis_contacts_page.current_url()
        assert self.KAMCHATSKIJ_IN_URL in current_url, (
            f'Current url {current_url} does not contain: '
            f'{self.KAMCHATSKIJ_IN_URL}'
        )
        current_title = self.sbis_contacts_page.current_title()
        assert self.KAMCHATSKIJ in current_title, (
            f'Current title {current_title}, expected {self.KAMCHATSKIJ}'
        )
