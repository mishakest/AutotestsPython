from pages.meteo import  MeteoPage
import pytest
@pytest.mark.regression
@pytest.mark.section_meteo
def test_meteo(page):
    """Поле ввода данных и кнопки рассчитать в ПГЗ"""
    meteo_page = MeteoPage(page)
    meteo_page.fill_meteo_data(
        height="86",
        temperature="-15",
        pressure="747",
        wind_direction="30",
        wind_speed="5"
    )