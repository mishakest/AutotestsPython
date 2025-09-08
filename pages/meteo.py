from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage
class MeteoPage(BasePage): # Класс для заполнения метео
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f'{BASE_URL}/Meteo/MeteoInfo/')

    def fill_meteo_data(self, height, temperature, pressure, wind_direction, wind_speed):
        """
        Заполнение данных по метео
        :param height: Высота метеопоста
        :param temperature: Температура
        :param pressure: Давление
        :param wind_direction: Направление ветра
        :param wind_speed: Скорость ветра
        """
        self.page.get_by_text("Загрузить").click()
        self.page.locator("#load-from-network-modal-frame-iframe").content_frame.get_by_text("Загрузить").click()
        self.page.locator("#load-from-network-modal-frame-iframe").content_frame.get_by_text("Использовать").click()

        self.fill_input('#meteo-inputData-height', height)
        self.fill_input('#meteo-inputData-temperature', temperature)
        self.fill_input('#meteo-inputData-pressure', pressure)
        self.fill_input('#meteo-inputData-windDirection', wind_direction)
        self.fill_input('#meteo-inputData-windSpeed', wind_speed)
        self.page.locator("#calculate-button").click()
        self.page.locator("#apply-result-button").click()

