class CoordPolar:
    alpha: int = 0
    distance: int = 0
    epsilon: int = 0

    def __init__(self, alpha, distance, epsilon=None):
        self.alpha = alpha
        self.distance = distance
        self.epsilon = epsilon

    def __repr__(self) -> str:
        return f"CoordPolar({self.alpha}, {self.distance}, {self.epsilon})"

    def __eq__(self, second):
        return self.alpha == second.alpha and self.distance == second.distance and self.epsilon == second.epsilon

    @property
    def alpha_str(self) -> str:
        return str(self.alpha)

    @property
    def distance_str(self) -> str:
        return str(self.distance)

    @property
    def epsilon_str(self) -> str:
        return str(self.epsilon)
