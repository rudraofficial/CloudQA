import time
from selenium.webdriver import Chrome


def test_fields(driver, field_names):
    for field_name in field_names:
        field = driver.find_element(by="name", value=field_name)
        field.send_keys("Test")
        time.sleep(1)


def main():
    driver = Chrome()
    driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")
    field_names = ["First Name", "Last Name", "Email"]
    test_fields(driver, field_names)
    driver.quit()


if __name__ == "__main__":
    main()
