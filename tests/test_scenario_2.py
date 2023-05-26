import time

import pytest
from pageObjects.SeleniumPlaygroundPage import SeleniumPlaygroundPage
from pageObjects.DragDropSliders import DragDropSliders
from tests.conftest import change_test_status


@pytest.mark.usefixtures("driver_init")
@pytest.mark.timeout(20)
class TestScenario2:
    def test_scenario_2(self, driver_init):
        selenium_playground = SeleniumPlaygroundPage(driver_init)
        selenium_playground.open_playground()
        drag_drop_sliders = selenium_playground.click_drag_drop_sliders()
        desired_value = 95
        drag_drop_sliders.drag_slider(desired_value)
        assert drag_drop_sliders.validate_slider_value(desired_value)

