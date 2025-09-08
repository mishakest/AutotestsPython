from screeninfo import get_monitors
from functional import seq

def get_main_display_resolution():
    """
    Метод, возвращающий разрешение главного монитора
    :return: List: {"width": mainDisplay.width, "height": mainDisplay.height}
    """
    displays = get_monitors()
    # Немного не привычная логика, но тут внесу ясности
    # displays - это list мониторов, то есть класса Monitor
    # seq - оборачивает этот лист, в поток, который библиотека может фильтровать
    # далее мы делаем выборку, то есть .filter(lambda m: m.is_primary) то же самое, что и
    # выбери из всего листа Мониторов тот, у кого is_primary == True
    # ну и first, первое вхождение (здесь без разницы, он у нас всегда один будет)
    mainDisplay = (seq(displays)
                   .filter(lambda m: m.is_primary)
                   .first())
    result = {"width": mainDisplay.width, "height": mainDisplay.height}
    return result