from pytest import mark


@mark.ui
@mark.entertainment
def test_radio(chrome_browser):
    chrome_browser.get('https://www.google.com')


@mark.entertainment
def test_bluetooth():
    pass


@mark.entertainment
def test_dvd():
    pass



