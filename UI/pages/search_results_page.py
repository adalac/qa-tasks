from UI.base.base_class import BaseClass


class SearchResultsPage(BaseClass):
    checkbox_uzywane = "//span[contains(text(), 'używane')]"
    price_from_textbox = "//input[@id='price_from']"
    searching_result = "//div[@class='_9c44d_1V-js']"
    active_filter_element = "//div[@class='_1h7wt _1fwkl _1bo4a _sizcr _yxrn4 _1t9p2 _1o9j9 _1qltd']"

    def click_checkbox_uzywane(self):
        self.wait_element_to_be_clickable(SearchResultsPage.checkbox_uzywane).click()

    def price_from_textbox_input(self, price_from):
        self.wait_element_to_be_clickable(SearchResultsPage.price_from_textbox).send_keys(price_from)

    def click_searching_result(self):
        self.wait_element_to_be_clickable(SearchResultsPage.searching_result).click()