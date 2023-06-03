import pytest
from selenium import webdriver
import json
import os

# Get the directory of this script
dir_path = os.path.dirname(os.path.abspath(__file__))

# Build the file path for config.json
config_path = os.path.join(dir_path, 'config.json')

url = 'https://the-internet.herokuapp.com'

@pytest.fixture
def get_config():
    with open(config_path) as config_file:
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
    