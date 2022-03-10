import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_HomepageTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title == "OrangeHRM"

    def test_Login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("Admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title == "OrangeHRM"

#RUN->pytest -v -s --html=report.html --self-contained-html test_OrangeHRM.py