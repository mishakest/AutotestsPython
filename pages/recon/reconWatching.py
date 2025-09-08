from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage


class ReconWatchingPage(BasePage): # Класс представляет расчет СН в разведке
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Recon/ReconWatching")

    def fill_watching_data(self, x_l, y_l, h_l, left_direction_angle, left_elevation_angle,
                           x_r, y_r, h_r, right_direction_angle, right_elevation_angle,):
        """
        Заполнение данных по цели
        :param x_l: Координаты X с левого КНП
        :param y_l: Координаты Y с левого КНП
        :param h_l: Координаты H с левого КНП
        :param left_direction_angle: дирекционный угол по левому КНП
        :param left_elevation_angle: угол места по левому КНП
        :param x_r: Координаты X с левого КНП
        :param y_r: Координаты Y с левого КНП
        :param h_r: Координаты H с левого КНП
        :param right_direction_angle: дирекционный угол по левому КНП
        :param right_elevation_angle: угол места по левому КНП
        """

        self.fill_input('#leftObservePostPosition-x', x_l)
        self.fill_input('#leftObservePostPosition-y', y_l)
        self.fill_input('#leftObservePostPosition-h', h_l)
        self.fill_input('#topoData-leftDirectionAngle', left_direction_angle)
        self.fill_input('#topoData-leftElevationAngle', left_elevation_angle)
        self.fill_input('#rightObservePostPosition-x', x_r)
        self.fill_input('#rightObservePostPosition-y', y_r)
        self.fill_input('#rightObservePostPosition-h', h_r)
        self.fill_input('#topoData-rightDirectionAngle', right_direction_angle)
        self.fill_input('#topoData-rightElevationAngle', right_elevation_angle)

        calculate_button = self.page.locator("#calculate-button")
        calculate_button.click()