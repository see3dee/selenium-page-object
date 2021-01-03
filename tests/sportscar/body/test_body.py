from pytest import mark


@mark.body
def test_door():
    assert True


@mark.body
def test_windshield():
    pass


@mark.body
def test_trunk():
    pass


