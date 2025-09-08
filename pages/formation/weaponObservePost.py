from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage


class WeaponFormationObsPostPage(BasePage): # Класс по созданию КНП
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Formation/WeaponObservePost")

    def fill_obs_post_data(self, obs_post_type, x, y, h):
        """
        Заполнение данных по метео
        :param obs_post_type: Характер
        :param x: Координата X
        :param y: Координата Y
        :param h: Высота КНП
        """

        self.page.locator("#createButton").click()
        self.page.wait_for_selector('#mainTable .row:last-child')
        last_row = self.page.locator('#mainTable .row:last-child')

        last_dropdown = last_row.locator('span.select2-selection__rendered')
        last_dropdown.click()
        self.page.wait_for_selector('ul.select2-results__options')
        self.page.locator(f'ul.select2-results__options li:has-text("{obs_post_type}")').click()

        self.fill_input('div[contenteditable="true"][v-mask="preset:coordX"]', x)
        self.fill_input('div[contenteditable="true"][v-mask="preset:coordY"]', y)
        self.fill_input('div[v-number="intLen:4; fractLen:0"]', h)

    # Находим кнопку "Сохранить" в окне
        save_button = self.page.locator("#saveButton")
        button_classes = save_button.get_attribute("class") or ""
        if "disabled" not in button_classes:
            # Отключаем перехват событий футером
            self.page.evaluate('document.querySelector(".footer")')
            save_button.click()
        else:
            print("Кнопка 'Сохранить' неактивна (класс 'disabled' присутствует), пропускаем шаг.")

        self.page.locator(".refresh-icon").click()