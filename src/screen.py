from math import ceil
from typing import Union, NamedTuple
from dry.core import Error


# Ширина профиля 3999
PROFILE_WIDTH = 9.5


class LogicError(Error):
    pass


class Screen(NamedTuple):
    number: int
    mass: float


def assert_positive(value: Union[int, float], name: str) -> None:
    if value <= 0:
        raise LogicError(
            f'Ошибка!\n{name} - значение отрицательно или равно нулю')


def calc_number_profiles(width: float, gap: float) -> int:
    result = ceil((width - gap) / (PROFILE_WIDTH + gap))
    assert_positive(result, 'Количество профилей')
    return result


def calc_mass_profile(length: float) -> float:
    result = 0.001 * length - 0.001
    assert_positive(result, 'Масса профиля')
    return result


def calc_mass_grid_canvas(length: float, number_profiles: int) -> float:
    mass_profile = calc_mass_profile(length)
    return mass_profile * number_profiles


def calc_mass_bottom_balk(length: float) -> float:
    result = 0.003 * length - 0.006
    assert_positive(result, 'Масса нижней балки')
    return result


def calc_mass_intermediate_raker(length: float) -> float:
    result = 0.001 * length - 0.022
    assert_positive(result, 'Масса перемычки')
    return result


def calc_mass_top_slide(width: float, length: float=340) -> float:
    result = 3.258e-5 * length * width + 0.00179 * length + 0.00411 * width
    assert_positive(result, 'Масса склиза')
    return result


def calc_mass_top_prop(length: float) -> float:
    result = 0.004 * length - 0.01
    assert_positive(result, 'Масса опоры')
    return result


def calc_mass_other() -> float:
    return 1.7


def calc_mass_screen(external_width: float, length: float,
                     internal_width: float,
                     number_profiles: int) -> float:
    return sum((calc_mass_bottom_balk(external_width),
                calc_mass_intermediate_raker(external_width),
                calc_mass_top_slide(internal_width),
                calc_mass_top_prop(external_width + 200),
                calc_mass_grid_canvas(length - 356, number_profiles),
                calc_mass_other()))


def calc_screen(external_width: float, length: float,
                gap: float) -> Screen:
    internal_width = external_width - 15
    number_profiles = calc_number_profiles(internal_width, gap)
    mass_screen = calc_mass_screen(external_width, length, internal_width,
                                   number_profiles)
    return Screen(
        number=number_profiles,
        mass=mass_screen)
