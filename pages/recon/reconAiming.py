from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage
from models.coord.rect import CoordRect
from models.coord.polar import CoordPolar


class ReconAimingPage(BasePage):  # Класс расчета целеуказания в разведке
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Recon/ReconAiming")

    def fill_inputdata_all(self, target: CoordRect, observe_post: CoordRect):
        """
        Заполняет данные в поля для расчета целеуказания в разведке и выполняет расчет
        :param target: Координаты по цели (CoordRect)
        :param observe_post: Координаты КНП (CoordRect)
        """

        self.page.fill('#target-x', str(int(target.x)))
        self.page.fill('#target-y', str(int(target.y)))
        self.page.fill('#target-h', str(int(target.h)))
        self.page.fill('#observePost-x', str(int(observe_post.x)))
        self.page.fill('#observePost-y', str(int(observe_post.y)))
        self.page.fill('#observePost-h', str(int(observe_post.h)))

        calculate_button = self.page.locator("#calculate-button")
        calculate_button.click()

    def get_target(self) -> CoordRect:
        """Получить координаты цели"""
        return CoordRect(
            int(self.page.locator("#target-x").text_content()),
            int(self.page.locator("#target-y").text_content()),
            int(self.page.locator("#target-h").text_content())
        )

    def get_observe_post(self) -> CoordRect:
        """Получить координаты КНП"""
        return CoordRect(
            int(self.page.locator("#observePost-x").text_content()),
            int(self.page.locator("#observePost-y").text_content()),
            int(self.page.locator("#observePost-h").text_content())
        )

    def get_result(self) -> CoordPolar:
        """Выполнить расчет"""
        alpha = int((self.page.locator("#topoData-directionAngle").text_content() or "").replace('-', '') or 0)
        distance = int(self.page.locator("#topoData-distance").text_content() or 0)
        epsilon = int(self.page.locator("#topoData-elevationAngle").text_content() or 0)

        return CoordPolar(alpha, distance, epsilon)
