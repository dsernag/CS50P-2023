from twttr import shorten

def test_shorten_upper_lower():
    assert shorten("VACA") == "VC"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("RATATACK") == "RTTCK"
    assert shorten("vaca") == "vc"
    assert shorten("twitter") == "twttr"
    assert shorten("ratatack") == "rttck"

def test_numbers():
    assert shorten("1234") == "1234"

def test_shorten_special():
    assert shorten("!?.,.") == "!?.,."