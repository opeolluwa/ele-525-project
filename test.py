import pytest

# import the functions to be tested
from main import convert, rectangular_to_cylindrical, rectangular_to_spherical, cylindrical_to_rectangular, cylindrical_to_spherical, spherical_to_rectangular, spherical_to_cylindrical


# test the rectangular to cylindrical function
def test_rectangular_to_cylindrical():
    assert 1 == 1