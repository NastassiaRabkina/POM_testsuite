import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from util.listener import Listener
import json
import os
import argparse
import logging

def pytest_addoption(parser):
    parser.addoption(
        "--environment", action="store", choices=['test'], help="Environment to run tests against"
    )

@pytest.fixture
def get_config(request):
    environment = request.config.getoption("--environment")
    if environment == 'test':
        config_path = os.path.join('/Users/nastassiarabkina/Desktop/py_course/POM/properties', 'test.properties.json')
    else:
        raise ValueError(f"Configuration file doesn't exist in properties folder")
    with open(config_path) as config_file:
        data = json.load(config_file)
    return data


def pytest_sessionstart(session):
    global log_file_path
    log_file_path = os.path.join('/Users/nastassiarabkina/Desktop/py_course/POM/output', 'test.log')
    with open(log_file_path, 'w') as _:
        pass


def pytest_runtest_protocol(item, nextitem):
    logger = logging.getLogger()
    filehandler = logging.FileHandler(log_file_path)
    filehandler.setLevel(logging.WARNING)
    logger.addHandler(filehandler)
    return None


def pytest_exception_interact(node, call, report):
    if isinstance(call.excinfo.value, AssertionError):
        listener = Listener()
        driver = node.funcargs.get('driver')
        if driver is not None:
            listener.on_exception(AssertionError, driver)


@pytest.fixture
def driver(get_config):
    browser = get_config['browser']
    url = get_config['url']
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    edriver = EventFiringWebDriver(driver, Listener())
    edriver.maximize_window()
    edriver.get(url)
    yield edriver
    edriver.quit()


@pytest.fixture
def username(get_config):
    username = get_config.get('username')
    if not username:
        raise ValueError("Username is empty")
    return username


@pytest.fixture
def password(get_config):
    password = get_config.get('password')
    if not password:
        raise ValueError("Password is empty")
    return password
    