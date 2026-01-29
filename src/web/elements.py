from playwright.sync_api import Page, expect
from web.calculator import OperatorType


class Inputbox:
    def __init__(self, page: Page, locator: str):
        self._locator: str = locator
        self._page = page

    @property
    def value(self) -> str:
        return self._page.locator(self._locator).input_value()

    @value.setter
    def value(self, num: str):
        self._page.locator(self._locator).fill(num)

    def wait_for_value(self, expected_answer: str) -> bool:
        try:
            expect(self._page.locator(self._locator)).to_have_value(expected_answer)
            return True
        except Exception as e:
            print(f"Error waiting for answer: {e}")
            return False


class DropDownList:
    def __init__(self, page: Page, locator: str):
        self._locator: str = locator
        self._page = page

    @property
    def value(self) -> str:
        return self._page.locator("#selectOperationDropdown").input_value()

    @value.setter
    def value(self, operator: OperatorType):
        self._page.locator("#selectOperationDropdown").select_option(index=operator.value)
