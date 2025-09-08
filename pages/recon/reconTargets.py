from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage


class ReconTargetsPage(BasePage): #Класс представляет создание цели
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Recon/ReconTargets")

    def fill_targets_data(self, x, y, h, front, depth):
        """
        Заполнение данных по цели
        :param x: Координаты по X
        :param y: Координаты по Y
        :param h: Высота цели
        :param front: Фронт цели
        :param depth: Глубина цели
        """

        self.page.locator("#createButton").click()
        self.fill_last_grid_input('div[contenteditable="true"][v-mask="preset:coordX"]', x)
        self.fill_last_grid_input('div[contenteditable="true"][v-mask="preset:coordY"]', y)
        self.fill_last_grid_input('div[contenteditable="true"][v-number="intLen:4; fractLen:0"]', h)
        self.fill_last_grid_input('div[id$="-front"][contenteditable="true"][v-number="intLen:4; fractLen:0; minVal:0"]', front)
        self.fill_last_grid_input('div[id$="-depth"][contenteditable="true"][v-number="intLen:4; fractLen:0; minVal:0"]', depth)

        save_btn_targets = self.page.locator("#saveButton")
        if "disabled" not in (save_btn_targets.get_attribute("class") or ""):
            self.page.evaluate('document.querySelector(".footer")')
            save_btn_targets.click()

        self.page.locator(".refresh-icon").click()





