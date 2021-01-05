from appium import webdriver
import pytest

desired_cap = {
    "platformName": "Android",
    "deviceName": "RF8M31XC6CF",
    "app": "C:\\Users\\Hamza\\Downloads\\app-staging.apk",
    "udid": "RF8M31XC6CF"
}
@pytest.fixture()
def setup():
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
    driver.implicitly_wait(30)
    return driver