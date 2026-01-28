from calendar import firstweekday

import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

from src.web.calculator import OperatorType, PageManager


@pytest.fixture(scope="session")
def browser():
    """Session-scoped browser fixture"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


DATA = [
    ("10.3", "5", OperatorType.ADD, "15.3"),
    ("12", "3", OperatorType.DIVIDE, "4"),
    ("2", "4", OperatorType.MULTIPLY, "8"),
    ("10", "5", OperatorType.SUBTRACT, "5"),
    ("100", "25", OperatorType.CONCATENATE, "10025")
]


class TestCalculator:
    @pytest.mark.parametrize("first_num, second_num, operator, expected_answer", DATA)
    def test_positive_flow(self, browser, first_num, second_num, operator: OperatorType, expected_answer):
        page_manager: PageManager = PageManager(browser, "https://testsheepnz.github.io/BasicCalculator.html")
        page_manager.initialize()
        page_manager.calculator.navigate()
        assert page_manager.calculator.check_answer(first_num, second_num, operator, expected_answer)
