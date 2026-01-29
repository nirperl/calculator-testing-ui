from playwright.sync_api import Page, expect


class Inputbox:
    def __init__(self, page: Page, locator: str):
        self._locator: str = locator
        self._page = page

    @property
    def value(self) -> str:
        return self._page.locator(self._locator).input_value()

    @value.setter
    def value(self, text: str):
        self._page.locator(self._locator).fill(text)

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
        return self._page.locator(self._locator).input_value()

    @value.setter
    def value(self, operator: str | int, by_index: bool = False):
        if by_index:
            self._page.locator(self._locator).select_option(index=operator)
        else:
            self._page.locator(self._locator).select_option(value=operator)

    @property
    def all_values(self) -> list[str]:
        return self._page.locator(self._locator).all_inner_texts()
