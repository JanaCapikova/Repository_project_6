

# Test 1: Verify that Inspiration page contains News topic
def test_inspiration_page_contains_news_topic(page, home_page_rohlik, accept_cookies):
    # Arrange
    expected_topic = "Novinky"

    page.goto(home_page_rohlik)
    accept_cookies(page)

    inspiration_link = page.get_by_text("Inspirace").first

    # Act
    inspiration_link.click()

    # Assert
    page.wait_for_selector(f"text={expected_topic}")
    assert expected_topic in page.inner_text("body")


# Test 2: Verify that login button opens login form
def test_login_button_opens_login_form(page, home_page_rohlik, accept_cookies):
    # Arrange
    page.goto(home_page_rohlik)
    accept_cookies(page)

    login_button = page.get_by_text("Přihlásit").first

    # Act
    login_button.click()

    # Assert
    page.wait_for_selector("text=E-mail")
    assert "E-mail" in page.content()
    assert "Heslo" in page.content()
  

# Test 3: Verify that the contact page contains the company address
def test_contact_page_contains_company_address(page, home_page_rohlik, accept_cookies):
    
    # Arrange
    expected_address = "Karolinská 654/2, Karlín, 186 00 Praha 8"

    page.goto(home_page_rohlik)
    accept_cookies(page)
    
    contact_link = page.locator('a[href="/cs-CZ/stranka/kontakt"]')

    # Act
    contact_link.click()
    
    # Assert
    page.wait_for_selector(f"text={expected_address}")
    assert expected_address in page.content()



