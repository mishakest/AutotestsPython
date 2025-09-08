from playwright.sync_api import Page

from models.coord.polar import CoordPolar
from models.coord.rect import CoordRect
from tests.conftest import BASE_URL
from pages.base_page import BasePage


class ReconStopwatchPage(BasePage):  # Класс представляет собой расчет по секундомеру в разведке
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Recon/ReconStopwatch")

    def fill_inputdata_all(self, observe_post: CoordRect, measure: CoordPolar, time: float, sonic_speed: float):
        """
        Заполняет данные в поля для расчета дальномера/РЛС и выполняет расчет
        :param observe_post: Координаты КНП
        :param measure: Измерение
        :param time: Время
        :param sonic_speed: Скорость звука
        """
        self.fill_input('#observePost-x', observe_post.x_str)
        self.fill_input('#observePost-y', observe_post.y_str)
        self.fill_input('#observePost-h', observe_post.h_str)

        sonic_speed_input = self.page.locator('#sonic-speed')
        sonic_speed_input.click()
        sonic_speed_input.fill(str(sonic_speed))

        time_input = self.page.locator('#stopwatch-time')
        time_input.click()
        time_input.type(str(time))

        self.fill_input('#topoData-directionAngle', measure.alpha_str)
        self.fill_input('#topoData-elevationAngle', measure.epsilon_str)

        calculate_button = self.page.locator("#calculate-button")
        calculate_button.click()

    def get_observe_post(self) -> CoordRect:
        """Получить координаты КНП"""
        return CoordRect(
            int(self.page.locator("#observePost-x").text_content()),
            int(self.page.locator("#observePost-y").text_content()),
            int(self.page.locator("#observePost-h").text_content())
        )

    def get_measure(self) -> CoordPolar:
        """Получить данные измерений"""
        return CoordPolar(
            alpha=int(self.page.locator("#topoData-directionAngle").text_content()),
            distance=None,
            epsilon=int(self.page.locator("#topoData-elevationAngle").text_content())
        )

    def get_result(self) -> CoordRect:
        """Выполнить расчет"""

        def parse_number(text):
            if not text:
                return 0
            return int(''.join(c for c in str(text) if c.isdigit() or (c == '-' and not str(text).index(c))))

        x = parse_number(self.page.locator("#target-x").text_content())
        y = parse_number(self.page.locator("#target-y").text_content())
        h = parse_number(self.page.locator("#target-h").text_content())

        return CoordRect(x, y, h)
