import pytest
from pages.recon.reconFrontiers import ReconFrontiersPage
@pytest.mark.regression
@pytest.mark.section_recon
def test_recon_frontiers(page):
    """Поле ввода данных и кнопки сохранить в создании рубежа ЗО"""
    recon_frontiers_page = ReconFrontiersPage(page)
    recon_frontiers_page.fill_frontiers_data(
        x_l="1234567",
        y_l="12345678",
        h_l="25",
        x_r="9876543",
        y_r="98765432",
        h_r="50"
    )