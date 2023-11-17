from seasons import check_birthday

def test_number_to_words():
    assert check_birthday("1998-06-25") == ["1998", "06", "25"]
    assert check_birthday("1989-12-3") == None
    assert check_birthday("January 1st, 1995") == None
