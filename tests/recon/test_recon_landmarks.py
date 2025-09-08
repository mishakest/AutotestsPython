import pytest
from pages.recon.reconLandmarks import ReconLandmarksPage
@pytest.mark.regression
@pytest.mark.section_recon
def test_recon_landmarks(page):
    """Поле ввода данных и кнопки сохранить в создании ориентира """
    recon_landmarks_page = ReconLandmarksPage(page)
    recon_landmarks_page.fill_landmarks_data(
        x="1234567",
        y="12345678",
        h="25"
    )