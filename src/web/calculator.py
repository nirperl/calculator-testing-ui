from enum import Enum
from playwright.sync_api import Page, expect


class OperatorType(Enum):
    ADD = 0
    SUBTRACT = 1
    MULTIPLY = 2
    DIVIDE = 3
    CONCATENATE = 4


class CalculatorPage:
    def __init__(self, page, url):
        self.page: Page = page
        self.url = url

    def navigate(self):
        self.page.goto(self.url)

    def set_first_number(self, num: str):
        self.page.locator("#number1Field").fill(num)

    def set_second_number(self, num: str):
        self.page.locator("#number2Field").fill(num)

    def set_operator(self, operator: OperatorType):
        self.page.locator("#selectOperationDropdown").select_option(index=operator.value)

    def click_calculate(self):
        self.page.locator("#calculateButton").click()

    def get_answer(self) -> str:
        return self.page.locator("input[id='numberAnswerField']").input_value()

    def set_build(self, build_number: str):
        self.page.locator("#selectBuild").select_option(value=build_number)

    def wait_for_answer(self, expected_answer: str) -> bool:
        try:
            expect(self.page.locator("input[id='numberAnswerField']")).to_have_value(expected_answer)
            return True
        except Exception as e:
            print(f"Error waiting for answer: {e}")
            return False

    def get_error(self) -> str:
        return self.page.locator("#errorMsgField").text_content()

    def clear_all(self):
        self.page.locator("input", has_text="Clear").click()

    def set_integer_only(self, to_select: bool):
        self.page.locator("#integerSelect").set_checked(to_select)

    def check_answer(self, first_num, second_num, operator: OperatorType, expected_answer: str) -> bool:
        self.set_first_number(first_num)
        self.set_second_number(second_num)
        self.set_operator(operator)
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