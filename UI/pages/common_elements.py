from UI.base.base_class import BaseClass


class CommonElements(BaseClass):
    # selectors
    search_box = "//input[@type='search']"
    search_button = "//button[@data-role='search-button']"

    def search_box_input(self, item_name):
        self.wait_element_to_be_clickable(CommonElements.search_box).send_keys(item_name)

    def click_search_button(self):
        self.wait_element_to_be_clickable(CommonElements.search_button).click()
