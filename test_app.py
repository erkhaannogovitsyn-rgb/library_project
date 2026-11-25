from app import check_availability

def test_check_availability_positive():
    assert check_availability(5) is True

def test_check_availability_zero():
    assert check_availability(0) is False

def test_check_availability_negative():
    assert check_availability(-1) is False