from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from tests.conftest import change_test_status


class DragDropSliders:
    def __init__(self, driver):
        self.driver = driver

    drag_and_drop_slider_link = (By.LINK_TEXT, "Drag & Drop Sliders")
    slider_range = (By.CSS_SELECTOR, "#rangeSuccess")
    slider_element = (By.CSS_SELECTOR, ".sp__range-success input[type='range']")


    def click_drag_drop_sliders(self):
        self.driver.find_element(*DragDropSliders.drag_and_drop_slider_link).click()

    def drag_slider(self, value):
        slider = self.driver.find_element(*DragDropSliders.slider_element)
        slider_width = slider.size['width']
        slider_range = self.driver.find_element(*DragDropSliders.slider_range)
        range_width = 52#int(slider_range.get_attribute("value"))

        current_value = 0
        if range_width != value:
            current_value = int(range_width)
            slider_location = slider.location['x']
            drag_offset = int((value - current_value) / 100 * slider_width)

            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(slider, drag_offset, 0).perform()

    def validate_slider_value(self, expected_value):
        slider_range = self.driver.find_element(*DragDropSliders.slider_range)
        range_width = int(slider_range.get_attribute("value"))
        change_test_status(self.driver,range_width == expected_value)
        return range_width == expected_value
