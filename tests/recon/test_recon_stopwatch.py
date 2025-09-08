import pytest

from models.coord.polar import CoordPolar
from pages.recon.reconStopwatch import ReconStopwatchPage
from models.coord.rect import CoordRect
from models.error_messages import (
    TARGET_MISMATCH,
    POST_MISMATCH,
    RESULT_MISMATCH
)

test_cases = [
    (
        CoordRect(6588525, 5661034, 36),  # Observe Post
        CoordPolar(5408, None, -3),  # Reference Data (measure)
        5.0,  # Time
        330.0,  # Sonic Speed
        CoordRect(6589868, 5660075, 31)  # Target
    )
]


@pytest.mark.regression
@pytest.mark.section_recon
@pytest.mark.parametrize("observe_post, measure_polar, time, sonic_speed, target", test_cases)
def test_recon_stopwatch(page, observe_post, measure_polar, time, sonic_speed, target):
    """Тестируется:
          1. Поле ввода данных КНП
          2. Поле ввода данных измерений
          3. Расчёт
      """
    recon_stopwatch_page = ReconStopwatchPage(page)

    recon_stopwatch_page.fill_inputdata_all(observe_post, measure_polar, time, sonic_speed)

    # Получаем введенные данные
    input_post = recon_stopwatch_page.get_observe_post()
    input_measure = recon_stopwatch_page.get_measure()

    assert input_post == observe_post, POST_MISMATCH.format(
        expected=observe_post,
        actual=input_post
    )

    assert input_measure == measure_polar, TARGET_MISMATCH.format(
        expected=measure_polar,
        actual=input_measure
    )

    # Проверяем результат расчета
    result = recon_stopwatch_page.get_result()

    assert result == target, RESULT_MISMATCH.format(
        expected=target,
        actual=result

    )
