from pages.topo.inverseGeoTask import  InverseGeoTaskPage
import pytest


@pytest.mark.regression
@pytest.mark.section_topo
def test_inverse_geo_task(page):
    """Поле ввода данных и кнопки рассчитать в ОГЗ"""
    inverse_geo_task_page = InverseGeoTaskPage(page)
    inverse_geo_task_page.fill_inverse_geo_task_data(
        x_target="1234567",
        y_target="12345678",
        h_target="25",
        x_1="5634567",
        y_1="01064657",
        h_1="25",
        x_2="5634567",
        y_2="01064657",
        h_2="25",
        x_3="5634567",
        y_3="01064657",
        h_3="25",
    )