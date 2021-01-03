from pytest import mark

@mark.smoke
@mark.entertainment
def test_radio():
    assert True


@mark.entertainment
def test_bluetooth():
    pass


@mark.entertainment
def test_dvd():
    pass



