import pytest
from selenium.webdriver.common.by import By
import sys
import time

@pytest.mark.usefixtures('driver')
class TestLink:

    def test_title(self, driver):
        """
        Verify click and title of page
        :return: None
        """
        driver.get('https://lambdatest.github.io/sample-todo-app/')
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.NAME, "li1").click()
        driver.find_element(By.NAME, "li2").click()

        title = "Sample page - lambdatest.com"
        assert title == driver.title
        # driver.implicitly_wait(10)
        # blocking sleep - not a good practice
        time.sleep(10)
        print("test_title complete")

    def test_item(self, driver):
        """
        Verify item submission
        :return: None
        """
        driver.get('https://lambdatest.github.io/sample-todo-app/')
        driver.maximize_window()
        sample_text = "Happy Testing at LambdaTest"
        email_text_field = driver.find_element(By.ID, "sampletodotext")
        email_text_field.send_keys(sample_text)

        driver.find_element(By.ID, "addbutton").click()

        li6 = driver.find_element(By.NAME, "li6")
        # driver.implicitly_wait(10)
        # blocking sleep - not a good practice
        time.sleep(10)
        print("test_item complete")
