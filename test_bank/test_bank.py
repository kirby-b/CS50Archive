from bank import value

def test_value():
    assert value("hello") == "$0"
    assert value("Hello") == "$0"
    assert value("Hi") == "$20"
    assert value("Hey") == "$20"
    assert value("What is up") == "$100"