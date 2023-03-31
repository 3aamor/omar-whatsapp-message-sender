import pywhatkit
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common. keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import *
from selenium.webdriver. support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium. webdriver.support.ui import *
from selenium. webdriver import *
import time
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import logging
import webbrowser
import multiprocessing

start_time = time.time()

num_of_numbers = int(input("how many numbers do you want: "))

url = "https://codebeautify.org/random-phone-number"

path = "chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument = {'user-data-dir':'/Users/Application/Chrome/Default'}

driver.implicitly_wait(5)

driver.get(url)

driver.maximize_window()

master2 = driver.find_element_by_id("inputRandomNumber")
master2.send_keys(num_of_numbers)

button = driver.find_element_by_xpath('//*[@id="app"]/section[2]/div[2]/div[2]/div/div[2]/button')
time.sleep(5)
button.click()

count = 1

id = f'phoneNumber{count}'

the_numbers = []

start_time = time.time()


for i in range(1000):
    
    element = driver.find_element_by_id(id).text
    
    the_numbers.append(element.replace(" ", ""))

    count += 1

print(the_numbers)


print(the_numbers)

end_time = time.time()
print('Time taken to generate numbers: {} seconds'.format(end_time - start_time))

def send_msg():
    for i in the_numbers:
        start_time = time.time()

        phone_number = f"+1{i}"
        messege = "hello"
    # syntax: phone number with country code, message
        pywhatkit.sendwhatmsg_instantly(phone_number, messege)

    # # print(the_numbers)


        end_time = time.time()

        print('Time taken to send message: {} seconds'.format(end_time - start_time))

# if __name__ == '__main__':
#     p = multiprocessing.Process(target=send_msg)
#     p1= multiprocessing.Process(target=send_msg)
#     p2= multiprocessing.Process(target=send_msg)
#     p3= multiprocessing.Process(target=send_msg)
#     p.start()
#     p1.start()
#     p2.start()
#     p3.start()
#     p.join()
#     p1.join()
#     p2.join()
#     p3.join()

send_msg()


driver.implicitly_wait(10)

driver.quit()