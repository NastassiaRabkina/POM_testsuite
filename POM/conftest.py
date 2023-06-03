import pytest
from selenium import webdriver
import json

url = 'https://the-internet.herokuapp.com'

@pytest.fixture
def get_config():
    with open('config.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture
def driver(get_config):
    browser = get_config['browser']
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
    