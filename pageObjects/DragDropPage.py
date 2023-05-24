from selenium.webdriver.common.by import By


class DragDropPage:
    def __init__(self,driver):
        self.driver = driver

    slider_15 = (By.XPATH, "//input[@value='15']")
    slider_value = (By.ID, "rangeSuccess")

    def get_slider_15(self):
        return self.driver.find_element(*DragDropPage.slider_15)

    def get_slider_value(self):
        return self.driver.find_element(*DragDropPage.slider_value)