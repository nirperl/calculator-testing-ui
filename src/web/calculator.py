from enum import Enum
from playwright.sync_api import Page, expect

from web.elements import Inputbox, DropDownList


class OperatorType(Enum):
    ADD = 0
    SUBTRACT = 1
    MULTIPLY = 2
    DIVIDE = 3
    CONCATENATE = 4


class CalculatorPage:
    def __init__(self, page, url):
        self._page: Page = page
        self.url = url
        self.first_number = Inputbox(self._page,"#number1Field")
        self.second_number = Inputbox(self._page,"#number2Field")
        self.operator = DropDownList(self._page,"#selectOperationDropdown")

    def navigate(self):
        self._page.goto(self.url)

    def click_calculate(self):
        self._page.locator("#calculateButton").click()

    def get_answer(self) -> str:
        return self._page.locator("input[id='numberAnswerField']").input_value()

    def set_build(self, build_number: str):
        self._page.locator("#selectBuild").select_option(value=build_number)

    def wait_for_answer(self, expected_answer: str) -> bool:
        try:
            expect(self._page.locator("input[id='numberAnswerField']")).to_have_value(expected_answer)
            return True
        except Exception as e:
            print(f"Error waiting for answer: {e}")
            return False

    def get_error(self) -> str:
        return self._page.locator("#errorMsgField").text_content()

    def clear_all(self):
        self._page.locator("input", has_text="Clear").click()

    def set_integer_only(self, to_select: bool):
        self._page.locator("#integerSelect").set_checked(to_select)

    def get_error_message(self):
        self._page.locator("#errorMsgField").text_content()

    def check_answer(self, first_num, second_num, operator: OperatorType, expected_answer: str) -> bool:
        self.first_number = first_num
        self.second_number = second_num
        self.math_operator = operator
        self.click_calculate()
        return self.wait_for_answer(expected_answer)


class PageManager:
    def __init__(self, browser, url):
        self._browser = browser
        self._url = url
        self._context = None
        self._page = None
        self.calculator: CalculatorPage = None

    def initialize(self):
        self._context = self._browser.new_context()
        self._page = self._context.new_page()
        self.calculator = CalculatorPage(self._page, self._url)
