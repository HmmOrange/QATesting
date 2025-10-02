import pytest
from code1 import bmi

bva_test_cases = [
    (-50.50, -1.50, "LOI"),
    (70.00, -2.00, "LOI"),
    (50.00, 1.70, "THIEU CAN"),
    (60.00, 1.60, "BINH THUONG"),
    (70.00, 1.55, "THUA CAN"),
    (80.00, 1.60, "BEO PHI"),
]

strong_bva_test_cases = [
    (100.00, 0.00, "LOI"),
    (100.00, 4.01, "LOI"),
    (0.00, 2.00, "LOI"),
    (200.01, 2.00, "LOI")
]

@pytest.mark.parametrize("weight,height,expected", bva_test_cases)
def test_table(weight, height, expected):
    assert bmi(weight, height) == expected





