import pytest

from models.coord.polar import CoordPolar
from pages.recon.reconAiming import ReconAimingPage
from models.coord.rect import CoordRect
from models.error_messages import (
    TARGET_MISMATCH,
    POST_MISMATCH,
    RESULT_MISMATCH
)

test_cases = [
    (
        CoordRect(6588525, 5661034, 36),  # Observe Post
        CoordRect(6592633, 5658100, 20),  # Target
        CoordPolar(5408, 5048, -3)  # Reference Data (measure)
    )
]



@pytest.mark.regression
@pytest.mark.section_recon
@pytest.mark.parametrize("observe_post, target,, reference_data", test_cases)
def test_recon_aiming(page, observe_post, target, reference_data):
    """Тестируется:
          1. Поле ввода данных цели
          2. Поле ввода данных КНП
          3. Расчёт
      """
    recon_aiming_page = ReconAimingPage(page)

    recon_aiming_page.fill_inputdata_all(target, observe_post)

    # Получаем введенные данны
    input_target = recon_aiming_page.get_target()
    input_post = recon_aiming_page.get_observe_post()

    assert input_target == target, TARGET_MISMATCH.format(
        expected=target,
        actual=input_target
    )

    assert input_post == observe_post, POST_MISMATCH.format(
        expected=observe_post,
        actual=input_post
    )

    # Проверяем результат расчета
    result = recon_aiming_page.get_result()

    assert result == reference_data, RESULT_MISMATCH.format(
        expected=reference_data,
        actual=result
    )
