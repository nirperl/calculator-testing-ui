import pytest
import pytest_asyncio
from playwright.async_api import Page
from src.web.calculator import CalculatorPage, OperatorType


@pytest_asyncio.fixture(scope="session")
async def new_page(browser) -> Page:
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()

@pytest_asyncio.fixture(scope="function")
async def calculator(new_page) -> CalculatorPage:
    return CalculatorPage(new_page, "https://testsheepnz.github.io/BasicCalculator.html")


class TestCalculator:
    @pytest.mark.asyncio
    async def test_add(self, calculator: CalculatorPage):
        await calculator.navigate()
        await calculator.set_first_number(5)
        await calculator.set_second_number(10)
        await calculator.set_operator(OperatorType.ADD)
        await calculator.click_calculate()
        assert await calculator.get_answer() == "15"
