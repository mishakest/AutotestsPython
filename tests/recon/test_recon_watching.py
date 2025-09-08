from pages.recon.reconWatching import ReconWatchingPage
import pytest
@pytest.mark.regression
@pytest.mark.section_recon
def test_recon_watching(page):
    """Поле ввода данных и кнопки расчета в СН"""
    recon_watching_page = ReconWatchingPage(page)
    recon_watching_page.fill_watching_data(
        x_l="1234567",
        y_l="12345678",
        h_l="25",
        left_direction_angle= "15",
        left_elevation_angle="1500",
        x_r="1234567",
        y_r="12345678",
        h_r="25",
        right_direction_angle= "2500",
        right_elevation_angle= "1000",
    )