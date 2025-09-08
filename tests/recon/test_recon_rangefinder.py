import pytest
from pages.recon.reconRangefinder import PageReconRangefinder
from models.coord.rect import CoordRect
from models.coord.polar import CoordPolar
from models.recon_input_data import ReconInputData
from models.error_messages import (
    POST_MISMATCH,
    RESULT_MISMATCH,
    MEASURE_MISMATCH
)

test_cases = [
    (ReconInputData(
        CoordRect(6519263, 5658100, 20),
        CoordPolar(4478, 2531, 3),
        CoordRect(0, 0, 28)
    ),
     CoordRect(6519205, 5655570, 28))
]


@pytest.mark.regression
@pytest.mark.section_recon
@pytest.mark.psi
@pytest.mark.no_profile
@pytest.mark.parametrize("test_data, reference_data", test_cases)
def test_recon_rangefinder(page, test_data, reference_data):
    """Тестируется:
        1. Поле ввода данных КНП
        2. Поле ввода данных измерений
        3. Расчёт
    """
    recon_rangefinder_page = PageReconRangefinder(page)
    # Ввод данных и проверка их корректности
    recon_rangefinder_page.fill_inputdata_all(test_data.observe_post, test_data.measure)

    # Получение и проверка введенных данных
    input_post = recon_rangefinder_page.get_observe_post()
    assert input_post == test_data.observe_post, POST_MISMATCH.format(
        expected=test_data.observe_post,
        actual=input_post
    )
    input_measure = recon_rangefinder_page.get_measure()
    assert input_measure == test_data.measure, MEASURE_MISMATCH.format(
        expected=test_data.measure,
        actual=input_measure
    )

    # Проверка результата расчета
    result = recon_rangefinder_page.get_result()
    assert result == reference_data, RESULT_MISMATCH.format(
        expected=reference_data,
        actual=result
    )
