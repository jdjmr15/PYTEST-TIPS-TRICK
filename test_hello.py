from hello import more_hello, more_goodbye


def test_more_hello():
    assert "hi" == more_hello()


def test_more_hello_not_empt():
    assert more_hello() != ""


def test_more_goodbye():
    assert "bye" == more_goodbye()


def test_more_goodbye_not_empty():
    assert more_goodbye() != ""


def test_more_hello_is_string():
    assert isinstance(more_hello(), str)


def test_more_goodbye_is_string():
    assert isinstance(more_goodbye(), str)
