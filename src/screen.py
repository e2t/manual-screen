from math import ceil
from dry.base_gui import assert_positive


class GridProfile:
    def __init__(self, length: float) -> None:
        self._profile_width: float
        self._length = length

    def number(self, width: float, gap: float) -> int:
        result = ceil((width - gap) / (self._profile_width + gap))
        assert_positive(result, 'Количество профилей')
        return result

    def mass(self) -> float:
        pass


class GridProfile3999(GridProfile):
    def __init__(self, length: float) -> None:
        super().__init__(length)
        self._profile_width = 9.5

    def mass(self) -> float:
        result = 0.001 * self._length - 0.001
        assert_positive(result, 'Масса профиля')
        return result


class Screen:
    def __init__(self, external_width: float, length: float,
                 gap: float) -> None:
        self._number: int
        self._mass = self._mass_calc(external_width, length, gap)

    @property
    def mass(self) -> float:
        return self._mass

    @property
    def number(self) -> int:
        return self._number

    def _mass_grid_canvas(self, width: float, length: float,
                          gap: float) -> float:
        profile = GridProfile3999(length)
        self._number = profile.number(width, gap)
        return profile.mass() * self._number

    def _mass_calc(self, external_width: float, length: float,
                   gap: float) -> float:
        internal_width = external_width - 15
        return sum([Screen._mass_bottom_balk(external_width),
                    Screen._mass_intermediate_raker(external_width),
                    Screen._mass_top_slide(internal_width),
                    Screen._mass_top_prop(external_width + 200),
                    self._mass_grid_canvas(internal_width, length - 356, gap),
                    Screen._mass_other()])

    @staticmethod
    def _mass_bottom_balk(length: float) -> float:
        result = 0.003 * length - 0.006
        assert_positive(result, 'Масса нижней балки')
        return result

    @staticmethod
    def _mass_intermediate_raker(length: float) -> float:
        result = 0.001 * length - 0.022
        assert_positive(result, 'Масса перемычки')
        return result

    @staticmethod
    def _mass_top_slide(width: float, length: float=340) -> float:
        result = 3.258e-5 * length * width + 0.00179 * length + 0.00411 * width
        assert_positive(result, 'Масса склиза')
        return result

    @staticmethod
    def _mass_top_prop(length: float) -> float:
        result = 0.004 * length - 0.01
        assert_positive(result, 'Масса опоры')
        return result

    @staticmethod
    def _mass_other() -> float:
        return 1.7
