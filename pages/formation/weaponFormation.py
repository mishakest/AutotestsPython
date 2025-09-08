from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage

class WeaponFormationFiringPositionPage(BasePage):  # Класс по созданию ОП
    def __init__(self, page: Page):
        super().__init__(page)
        self.page.goto(f"{BASE_URL}/Formation/WeaponFormation")

    def fill_firing_position_data(self, weapon_type, x, y, h, direction,
                                  temperature, delta_v0, main_angle, reserve_angle, night_angle):
        """
        Заполнение полей по созданию ОП
        :param weapon_type: Выбор системы
        :param x: Координата X
        :param y: Координата Y
        :param h: Высота ОП
        :param direction: основное направление
        :param temperature: Температура заряда
        :param delta_v0: Дельта V0 орудия
        :param main_angle: Точки наводки - основная
        :param reserve_angle: Точки наводки - запасная
        :param night_angle: Точки наводки - ночная
        """
        def fill_input(selector, value):
            input_element = self.page.locator(selector)
            input_element.fill(value)

        weapon_dropdown = self.page.locator("#select2-weapon-system-container")
        weapon_dropdown.click()
        self.page.wait_for_selector("ul.select2-results__options")
        self.page.locator(f"li.select2-results__option:has-text('{weapon_type}')").click()
        self.page.wait_for_selector(f"#select2-weapon-system-container:has-text('{weapon_type}')")
        self.fill_input("#weapon-x", x)
        self.fill_input("#weapon-y", y)
        self.fill_input("#weapon-h", h)
        self.fill_input("#weapon-direction", direction)
        self.fill_input("#ballisticsTemperature", temperature)
        self.fill_input("#deltaV0", delta_v0)
        self.fill_input("#mainAimingPointAngle", main_angle)
        self.fill_input("#reserveAimingPointAngle", reserve_angle)
        self.fill_input("#nightAimingPointAngle", night_angle)

        save_button = self.page.locator("#saveButton")
        button_classes = save_button.get_attribute("class") or ""
        if "disabled" not in button_classes:
            self.page.evaluate('document.querySelector(".footer")')
            save_button.click()
            print("Данные сохранены успешно.")
        else:
            print("Кнопка 'Сохранить' неактивна (серая). Изменений не было, сохранение не требуется.")

        self.page.locator('.refresh-icon').click()
