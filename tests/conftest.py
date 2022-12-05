import pytest
from selene import have, command
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 2560
    browser.config.window_height = 1440


    # #remove/close all advertisements:
    # ads = browser.all('[id^=google_ads_][id$=container__]')
    # ads.should(have.size_less_than_or_equal(3))
    # ads.perform(command.js.remove)

    yield
    browser.quit()