from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:/Users\Android - PC\Downloads\drivers\chromedriver.exe")

driver.get("https://www.tutorialspoint.com/online_javascript_editor.php")

driver.find_element_by_xpath("//*[@id='web_view']/span").click()

driver.find_element_by_xpath("//*[@id='banner-accept']").click()

time.sleep(5)--

driver.switch_to_alert().accept()  #close alert window by ok button
#driver.switch_to_alert().dismiss() #close alert window by cancel button