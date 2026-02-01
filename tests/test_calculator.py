import pytest
from playwright.sync_api import sync_playwright
from src.web.calculator import OperatorType, PageManager


@pytest.fixture(scope="session")
def browser():
    """Session-scoped browser fixture"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


POSITIVE_DATA = [
    ("10.3", "5", OperatorType.ADD, "15.3"),
    ("12", "3", OperatorType.DIVIDE, "4"),
    ("2", "4", OperatorType.MULTIPLY, "8"),
    ("10", "5", OperatorType.SUBTRACT, "5"),
    ("100", "25", OperatorType.CONCATENATE, "10025"),
]

# NEGATIVE_DATA = [
#     ("11111111111", "1111111111")
#     ("a"),
#     ("1a")
# ]

BUILD_DATA = ["Prototype"]  # , "1", "2", "3", "4", "5", "6", "7", "8", "9"]


class TestCalculator:
    @pytest.mark.parametrize("build", BUILD_DATA)
    @pytest.mark.parametrize("first_num, second_num, operator, expected_answer", POSITIVE_DATA)
    def test_positive_flow(
        self, browser, build, first_num, second_num, operator: OperatorType, expected_answer
    ):
        page_manager: PageManager = PageManager(
            browser, "https://testsheepnz.github.io/BasicCalculator.html"
        )
        page_manager.initialize()
        page_manager.calculator.navigate()
        page_manager.calculator.build.value = build
        assert page_manager.calculator.check_answer(
            first_num, second_num, operator, expected_answer
        )

    def test_wrong_values(self, browser):
        too_long_num = "11111111111"
        max_size_num = "1111111111"
        page_manager: PageManager = PageManager(
            browser, "https://testsheepnz.github.io/BasicCalculator.html"
        )
        page_manager.initialize()
        page_manager.calculator.navigate()
        page_manager.calculator.first_number.value = too_long_num
        assert page_manager.calculator.first_number.value == max_size_num
