from twttr import shorten

def test_shorten():
    assert shorten("Bobby") == "Bbby"
    assert shorten("Twitter") == "Twttr"
    assert shorten("Reddit") == "Rddt"
    assert shorten("Python") == "Pythn"
    assert shorten("Django") == "Djng"