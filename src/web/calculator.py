from enum import Enum
from playwright.async_api import Page


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

    async def navigate(self):
        await self.page.goto(self.url)

    async def set_first_number(self, num: int):
        await self.page.locator("#number1Field").fill(str(num))

    async def set_second_number(self, num: int):
        await self.page.locator("#number1Field").fill(str(num))

    async def set_operator(self, operator: OperatorType):
        await self.page.locator("select").select_option(str(operator.value))

    async def click_calculate(self):
        await self.page.locator("input").click()

    async def get_answer(self) -> str:
        return await self.page.locator("input").text_content()

    async def get_error(self) -> str:
        return await self.page.locator("#errorMsgField").text_content()

    async def clear_all(self):
        await self.page.locator("input", has_text="Clear").click()