from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
mensa_lux_url = "https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"
driver.get(mensa_lux_url)
driver.maximize_window()

q1 = driver.find_element(By.NAME, "q1")
q1.send_keys('m')
time.sleep(1)

q2 = driver.find_element(By.NAME, "q2")
q2.send_keys('15')
time.sleep(1)

q3 = driver.find_element(By.NAME, "q3")
q3.send_keys('6')
time.sleep(1)

q4 = driver.find_element(By.NAME, "q4")
q4.send_keys('10')
time.sleep(1)

q5 = driver.find_element(By.NAME, "q5")
q5.send_keys('2')
time.sleep(1)

q6 = driver.find_element(By.NAME, "q6")
q6.send_keys('35')
time.sleep(1)

q7 = driver.find_element(By.NAME, "q7")
q7.send_keys('1')
time.sleep(1)

q8 = driver.find_element(By.NAME, "q8")
q8.send_keys('9')
time.sleep(1)

q9 = driver.find_element(By.XPATH, "//input[@name='q9' and @value='c']")
q9.click()
time.sleep(1)

q10 = driver.find_element(By.XPATH, "//input[@name='q10' and @value='b']")
q10.click()
time.sleep(1)

q11 = driver.find_element(By.XPATH, "//input[@name='q11' and @value='d']")
q11.click()
time.sleep(1)

q12 = driver.find_element(By.XPATH, "//input[@name='q12' and @value='a']")
q12.click()
time.sleep(1)

q13 = driver.find_element(By.XPATH, "//input[@name='q13' and @value='c']")
q13.click()
time.sleep(1)

q14 = driver.find_element(By.XPATH, "//input[@name='q14' and @value='d']")
q14.click()
time.sleep(1)

q15 = driver.find_element(By.XPATH, "//input[@name='q15' and @value='a']")
q15.click()
time.sleep(1)

q16 = driver.find_element(By.XPATH, "//input[@name='q16' and @value='b']")
q16.click()
time.sleep(1)

q17 = driver.find_element(By.XPATH, "//input[@name='q17' and @value='c']")
q17.click()
time.sleep(1)

q18 = driver.find_element(By.XPATH, "//input[@name='q18' and @value='d']")
q18.click()
time.sleep(1)

q19 = driver.find_element(By.XPATH, "//input[@name='q19' and @value='e']")
q19.click()
time.sleep(1)

q20 = driver.find_element(By.XPATH, "//input[@name='q20' and @value='b']")
q20.click()
time.sleep(1)

q21 = driver.find_element(By.XPATH, "//input[@name='q21' and @value='a']")
q21.click()
time.sleep(1)

q22 = driver.find_element(By.XPATH, "//input[@name='q22' and @value='c']")
q22.click()
time.sleep(1)

q23 = driver.find_element(By.XPATH, "//input[@name='q23' and @value='d']")
q23.click()
time.sleep(1)

q24 = driver.find_element(By.XPATH, "//input[@name='q24' and @value='b']")
q24.click()
time.sleep(1)

q25 = driver.find_element(By.XPATH, "//input[@name='q25' and @value='a']")
q25.click()
time.sleep(1)

q26 = driver.find_element(By.XPATH, "//input[@name='q26' and @value='c']")
q26.click()
time.sleep(1)

q27 = driver.find_element(By.XPATH, "//input[@name='q27' and @value='d']")
q27.click()
time.sleep(1)

q28 = driver.find_element(By.XPATH, "//input[@name='q28' and @value='b']")
q28.click()
time.sleep(1)

q29 = driver.find_element(By.XPATH, "//input[@name='q29' and @value='a']")
q29.click()
time.sleep(1)

q30 = driver.find_element(By.XPATH, "//input[@name='q30' and @value='c']")
q30.click()
time.sleep(1)

q31 = driver.find_element(By.XPATH, "//input[@name='q31' and @value='d']")
q31.click()
time.sleep(1)

q32 = driver.find_element(By.XPATH, "//input[@name='q32' and @value='b']")
q32.click()
time.sleep(1)

q33 = driver.find_element(By.XPATH, "//input[@name='q33' and @value='a']")
q33.click()
time.sleep(1)
