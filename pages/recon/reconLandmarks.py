from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage


class ReconLandmarksPage(BasePage): # Класс представляет создание ориентиров
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Recon/ReconLandmarks")

    def fill_landmarks_data(self, x, y, h ):
        """
        Заполняет данные по созданию ориентиров
        :param x: Координаты по X цели
        :param y: Координаты по Y цели
        :param h: Координаты по H цели
        """
        self.page.locator("#createButton").click()
        self.fill_last_row_input('div[contenteditable="true"][v-mask="preset:coordX"]', x)
        self.fill_last_row_input('div[contenteditable="true"][v-mask="preset:coordY"]', y)
        self.fill_last_row_input('div[contenteditable="true"][v-number="intLen:4; fractLen:0"]', h)

        save_btn_landmarks = self.page.locator("#saveButton")
        if "disabled" not in (save_btn_landmarks.get_attribute("class") or ""):
            self.page.evaluate('document.querySelector(".footer")')
            save_btn_landmarks.click()

        self.page.locator(".refresh-icon").click()