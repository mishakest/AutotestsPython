from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage
class DirectGeoTaskPage(BasePage):  # Класс представляет решение ПГЗ
    def __init__(self, page: Page):
        super().__init__(page)  # Инициализация базового класса
        self.page.goto(f"{BASE_URL}/Topo/DirectGeoTask")

    def fill_direct_geo_task_data(self, x_0, y_0, h_0, elevation_angle, distance, amount,
                                  elevation_angle_two, distance_two, amount_two):
        """
        Заполнение данных по цели
        :param x_0: Координаты по первому ходу X
        :param y_0: Координаты по первому ходу Y
        :param h_0: Высота по первому ходу
        :param elevation_angle: угол места (первый ход)
        :param distance: Дальность наблюдения (первый ход)
        :param amount: ε (эпсилон (первый ход))
        :param elevation_angle_two: угол места (второй ход)
        :param distance_two: Дальность наблюдения (второй ход)
        :param amount_two: ε (эпсилон(второй ход))
        """
        self.fill_input('#observePost-x', x_0)
        self.fill_input('#observePost-y', y_0)
        self.fill_input('#observePost-h', h_0)
        self.fill_input('div[id$="-directionAngle"]', amount)
        self.fill_input('div[id$="-distance"]', distance)
        self.fill_input('div[id$="-elevationAngle"]', elevation_angle)
        calculate_button = self.page.locator("#calculate-button")
        calculate_button.click()
        self.fill_input('div[id$="-directionAngle"]', amount_two)
        self.fill_input('div[id$="-distance"]', distance_two)
        self.fill_input('div[id$="-elevationAngle"]', elevation_angle_two)
        calculate_button.click()

        self.page.locator(".refresh-icon").click()