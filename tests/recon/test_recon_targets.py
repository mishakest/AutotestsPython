import pytest
from pages.recon.reconTargets import ReconTargetsPage

@pytest.mark.regression
@pytest.mark.section_recon
def test_recon_targets(page):
    """Поле ввода данных и кнопки сохранить в создании цели"""
    recon_targets_page = ReconTargetsPage(page)
    recon_targets_page.fill_targets_data(
        x="1234567",
        y="12345678",
        h="25",
        front="25",
        depth="25"
    )