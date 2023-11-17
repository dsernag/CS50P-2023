from bank import value

def test_upper_lower_value():
    assert value("Hello Tom") == 0
    assert value("hello Carlitos") == 0
    assert value("HEY dude") == 20
    assert value("WhasaaaAAAa") == 100

def test_numbers_value():
    assert value("1234") == 100

def test_punct_value():
    assert value(".?!,.;") == 100