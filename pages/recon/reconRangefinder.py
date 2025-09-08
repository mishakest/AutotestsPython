import time
from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage
from models.coord.rect import CoordRect
from models.coord.polar import CoordPolar


class PageReconRangefinder(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Recon/ReconRangefinder")

    def fill_with_delay(self, selector: str, value, delay: float = 0.8):
        self.page.fill(selector, str(value))
        time.sleep(delay)

    def fill_inputdata_all(self, observe_post: CoordRect, measure: CoordPolar):
        """
        Расчет дальномера/РЛС
        :param observe_post: Координаты КНП (CoordRect)
        :param measure: Измерения (CoordPolar)
        """
        # Ждем появления элементов перед заполнением
        self.page.wait_for_selector('#observePost-x', state='visible')
        self.page.wait_for_selector('#observePost-y', state='visible')
        self.page.wait_for_selector('#observePost-h', state='visible')

        # Заполняем поля с автоматической задержкой
        self.fill_with_delay('#observePost-x', int(observe_post.x))
        self.fill_with_delay('#observePost-y', int(observe_post.y))
        self.fill_with_delay('#observePost-h', int(observe_post.h))
        self.fill_with_delay('#topoData-directionAngle', int(measure.alpha))
        self.fill_with_delay('#topoData-distance', int(measure.distance))
        self.fill_with_delay('#topoData-elevationAngle', int(measure.epsilon))

        self.page.locator("#calculate-button").click()

    def get_observe_post(self) -> CoordRect:
        """Получить координаты КНП"""
        return CoordRect(
            self.parse_number(self.page.locator("#observePost-x").text_content()),
            self.parse_number(self.page.locator("#observePost-y").text_content()),
            self.parse_number(self.page.locator("#observePost-h").text_content())
        )

    def get_measure(self) -> CoordPolar:
        """Получить данные измерений"""
        return CoordPolar(
            self.parse_number(self.page.locator("#topoData-directionAngle").text_content()),
            self.parse_number(self.page.locator("#topoData-distance").text_content()),
            self.parse_number(self.page.locator("#topoData-elevationAngle").text_content())
        )

    def get_result(self) -> CoordRect:
        x = self.parse_number(self.page.locator("#target-x").text_content())
        y = self.parse_number(self.page.locator("#target-y").text_content())
        h = self.parse_number(self.page.locator("#target-h").text_content())
        return CoordRect(x, y, h)
