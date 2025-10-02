import pytest
from code1 import bmi

test_cases = [
    (50, 1.7, "THIEU CAN"),
    (65, 1.7, "BÌNH THƯỜNG"),
    (80, 1.7, "THUA CAN"),
    (95, 1.7, "BEO PHI"),
    (120, 1.7, "BEO PHI NANG"),
    (201, 5, "LOI"),
    (0, 0, "LOI"),
    (200, 0, "LOI")
]

@pytest.mark.parametrize("weight,height,expected", test_cases)
def test_bmi(weight, height, expected):
    assert bmi(weight, height) == expected


