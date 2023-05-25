from selenium.webdriver.common.by import By

from pageObjects.DragDropPage import DragDropPage
from pageObjects.InputFormDemo import InputFormDemo
from pageObjects.SimpleFormDemo import SimpleFormDemo


class PlayGroundPage:
    def __init__(self, driver):
        self.driver = driver

    simple_form_demo_link = (By.LINK_TEXT, "Simple Form Demo")
    drag_and_drop_slider_link = (By.LINK_TEXT, "Drag & Drop Sliders")
    input_form_submit_link = (By.XPATH, "//a[normalize-space()='Input Form Submit']")

    def click_simple_form_demo_link(self):
        self.driver.find_element(*PlayGroundPage.simple_form_demo_link).click()
        simpleFormDemo = SimpleFormDemo(self.driver)
        return simpleFormDemo

    def click_drag_and_drop_slider_link(self):
        self.driver.find_element(*PlayGroundPage.drag_and_drop_slider_link).click()
        dragDropPage = DragDropPage(self.driver)
        return dragDropPage

    def click_input_form_submit_link(self):
        self.driver.find_element(*PlayGroundPage.input_form_submit_link).click()
        inputFormDemo = InputFormDemo(self.driver)
        return inputFormDemo
