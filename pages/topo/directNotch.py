from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage
class DirectNotchPage(BasePage):  # Класс представляет решение прямой засечки
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Topo/DirectNotch")

    def fill_direct_notch_data(self, x_obs_post_left, y_obs_post_left, h_obs_post_left,
                               left_direction_angle, left_elevation_angle,
                               x_obs_post_right, y_obs_post_right, h_obs_post_right,
                               right_direction_angle, right_elevation_angle):
        """
        Заполнение данных по цели
        :param x_obs_post_left: Координаты по левому КНП X
        :param y_obs_post_left: Координаты по левому КНП Y
        :param h_obs_post_left: Высота по левому КНП
        :param left_direction_angle: Угол места по левому КНП
        :param left_elevation_angle: Дальность наблюдения по левому КНП
        :param x_obs_post_right: Координаты по правому КНП X
        :param y_obs_post_right: Координаты по правому КНП Y
        :param h_obs_post_right: Высота по правому КНП H
        :param right_direction_angle: Угол места по правому КНП
        :param right_elevation_angle: Дальность наблюдения по правому КНП
        """
        self.fill_input('#leftObservePostPosition-x',x_obs_post_left)
        self.fill_input('#leftObservePostPosition-y', y_obs_post_left)
        self.fill_input('#leftObservePostPosition-h', h_obs_post_left)
        self.fill_input('#topoData-leftDirectionAngle', left_direction_angle)
        self.fill_input('#topoData-leftElevationAngle', left_elevation_angle)
        self.fill_input('#rightObservePostPosition-x', x_obs_post_right)
        self.fill_input('#rightObservePostPosition-y', y_obs_post_right)
        self.fill_input('#rightObservePostPosition-h', h_obs_post_right)
        self.fill_input('#topoData-rightDirectionAngle', right_direction_angle)
        self.fill_input('#topoData-rightElevationAngle', right_elevation_angle)
        calculate_button = self.page.locator("#calculate-button")
        calculate_button.click()
        self.page.locator(".refresh-icon").click()