from um import count

def test_count_upperlower():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um.") == 2

def test_count_wordwithum():
    assert count("Yummy!") == 0
    assert count("Watch out with your mummy!") == 0

def test_count_specialchars():
    assert count("Hello um  world ") == 1
    assert count("um?") == 1