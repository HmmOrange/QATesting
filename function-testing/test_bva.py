import pytest
# from code1 import bmi
from code2 import bmi

bva_test_cases = [
    (100.00, 0.01, "BEO PHI"),
    (100.00, 0.02, "BEO PHI"),
    (100.00, 3.99, "THIEU CAN"),
    (100.00, 4.00, "THIEU CAN"),
    (0.01, 1.5, "THIEU CAN"),
    (0.02, 1.5, "THIEU CAN"),
    (199.99, 1.5, "BEO PHI"),
    (200.00, 1.5, "BEO PHI"),
    (100.00, 1.5, "BEO PHI")
]

strong_bva_test_cases = [
    (100.00, 0.00, "LOI"),
    (100.00, 4.01, "LOI"),
    (0.00, 2.00, "LOI"),
    (200.01, 2.00, "LOI")
]

@pytest.mark.parametrize("weight,height,expected", bva_test_cases)
def test_bva(weight, height, expected):
    assert bmi(weight, height) == expected


@pytest.mark.parametrize("weight,height,expected", strong_bva_test_cases)
def test_strong_bva(weight, height, expected):
    assert bmi(weight, height) == expected




