# from playwright.async_api import Page
#
#
# class ElementHandler:
#     def __init__(self, page: Page):
#         self.page: Page = page
#
#     def _get_by_class_name(self, class_name: str, text: str | None = None):
#         element = self.page.locator(f".{class_name}")
#         if text:
#             return element.filter(has_text=text)
#         return element
#
#     def click(self, element: str):
#         self.page.locator(element).click()
#
#     def fill(self):
#
# class ElementFinder:
#     def __init__(self, page: Page):
#         self.page: Page = page
#
