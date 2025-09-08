from pages.formation.weaponObservePost import WeaponFormationObsPostPage
import pytest
@pytest.mark.regression
@pytest.mark.section_formation
def test_weapon_formation_obs_post(page):
    """Поле ввода данных и кнопки сохранения в создании КНП"""
    obs_post_page = WeaponFormationObsPostPage(page)
    obs_post_page.fill_obs_post_data(
        obs_post_type="КНП АДН",
        x="56555552",
        y="05655555",
        h="56",
    )