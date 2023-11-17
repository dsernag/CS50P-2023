from numb3rs import validate

def test_validate_format():
    assert validate("127.0.0.1") == True
    assert validate("127.0.0") == False
    assert validate("127.0") == False
    assert validate("127") == False


def test_validate_size():
    assert validate("255.255.255.255") == True
    assert validate("255.256.255.255") == False
    assert validate("255.200.500.300") == False
