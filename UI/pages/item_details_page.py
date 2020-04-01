from UI.base.base_class import BaseClass


class ItemDetailsPage(BaseClass):
    # selectors
    item_title = "//h1[@class='_1sjrk']"
    add_to_cart_button = "//button[@id='add-to-cart-button']"
    go_to_cart_button = "//a[@class='_13q9y _8tsq7 _nt6qd']"

    def click_add_to_cart_button(self):
        self.wait_element_to_be_clickable(ItemDetailsPage.add_to_cart_button).click()

    def click_go_to_cart_button(self):
        self.wait_element_to_be_clickable(ItemDetailsPage.go_to_cart_button).click()
