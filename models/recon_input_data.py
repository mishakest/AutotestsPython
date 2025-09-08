from models.coord.polar import CoordPolar
from models.coord.rect import CoordRect


class ReconInputData:
    observe_post: CoordRect = None
    measure: CoordPolar = None
    target: CoordRect = None

    def __init__(self, observe_post, measure, target):
        self.observe_post = observe_post
        self.measure = measure
        self.target = target

    def __repr__(self) -> str:
        """
        Текстовое представление модели
        Так-же выводится в отчёт Allure
        """
        return (f"ReconInputData({self.observe_post}, "
                f"{self.measure})"
                f"{self.target}")

    def __eq__(self, second):
        return (self.observe_post == second.observe_post and
                self.measure == second.measure and
                self.target == second.target)
