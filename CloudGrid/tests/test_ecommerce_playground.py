import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures('driver')
@pytest.mark.text
def test_text(driver):
        """
        Verify a text in the page
        :return: None
        """
        driver.get('https://ecommerce-playground.lambdatest.io/')
        driver.implicitly_wait(10)

        txt = "This is a dummy website for Web Automation Testing"
        assert txt == driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div[5]/header/div[3]/div[3]/div[1]/p/strong"
                                        ).text 

@pytest.mark.usefixtures('driver')
@pytest.mark.register
def test_register(driver):
    
    driver.get('https://ecommerce-playground.lambdatest.io/index.php?route=account/register')
    
    first_name = driver.find_element(By.NAME, "firstname")
    first_name.send_keys("James")
    
    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys("Ford")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("jamesford@example.com")

    telephone = driver.find_element(By.NAME, "telephone")
    telephone.send_keys("1234567888")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("password123")

    confirm = driver.find_element(By.NAME, "confirm")
    confirm.send_keys("password123")

    agree = driver.find_element(By.NAME, "agree")
    # Move the cursor to the agree checkbox element before clicking on it
    actions = ActionChains(driver)
    actions.move_to_element(agree).click().perform()

    submit = driver.find_element(By.XPATH, "//input[@value='Continue']")
    submit.click()
    
    driver.implicitly_wait(10)
    
    text = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div/div/h1").text
    
    assert text == "Your Account Has Been Created!"
    