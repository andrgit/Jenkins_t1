# import allure
from selenium.webdriver.common.by import By


# from selenium.webdriver import Chrome

# @allure.story("Check valid plugin for shining panda")
# def test_jenkinks_plugin(browser):
#     with allure.step("Open Jenkins page"):
#         browser.get("https://plugins.jenkins.io/shiningpanda")
#     with allure.step("Find title"):
#         title_element = browser.find_element(By.XPATH, "//*[@class='title']")
#     with allure.step("Assert Title"):
#         assert title_element.text == "ShiningPanda"


def test_shining_panda(browser):
    browser.get("https://plugins.jenkins.io/shiningpanda")
    title_element = browser.find_element(By.XPATH, "//*[@class='title']")
    assert title_element.text == "ShiningPanda"
