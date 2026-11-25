from app import check_availability, calculate_fine

def test_check_availability_positive():
    assert check_availability(5) is True

def test_check_availability_zero():
    assert check_availability(0) is False

def test_calculate_fine_positive():
    assert calculate_fine(3) == 15
