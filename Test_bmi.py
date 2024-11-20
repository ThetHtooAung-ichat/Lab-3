import Lab_2.bmi as bmi


def test_bmi_normal_weight():
    expected = 0
    result = bmi.calculate_bmi(weight=65.0,height=1.80)
    assert(result == expected)

def test_bmi_under_weight():
    expected = -1
    result = bmi.calculate_bmi(weight=35.0,height=1.80)
    assert(result == expected)

def test_bmi_over_weight():
    expected = 1
    result = bmi.calculate_bmi(weight=95.0,height=1.80)
    assert(result == expected)