from selenium import webdriver #подключение библиотеки
driver = webdriver.Chrome() #получение объекта веб-драйвера для нужного браузера



def test_find_function_normal_text():
    text1 = "Война и Мир"
    selenium.get("https://www.labirint.ru/")
    search_field = selenium.find_element_by_id("search-field")
    search_field.clear
    search_field.send_keys(text1)
    btn_submit = selenium.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn_submit.click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()

def test_find_function_long_text():
    text1 = "Супер очень длинный текст" * 100
    selenium.get("https://www.labirint.ru/")
    search_field = selenium.find_element_by_id("search-field")
    search_field.clear
    search_field.send_keys(text1)
    btn_submit = selenium.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn_submit.click()

def test_find_function_empty_text():
    text1 = ""
    selenium.get("https://www.labirint.ru/")
    search_field = selenium.find_element_by_id("search-field")
    search_field.clear
    search_field.send_keys(text1)
    btn_submit = selenium.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn_submit.click(

def test_find_function_255sim_text():
    text1 = "мирка" * 51
    selenium.get("https://www.labirint.ru/")
    search_field = selenium.find_element_by_id("search-field")
    search_field.clear
    search_field.send_keys(text1)
    btn_submit = selenium.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn_submit.click()

def test_find_function_simbols_text():
    text1 = "$#@%^&"
    selenium.get("https://www.labirint.ru/")
    search_field = selenium.find_element_by_id("search-field")
    search_field.clear
    search_field.send_keys(text1)
    btn_submit = selenium.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn_submit.click()

def test_find_function_numbers_text():
    text1 = "123454321"
    selenium.get("https://www.labirint.ru/")
    search_field = selenium.find_element_by_id("search-field")
    search_field.clear
    search_field.send_keys(text1)
    btn_submit = selenium.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn_submit.click()

def test_message_button():
    selenium.get("https://www.labirint.ru/")
    message_button = selenium.fint_element_by_xpath(/html/body/div[1]/div[5]/div[5]/div/div[1]/div[2]/div/ul/li[3]/a/span[1]/span)
    message_button.click()

def test_registration():
    selenium.get("https://www.labirint.ru/")
    reg_button = selenium.fint_element_by_xpath(//*[@id="minwidth"]/div[5]/div/div[1]/div[2]/div/ul/li[4]/a/span[1]/span[1]/span)
    reg_button.click()
    kod = 36A5-444A-A1D3
    reg_button_2 = selenium.find_element_by_id("_inputnamecode_34")
    reg_button_2.clear
    reg_button_2.send_keys(kod)
    reg_button_3 = selenium.find_element_by_id("g-recap-0-btn")
    reg_button_3.click()


