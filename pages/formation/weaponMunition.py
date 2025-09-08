from playwright.sync_api import Page
from tests.conftest import BASE_URL
from pages.base_page import BasePage


class WeaponFormationMunitionPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.page.goto(f"{BASE_URL}/Formation/WeaponMunition")

    def fill_munition_data(self, weapon_type, trajectory, projectile, fuse,
                           charge, amount):
        """
                   Заполнение dropdown по СП
                :param weapon_type: Вид АС
                :param trajectory: Вид стрельбы
                :param projectile: Снаряд
                :param fuse: Взрыватель
                :param charge: Заряд
                :param amount: дельта Vоз
        """
        self.page.locator("#createButton").click()
        last_row = self.page.locator('div[id^="row_"]').last

        # Заполнение выпадающих списков

        dropdown_values = [
            (0, weapon_type),
            (1, trajectory),
            (2, projectile),
            (3, fuse),
            (4, charge)
        ]

        for index, value in dropdown_values:
            self.select_dropdown_option(
                parent_locator=last_row,
                index=index,
                value=value
            )

        # Заполнение поля количества
        last_row.locator('div[v-number="intLen:2;fractLen:2"]').first.fill(amount)

        save_button = self.page.locator("#saveButton")
        button_classes = save_button.get_attribute("class") or ""
        if "disabled" not in button_classes:
            self.page.evaluate('document.querySelector(".footer")')
            save_button.click()
            print("Данные сохранены успешно.")
        else:
            print("Кнопка 'Сохранить' неактивна (серая). Изменений не было, сохранение не требуется.")

        self.page.locator(".refresh-icon").click()
