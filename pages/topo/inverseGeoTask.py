from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage
class InverseGeoTaskPage(BasePage):  # Класс представляет решение ОГЗ
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Topo/InverseGeoTask")

    def fill_inverse_geo_task_data(self, x_target, y_target, h_target,
                                   x_1, y_1, h_1, x_2, y_2, h_2, x_3, y_3, h_3):
        """
        Заполнение данных по цели
        :param x_target: Координаты X по цели
        :param y_target: Координаты Y по цели
        :param h_target: Высота цели
        :param x_1: Координаты X по первому КНП
        :param y_1: Координаты Y по первому КНП
        :param h_1: Координаты H по первому КНП
        :param x_2: Координаты X по второму КНП
        :param y_2: Координаты Y по второму КНП
        :param h_2: Координаты H по второму КНП
        :param x_3  Координаты X по третьему КНП
        :param y_3  Координаты Y по третьему КНП
        :param h_3  Координаты H по третьему КНП
        """
        self.fill_input('#target-x', x_target)
        self.fill_input('#target-y', y_target)
        self.fill_input('#target-h', h_target)
        self.fill_input('#observePost-1-x', x_1)
        self.fill_input('#observePost-1-y', y_1)
        self.fill_input('#observePost-1-h', h_1)
        self.fill_input('#observePost-2-x', x_2)
        self.fill_input('#observePost-2-y', y_2)
        self.fill_input('#observePost-2-h', h_2)
        self.fill_input('#observePost-3-x', x_3)
        self.fill_input('#observePost-3-y', y_3)
        self.fill_input('#observePost-3-h', h_3)
        calculate_button = self.page.locator("#calculate-button")
        calculate_button.click()
        self.page.locator(".refresh-icon").click()