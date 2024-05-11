import pytest

from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from pages.tensor_about_page import TensorAboutPage
from pages.sbis_contacts_page import SbisContactsPage


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.sbis_page = SbisPage(driver)
        request.cls.tensor_page = TensorPage(driver)
        request.cls.tensor_about_page = TensorAboutPage(driver)
        request.cls.sbis_contacts_page = SbisContactsPage(driver)
