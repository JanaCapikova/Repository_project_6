import pytest

@pytest.fixture
def home_page_rohlik():
    return "https://www.rohlik.cz"

@pytest.fixture
def accept_cookies():
    def _accept_cookies(page):
        accept_button = page.locator("#accept")

        if accept_button.is_visible():
            accept_button.click()

    return _accept_cookies