from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
mensa_norway_url = "https://test.mensa.no/"
driver.get(mensa_norway_url)
driver.maximize_window()

age_1850 = driver.find_element(By.CLASS_NAME, "ageselect_1850")
age_1850.click()
time.sleep(2)

start_button = driver.find_element(By.ID, "startTest")
start_button.click()


driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)
q1_a_button = driver.find_element(By.XPATH, "//div[@id='question_0']/div/div/div[@data-answerid='0']")
q1_a_button.click()
time.sleep(3)

q2_b_button = driver.find_element(By.XPATH, "//div[@id='question_1']/div/div/div[@data-answerid='1']")
q2_b_button.click()
time.sleep(2)

q3_c_button = driver.find_element(By.XPATH,"//div[@id='question_2']/div/div/div[@data-answerid='2']")
q3_c_button.click()
time.sleep(2)

q4_d_button = driver.find_element(By.XPATH,"//div[@id='question_3']/div/div/div[@data-answerid='3']")
q4_d_button.click()
time.sleep(2)

q5_e_button = driver.find_element(By.XPATH, "//div[@id='question_4']/div/div/div[@data-answerid='4']")
q5_e_button.click()
time.sleep(2)

q6_f_button = driver.find_element(By.XPATH,"//div[@id='question_5']/div/div/div[@data-answerid='5']")
q6_f_button.click()
time.sleep(2)

q7_b_button = driver.find_element(By.XPATH,"//div[@id='question_6']/div/div/div[@data-answerid='1']")
q7_b_button.click()
time.sleep(2)

q8_d_button = driver.find_element(By.XPATH,"//div[@id='question_7']/div/div/div[@data-answerid='3']")
q8_d_button.click()
time.sleep(2)

q9_e_button = driver.find_element(By.XPATH,"//div[@id='question_8']/div/div/div[@data-answerid='4']")
q9_e_button.click()
time.sleep(2)

q10_f_button = driver.find_element(By.XPATH,"//div[@id='question_9']/div/div/div[@data-answerid='5']")
q10_f_button.click()
time.sleep(2)

q11_c_button = driver.find_element(By.XPATH,"//div[@id='question_10']/div/div/div[@data-answerid='2']")
q11_c_button.click()
time.sleep(2)

q12_f_button = driver.find_element(By.XPATH,"//div[@id='question_11']/div/div/div[@data-answerid='5']")
q12_f_button.click()
time.sleep(2)

q13_b_button = driver.find_element(By.XPATH,"//div[@id='question_12']/div/div/div[@data-answerid='1']")
q13_b_button.click()
time.sleep(2)

q14_b_button = driver.find_element(By.XPATH,"//div[@id='question_13']/div/div/div[@data-answerid='1']")
q14_b_button.click()
time.sleep(2)

q15_e_button = driver.find_element(By.XPATH,"//div[@id='question_14']/div/div/div[@data-answerid='4']")
q15_e_button.click()
time.sleep(2)

q16_e_button = driver.find_element(By.XPATH,"//div[@id='question_15']/div/div/div[@data-answerid='4']")
q16_e_button.click()
time.sleep(3)

q17_b_button = driver.find_element(By.XPATH,"//div[@id='question_16']/div/div/div[@data-answerid='1']")
q17_b_button.click()
time.sleep(3)

q18_b_button = driver.find_element(By.XPATH,"//div[@id='question_17']/div/div/div[@data-answerid='1']")
q18_b_button.click()
time.sleep(2)

q19_c_button = driver.find_element(By.XPATH,"//div[@id='question_18']/div/div/div[@data-answerid='2']")
q19_c_button.click()
time.sleep(2)

q20_f_button = driver.find_element(By.XPATH,"//div[@id='question_19']/div/div/div[@data-answerid='5']")
q20_f_button.click()
time.sleep(3)

q21_c_button = driver.find_element(By.XPATH,"//div[@id='question_20']/div/div/div[@data-answerid='2']")
q21_c_button.click()
time.sleep(3)

q22_c_button = driver.find_element(By.XPATH,"//div[@id='question_21']/div/div/div[@data-answerid='2']")
q22_c_button.click()
time.sleep(2)

q23_d_button = driver.find_element(By.XPATH,"//div[@id='question_22']/div/div/div[@data-answerid='3']")
q23_d_button.click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)
q24_a_button = driver.find_element(By.XPATH,"//div[@id='question_23']/div/div/div[@data-answerid='0']")
q24_a_button.click()
time.sleep(2)

q25_f_button = driver.find_element(By.XPATH,"//div[@id='question_24']/div/div/div[@data-answerid='5']")
q25_f_button.click()
time.sleep(2)

q26_b_button = driver.find_element(By.XPATH,"//div[@id='question_25']/div/div/div[@data-answerid='1']")
q26_b_button.click()
time.sleep(2)

q27_c_button = driver.find_element(By.XPATH,"//div[@id='question_26']/div/div/div[@data-answerid='2']")
q27_c_button.click()
time.sleep(2)

q28_b_button = driver.find_element(By.XPATH,"//div[@id='question_27']/div/div/div[@data-answerid='1']")
q28_b_button.click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)
q29_a_button = driver.find_element(By.XPATH,"//div[@id='question_28']/div/div/div[@data-answerid='0']")
q29_a_button.click()
time.sleep(2)

q30_d_button = driver.find_element(By.XPATH,"//div[@id='question_29']/div/div/div[@data-answerid='3']")
q30_d_button.click()
time.sleep(2)

q31_f_button = driver.find_element(By.XPATH,"//div[@id='question_30']/div/div/div[@data-answerid='5']")
q31_f_button.click()
time.sleep(2)

q32_e_button = driver.find_element(By.XPATH,"//div[@id='question_31']/div/div/div[@data-answerid='4']")
q32_e_button.click()
time.sleep(2)

q33_c_button = driver.find_element(By.XPATH,"//div[@id='question_32']/div/div/div[@data-answerid='2']")
q33_c_button.click()
time.sleep(2)

q34_b_button = driver.find_element(By.XPATH,"//div[@id='question_33']/div/div/div[@data-answerid='1']")
q34_b_button.click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)
q35_a_button = driver.find_element(By.XPATH,"//div[@id='question_34']/div/div/div[@data-answerid='0']")
q35_a_button.click()
time.sleep(5)




#//div[@id='question_3']/div/div/div[@data_answerid='3']
#//div[@id='question_2']/div/div/div[@data-answerid='2']