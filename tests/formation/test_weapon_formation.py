from pages.formation.weaponFormation import WeaponFormationFiringPositionPage
import pytest
@pytest.mark.regression
@pytest.mark.section_formation
def test_weapon_formation_firing_position(page):
    """Поле ввода данных и кнопки сохранения в создании огневой позиции"""
    firing_position_page = WeaponFormationFiringPositionPage(page)
    firing_position_page.fill_firing_position_data(
        weapon_type="Д-20",
        x="5653712",
        y="05654637",
        h="30",
        direction="125",
        temperature="-12",
        delta_v0="-2",
        main_angle="1111",
        reserve_angle="1222",
        night_angle="83-56"
    )