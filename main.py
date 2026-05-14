import pytest

#Test 1: Accept cookies
def test_accept_rohlik_cookies(page):
    home_page_rohlik = "https://www.rohlik.cz"
    button_accept_cookies = "#accept"

    page.goto(home_page_rohlik)
    accept_button = page.locator(button_accept_cookies)
    accept_button.click()


#Test 2: Verify that the search field is empty
def test_search_field_is_empty(page):
    home_page_rohlik = "https://www.rohlik.cz"
    search_field_selector = "#searchGlobal"

    page.goto(home_page_rohlik)
    search_field = page.locator(search_field_selector).first
    assert search_field.input_value() == ""


#Test 3: Verify that the contact page contains the company address
def test_contact_page_contains_company_address(page):
    home_page_rohlik = "https://www.rohlik.cz"
    contact_link = page.locator('a[href="/stranka/kontakt"]')
    expected_address = "Karolinská 654/2, Karlín, 186 00 Praha 8"

    page.goto(home_page_rohlik)

    accept_button = page.locator("#accept")
    accept_button.click()

    contact_link.click()
    page.wait_for_timeout(3000)
    assert expected_address in page.content()

