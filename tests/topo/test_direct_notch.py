import pytest
from pages.topo.directNotch import  DirectNotchPage
@pytest.mark.regression
@pytest.mark.section_topo
def test_direct_notch(page):
    """Поле ввода данных и кнопки рассчитать в прямой засечки"""
    direct_notch_page = DirectNotchPage(page)
    direct_notch_page.fill_direct_notch_data(
        x_obs_post_left="2424000",
        y_obs_post_left="42444440",
        h_obs_post_left="2525",
        left_direction_angle="24",
        left_elevation_angle="424",
        x_obs_post_right="2525000",
        y_obs_post_right="44444240",
        h_obs_post_right="0",
        right_direction_angle="4245",
        right_elevation_angle="5"
    )