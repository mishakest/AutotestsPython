from pages.formation.weaponMunition import  WeaponFormationMunitionPage
import pytest
@pytest.mark.regression
@pytest.mark.section_formation
def test_weapon_formation_munition(page):
    """Поле ввода данных и кнопки сохранения в создании средства поражения"""
    monition_page = WeaponFormationMunitionPage(page)
    monition_page.fill_munition_data(
        weapon_type="2А65",
        trajectory="Настильная",
        projectile="ОФ-25",
        fuse="В-90",
        charge="2",
        amount="1"
    )