from pages.topo.inverseNotchTwoAngles import InverseNotchTwoAnglesPage
import pytest
@pytest.mark.regression
@pytest.mark.section_topo
def test_inverse_notch_two_angles(page):
    """Поле ввода данных и кнопки рассчитать в обратной по углам засечки"""
    inverse_notch_two_angles = InverseNotchTwoAnglesPage(page)
    inverse_notch_two_angles.fill_inverse_notch_two_angles_data(
        x_3="6537260",
        y_3="05654159",
        x_2="05654159",
        y_2="05659857",
        x_1="6538888",
        y_1="05664844",
        alpha_angle="240",
        betta_angle="24",
    )