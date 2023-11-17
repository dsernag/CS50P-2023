from plates import is_valid

# 1) Between 6 and 2 characters
def test_lenght_is_valid():
    assert is_valid("AA123456789") == False

# 2) No puctuation or spaces
def test_punct_is_valid():
    assert is_valid("CS50.") == False

# 3) Start with 2 letters
def test_start_is_valid():
    assert is_valid("12AAEE") == False

# 4) Numbers cannot be used in the middle of a plate; they must come at the end
def test_numbers_is_valid():
    assert is_valid("CS525C") == False

# 5) Numbers cannot start by 0
def test_number_zero_is_valid():
    assert is_valid("CS050") == False

# 6) Plates 2 chars
def test_twochars_is_valid():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("12") == False