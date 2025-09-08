import pytest
from pages.topo.directGeoTask import DirectGeoTaskPage
@pytest.mark.regression
@pytest.mark.section_topo
def test_direct_geo_task(page):
    """Поле ввода данных и кнопки рассчитать в ПГЗ"""
    direct_geo_task_page = DirectGeoTaskPage(page)
    direct_geo_task_page.fill_direct_geo_task_data(
        x_0="21 45756",
        y_0="152 23484",
        h_0="85",
        distance="25",
        elevation_angle="2",
        amount="1",
        distance_two= "12",
        elevation_angle_two = "25",
        amount_two = "2"
    )