from pytest import mark


@mark.body
class BodyTests:

    @mark.ui
    def test_door(self, chrome_browser):
        chrome_browser.get('https://www.google.com')

    def test_windshield(self):
        pass

    def test_trunk(self):
        pass


