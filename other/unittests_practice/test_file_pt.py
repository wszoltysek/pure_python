import pytest
from other.unittests_practice.file import Car, IllegalCarError


@pytest.mark.parametrize("car, result", (
        (Car(2, 900, 5).total_mass, 1040),
        (Car(5, 1200, 5).total_mass, 1550),
        (Car(4, 1400, 6).total_mass, 1680)
))
def test_car_total_mass(car, result):
    assert car == result


def test_pax_count_only_errors():
    with pytest.raises(IllegalCarError):
        assert Car(6, 1500, 6).pax_count()      # To many passengers
        assert Car(0, 1999, 5).pax_count()      # No passengers
        assert Car(5, 2100, 6).car_mass()       # Car is to heavy
        assert Car(6, 2200, 6).car_mass()       # To many passengers, Car is to heavy


def test_car_mass_to_heavy():
    with pytest.raises(IllegalCarError) as e:
        Car(5, 2100, 6).car_mass()
    assert str(e.value) == "Car is to heavy"


def test_pax_count_empty():
    with pytest.raises(IllegalCarError) as e:
        Car(0, 40, 5).pax_count()
    assert str(e.value) == "No passengers"


def test_pax_count_to_many():
    with pytest.raises(IllegalCarError) as e:
        Car(6, 1500, 6).pax_count()
    assert str(e.value) == "To many passengers"
