from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def fill_input(self, selector, value):
        input_element = self.page.locator(selector)
        input_element.fill(value)

    def fill_last_row_input(self, selector, value):
        full_selector = f'.row:last-child {selector}'
        self.fill_input(full_selector, value)

    def fill_last_grid_input(self, selector, value):
        full_selector = f'.grid-strikeout-row-container:last-child {selector}'
        self.fill_input(full_selector, value)

    def select_dropdown_option(
            self,
            parent_locator: Locator,
            index: int,
            value: str,
            dropdown_selector: str = 'span[role="combobox"].select2-selection',
            options_selector: str = 'ul.select2-results__options[role="listbox"]',
            option_selector: str = 'li.select2-results__option:text("{value}")'
    ) -> None:
        """
        Выбирает опцию из выпадающего списка.

        Args:
            parent_locator: Локатор родительского элемента, содержащего выпадающий список
            index: Индекс выпадающего списка (начиная с 0)
            value: Текстовое значение выбираемой опции
            dropdown_selector: CSS-селектор элемента выпадающего списка
            options_selector: CSS-селектор контейнера с опциями
            option_selector: CSS-селектор элементов опций (используйте {value} как плейсхолдер для значения)
        """
        dropdown = parent_locator.locator(dropdown_selector).nth(index)
        dropdown.click()
        self.page.wait_for_selector(options_selector)
        self.page.locator(option_selector.format(value=value)).click()

    def parse_number(self, text):
        """Преобразует текст в число, удаляя неразрывные пробелы"""
        if not text:
            return 0
        num_str = str(text).replace('\xa0', '').replace('-', '')
        return int(num_str) if num_str else 0
