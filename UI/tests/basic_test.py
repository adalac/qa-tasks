from UI.base.base_class import BaseClass
from UI.pages.common_elements import CommonElements
from UI.pages.search_results_page import SearchResultsPage
from selenium.webdriver.common.keys import Keys
from UI.pages.landing_page import LandingPage
from UI.pages.item_details_page import ItemDetailsPage
from UI.pages.cart_page import CartPage
import time


class BasicTest(BaseClass):
    def test_basic_test(self):
        LandingPage.click_close_consent_button(self)
        CommonElements.search_box_input(self, "komputer")
        CommonElements.click_search_button(self)
        SearchResultsPage.click_checkbox_uzywane(self)
        SearchResultsPage.price_from_textbox_input(self, "200")
        SearchResultsPage.price_from_textbox_input(self, Keys.ENTER)
        time.sleep(3)
        SearchResultsPage.click_searching_result(self)
        item = self.wait_element_to_be_visible(ItemDetailsPage.item_title).text
        ItemDetailsPage.click_add_to_cart_button(self)
        ItemDetailsPage.click_go_to_cart_button(self)
        self.assertEqual(item, self.wait_element_to_be_visible(CartPage.item_title).text, "Titles do not match")
