from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import csv

driver = webdriver.Firefox()
url = 'https://fleximize.com/unicorns/'
driver.get(url)
time.sleep(3)

name = []
description = []
founded = []
becameUnicorn = []
timeToUnicorn = []

for i in range(1,224):
    element = driver.find_element_by_xpath("//*[@id='chartRows']/li[{}]".format(i))
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()
    time.sleep(2)
    name.append(driver.find_element_by_class_name("name").text)
    print(driver.find_element_by_class_name("name").text)
    description.append(driver.find_element_by_class_name("description").text)
    founded.append(driver.find_element_by_class_name("founded").text)
    becameUnicorn.append(driver.find_element_by_class_name("becameUnicorn").text)
    timeToUnicorn.append(driver.find_element_by_class_name("timeToUnicorn").text)


with open ('ready.csv','w',encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(('name', 'description', 'founded','becameUnicorn', 'timeToUnicorn'))
    for row in zip(name, description, founded, becameUnicorn, timeToUnicorn):
        writer.writerow(row)
