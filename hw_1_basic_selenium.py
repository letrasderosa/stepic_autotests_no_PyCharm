
# ------------Задание: ждем нужный текст на странице
# Написать программу, которая будет бронировать нам дом для отдыха по строго заданной
# цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет
# забронировать кто-то другой.

# Написать программу, которая будет выполнять следующий сценарий:

# -- Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# -- Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не
# меньше 12 секунд)
# -- Нажать на кнопку "Book"
# -- Решить уже известную нам математическую задачу и отправить решение

# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте
# метод text_to_be_present_in_element из библиотеки expected_conditions.

# Если все сделано правильно и быстро, то вы увидите окно с числом.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser.get(link)
    price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(
        (By.ID, 'price'),text_= '100'))
    button = browser.find_element(By.ID, 'book')
    button.click()


    x_element = browser.find_element(By.CSS_SELECTOR, "label > span:nth-child(2)")
    y = calc(int(x_element.text))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    button.click()

except Exception as err:
    print(f"The test is flaky. If any exception occur, try the test again")
    raise

finally:
    time.sleep(2)
    browser.quit()




