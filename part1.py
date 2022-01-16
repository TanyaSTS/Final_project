import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
driver = webdriver.Chrome()

url = "https://www.labirint.ru"


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


#1
    def test_find_function_normal_text(self):
        text1 = u"Война и Мир"
        driver = self.driver
        driver.get(url)
        search_field = driver.find_element(By.ID, "search-field")
        search_field.send_keys(text1)
        search_field.submit()


#2
    def test_find_function_long_text(self):
        text1 = "Очень длинный текст" * 1000
        driver = self.driver
        driver.get(url)
        search_field = driver.find_element(By.ID, "search-field")
        search_field.send_keys(text1)
        search_field.submit()


#3
    def test_find_function_empty_text(self):
        text1 = ""
        driver = self.driver
        driver.get(url)
        search_field = driver.find_element(By.ID, "search-field")
        search_field.send_keys(text1)
        search_field.submit()


#4
    def test_find_function_255sim_text(self):
        text1 = "мирка" * 51
        driver = self.driver
        driver.get(url)
        search_field = driver.find_element(By.ID, "search-field")
        search_field.send_keys(text1)
        search_field.submit()


#5
    def test_find_function_simbols_text(self):
        text1 = "$#@%^&"
        driver = self.driver
        driver.get(url)
        search_field = driver.find_element(By.ID, "search-field")
        search_field.send_keys(text1)
        search_field.submit()


#6
    def test_find_function_numbers_text(self):
        text1 = "123454321"
        driver = self.driver
        driver.get(url)
        search_field = driver.find_element(By.ID, "search-field")
        search_field.send_keys(text1)
        search_field.submit()


#7
    def test_message_button(self):
        driver = self.driver
        driver.get(url)
        message_button = driver.find_element(By.CSS_SELECTOR, "div#minwidth > div:nth-of-type(4) > div > div > div:nth-of-type(2) > div > ul > li:nth-of-type(6) > a > span > span > span:nth-of-type(3)")
        message_button.click()


#8
    def test_registration_with_valid_key(self):
        driver = self.driver
        driver.get(url)
        reg_button = driver.find_element(By.CSS_SELECTOR, "div#minwidth > div:nth-of-type(4) > div > div > div:nth-of-type(2) > div > ul > li:nth-of-type(4) > a > span > span > span")
        reg_button.click()
        kod = "36A5-444A-A1D3"
        reg_button_2 = driver.find_element(By.ID, "_inputnamecode_34")
        reg_button_2.clear
        reg_button_2.send_keys(kod)
        reg_button_2.submit()


#9
    def test_registration_with_unvalid_key(self):
        driver.get(url)
        reg_button = driver.find_element(By.ID, '//*[@id="minwidth"]/div[5]/div/div[1]/div[2]/div/ul/li[4]/a/span[1]/span[1]/span')
        reg_button.click()
        kod = "123456789"
        reg_button_2 = driver.find_element(By.ID, "_inputnamecode_34")
        reg_button_2.clear
        reg_button_2.send_keys(kod)
        reg_button_2.submit()


#10
    def test_heart_button(self):
        driver.get(url)
        heart_button = driver.find_element(By.CSS_SELECTOR, 'div#minwidth > div:nth-of-type(4) > div > div > div:nth-of-type(2) > div > ul > li:nth-of-type(5) > a > span > span > span')
        heart_button.click()


#11
    def test_basket_button_empty(self):
        driver.get(url)
        basket_button = driver.find_element(By.CSS_SELECTOR, "div#minwidth > div:nth-of-type(4) > div > div > div:nth-of-type(2) > div > ul > li:nth-of-type(6) > a > span > span > span:nth-of-type(3)")
        basket_button.click()
        driver.close()

#12
    def test_location_button(self):
        driver.get(url)
        location_button = driver.find_element(By.CLASS_NAME, "region-location-icon-txt")
        location_button.click()


#13
    def test_suggestion_form(self):
        text1 = u"Война и Мир"
        driver = self.driver
        driver.get(url)
        search_field = driver.find_element(By.ID, "search-field")
        search_field.send_keys(text1)
        search_field.submit()
        suggesion_rows = driver.find_element(By.ID, "autohelp_rows")
        suggesion_rows.submit()


#14
    def test_location_suggestion_form_normal_text(self):
        driver.get(url)
        location_button = driver.find_element(By.CLASS_NAME, "region-location-icon-txt")
        location_button.click()
        location_field = driver.find_element(By.ID, "region-post")
        location_field.send_keys(u"Москва")
        location_field.submit()


#15
    def test_location_suggestion_form_long_text(self):
        text1 = u"Очень длинный текст" * 1000
        driver.get(url)
        location_button = driver.find_element(By.CLASS_NAME, "region-location-icon-txt")
        location_button.click()
        location_field = driver.find_element(By.ID, "region-post")
        location_field.send_keys(text1)
        location_field.submit()


#16
    def test_location_suggestion_form_with_empty_test(self):
        text1 = ""
        driver.get(url)
        location_button = driver.find_element(By.CLASS_NAME, "region-location-icon-txt")
        location_button.click()
        location_field = driver.find_element(By.ID, "region-post")
        location_field.send_keys(text1)
        location_field.submit()


#17
    def test_location_suggesion_form_with_255_letter_text(self):
        text1 = u"мирка" * 51
        driver.get(url)
        location_button = driver.find_element(By.CLASS_NAME, "region-location-icon-txt")
        location_button.click()
        location_field = driver.find_element(By.ID, "region-post")
        location_field.send_keys(text1)
        location_field.submit()


#18
    def test_location_suggesion_form_with_simble_text(self):
        text1 = "@#$$%^&%$"
        driver.get(url)
        location_button = driver.find_element(By.CLASS_NAME, "region-location-icon-txt")
        location_button.click()
        location_field = driver.find_element(By.ID, "region-post")
        location_field.send_keys(text1)
        location_field.submit()


#19
    def test_location_suggesion_form_with_numbers_text(self):
        text1 = "56786433"
        driver.get(url)
        location_button = driver.find_element(By.CLASS_NAME, "region-location-icon-txt")
        location_button.click()
        location_field = driver.find_element(By.ID, "region-post")
        location_field.send_keys(text1)
        location_field.submit()

#20
    def test_contacts_button(self):
        driver.get(url)
        contact_button = driver.find_element(By.LINK_TEXT, "Контакты")
        contact_button.click()



#21
    def test_support_button(self):
        driver.get(url)
        contact_button = driver.find_element(By.LINK_TEXT, "Поддержка")
        contact_button.click()
        driver.close()

driver.quit()

