from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage


class ReconFrontiersPage(BasePage): # Класс представляет заполнение страницы Рубежи ЗО
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Recon/ReconFrontiers")


    def fill_frontiers_data(self, x_l, y_l, h_l, x_r, y_r, h_r):
        """
        Заполняет данные по созданию Рубежей ЗО
        :param x_l: Координаты по X левого рубежа
        :param y_l: Координаты по Y правого рубежа
        :param h_l: Высота левого рубежа
        :param x_r: Координаты по X правого рубежа
        :param y_r: Координаты по Y правого рубежа
        :param h_r: Высота правого рубежа
        """
        self.page.locator("#createButton").click()
        self.fill_last_row_input('div[id$="-leftFrontier-x"][contenteditable="true"][v-mask="preset:coordX"]', x_l)
        self.fill_last_row_input('div[id$="-leftFrontier-y"][contenteditable="true"][v-mask="preset:coordY"]', y_l)
        self.fill_last_row_input('div[id$="-leftFrontier-h"][contenteditable="true"][v-number="intLen:4; fractLen:0"]',h_l)

        self.fill_last_row_input('div[id$="-rightFrontier-x"][contenteditable="true"][v-mask="preset:coordX"]', x_r)
        self.fill_last_row_input('div[id$="-rightFrontier-y"][contenteditable="true"][v-mask="preset:coordY"]', y_r)
        self.fill_last_row_input('div[id$="-rightFrontier-h"][contenteditable="true"][v-number="intLen:4; fractLen:0"]',
                                 h_r)

        save_btn_frontiers = self.page.locator("#saveButton")
        if "disabled" not in (save_btn_frontiers.get_attribute("class") or ""):
            self.page.evaluate('document.querySelector(".footer")')
            save_btn_frontiers.click()

        self.page.locator(".refresh-icon").click()