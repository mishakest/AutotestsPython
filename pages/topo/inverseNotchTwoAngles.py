from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage
class InverseNotchTwoAnglesPage(BasePage):  # Класс представляет решение задачи обратной по углам засечки
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Topo/InverseNotchTwoAngles")

    def fill_inverse_notch_two_angles_data(self, x_3, y_3, x_2, y_2, x_1, y_1, alpha_angle,  betta_angle,):
        """
        Заполнение данных по цели
        :param x_3: Координаты по третьей цели X
        :param y_3: Координаты по третьей цели Y
        :param x_2: Координаты по второй цели X
        :param y_2: Координаты по второй цели Y
        :param x_1: Координаты по первой цели X
        :param y_1: Координаты по правому цели Y
        :param alpha_angle: β3-2
        :param betta_angle: β2-1
        """
        self.fill_input('div[id="0-target-x"]', x_3)
        self.fill_input('div[id="0-target-y"]', y_3)
        self.fill_input('div[id="1-target-x"]', x_2)
        self.fill_input('div[id="1-target-y"]', y_2)
        self.fill_input('div[id="2-target-x"]', x_1)
        self.fill_input('div[id="2-target-y"]', y_1)
        self.fill_input('#topoData-alphaAngle', alpha_angle)
        self.fill_input('#topoData-bettaAngle', betta_angle)
        calculate_button = self.page.locator("#calculate-button")
        calculate_button.click()
        self.page.locator(".refresh-icon").click()