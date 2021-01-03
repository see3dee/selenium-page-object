from pytest import mark

@mark.smoke
@mark.engine
def test_coils():
    assert True

@mark.smoke
@mark.engine
def test_compression():
    pass

@mark.smoke
@mark.engine
def test_timing():
    pass
