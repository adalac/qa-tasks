from UI.base.base_class import BaseClass

class LandingPage(BaseClass):
    # selectors
    close_consent_button = "//button[@data-role='close-and-accept-consent']"

    def click_close_consent_button(self):
        self.wait_element_to_be_clickable(LandingPage.close_consent_button).click()