from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
mensa_norway_url = "https://test.mensa.no/"
driver.get(mensa_norway_url)
driver.maximize_window()
xpath_template = '//div[contains(@id,"question_") and @style=""]'

age_1850_class_name = "ageselect_1850"
age_1850 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, age_1850_class_name)))
#age_1850 = driver.find_element(By.CLASS_NAME, "ageselect_1850")
age_1850.click()
#time.sleep(2)

start_button_id = "startTest"
start_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, start_button_id)))
#start_button = driver.find_element(By.ID, "startTest")
start_button.click()


driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
xpath_template = '//div[contains(@id,"question_") and @style=""]'
#time.sleep(3)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q1_a_button_xpath = "//div[@id='question_0']/div/div/div[@data-answerid='0']"
q1_a_button = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, q1_a_button_xpath)))
#q1_a_button = driver.find_element(By.XPATH, "//div[@id='question_0']/div/div/div[@data-answerid='0']")
#time.sleep(5)
q1_a_button.click()
#time.sleep(20)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q2_b_button_xpath = "//div[@id='question_1']/div/div/div[@data-answerid='1']"
q2_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q2_b_button_xpath)))
#q2_b_button = driver.find_element(By.XPATH, "//div[@id='question_1']/div/div/div[@data-answerid='1']")
q2_b_button.click()
#time.sleep(2)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q3_c_button_xpath = "//div[@id='question_2']/div/div/div[@data-answerid='2']"
q3_c_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,q3_c_button_xpath)))
q3_c_button.click()
#time.sleep(2)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q4_d_button_xpath = "//div[@id='question_3']/div/div/div[@data-answerid='3']"
q4_d_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,q4_d_button_xpath)))
q4_d_button.click()
time.sleep(30)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q5_e_button_xpath = "//div[@id='question_4']/div/div/div[@data-answerid='4']"
q5_e_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q5_e_button_xpath)))
q5_e_button.click()
#time.sleep(2)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q6_f_button_xpath = "//div[@id='question_5']/div/div/div[@data-answerid='5']"
q6_f_button = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,q6_f_button_xpath)))
q6_f_button.click()
#time.sleep(2)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q7_b_button_xpath = "//div[@id='question_6']/div/div/div[@data-answerid='1']"
q7_b_button = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,q7_b_button_xpath)))
q7_b_button.click()
#time.sleep(2)

WebDriverWait(driver ,30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q8_d_button_xpath = "//div[@id='question_7']/div/div/div[@data-answerid='3']"
q8_d_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q8_d_button_xpath)))
q8_d_button.click()
#time.sleep(2)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q9_e_button_xpath = "//div[@id='question_8']/div/div/div[@data-answerid='4']"
q9_e_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q9_e_button_xpath)))
q9_e_button.click()
#time.sleep(2)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q10_f_button_xpath = "//div[@id='question_9']/div/div/div[@data-answerid='5']"
q10_f_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q10_f_button_xpath)))
q10_f_button.click()
#time.sleep(2)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q11_c_button_xpath = "//div[@id='question_10']/div/div/div[@data-answerid='2']"
q11_c_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q11_c_button_xpath)))
q11_c_button.click()
#time.sleep(2)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q12_f_button_xpath = "//div[@id='question_11']/div/div/div[@data-answerid='5']"
q12_f_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q12_f_button_xpath)))
q12_f_button.click()
#time.sleep(2)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q13_b_button_xpath = "//div[@id='question_12']/div/div/div[@data-answerid='1']"
q13_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q13_b_button_xpath)))
q13_b_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q14_b_button_xpath = "//div[@id='question_13']/div/div/div[@data-answerid='1']"
q14_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q14_b_button_xpath)))
q14_b_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q15_e_button_xpath = "//div[@id='question_14']/div/div/div[@data-answerid='4']"
q15_e_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q15_e_button_xpath)))
q15_e_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q16_e_button_xpath = "//div[@id='question_15']/div/div/div[@data-answerid='4']"
q16_e_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q16_e_button_xpath)))
q16_e_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q17_b_button_xpath = "//div[@id='question_16']/div/div/div[@data-answerid='1']"
q17_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q17_b_button_xpath)))
q17_b_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q18_b_button_xpath = "//div[@id='question_17']/div/div/div[@data-answerid='1']"
q18_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q18_b_button_xpath)))
q18_b_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q19_c_button_xpath = "//div[@id='question_18']/div/div/div[@data-answerid='2']"
q19_c_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q19_c_button_xpath)))
q19_c_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q20_f_button_xpath = "//div[@id='question_19']/div/div/div[@data-answerid='5']"
q20_f_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q20_f_button_xpath)))
q20_f_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q21_c_button_xpath = "//div[@id='question_20']/div/div/div[@data-answerid='2']"
q21_c_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q21_c_button_xpath)))
q21_c_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q22_c_button_xpath = "//div[@id='question_21']/div/div/div[@data-answerid='2']"
q22_c_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q22_c_button_xpath)))
q22_c_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q23_d_button_xpath = "//div[@id='question_22']/div/div/div[@data-answerid='3']"
q23_d_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q23_d_button_xpath)))
q23_d_button.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q24_a_button_xpath = "//div[@id='question_23']/div/div/div[@data-answerid='0']"
q24_a_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q24_a_button_xpath)))
q24_a_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q25_f_button_xpath = "//div[@id='question_24']/div/div/div[@data-answerid='5']"
q25_f_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q25_f_button_xpath)))
q25_f_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q26_b_button_xpath = "//div[@id='question_25']/div/div/div[@data-answerid='1']"
q26_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q26_b_button_xpath)))
q26_b_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q27_c_button_xpath = "//div[@id='question_26']/div/div/div[@data-answerid='2']"
q27_c_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q27_c_button_xpath)))
q27_c_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q28_b_button_xpath = "//div[@id='question_27']/div/div/div[@data-answerid='1']"
q28_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q28_b_button_xpath)))
q28_b_button.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q29_a_button_xpath = "//div[@id='question_28']/div/div/div[@data-answerid='0']"
q29_a_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q29_a_button_xpath)))
q29_a_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q30_d_button_xpath = "//div[@id='question_29']/div/div/div[@data-answerid='3']"
q30_d_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q30_d_button_xpath)))
q30_d_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q31_f_button_xpath = "//div[@id='question_30']/div/div/div[@data-answerid='5']"
q31_f_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q31_f_button_xpath)))
q31_f_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q32_e_button_xpath = "//div[@id='question_31']/div/div/div[@data-answerid='4']"
q32_e_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q32_e_button_xpath)))
q32_e_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q33_c_button_xpath = "//div[@id='question_32']/div/div/div[@data-answerid='2']"
q33_c_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q33_c_button_xpath)))
q33_c_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q34_b_button_xpath = "//div[@id='question_33']/div/div/div[@data-answerid='1']"
q34_b_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q34_b_button_xpath)))
q34_b_button.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q35_a_button_xpath = "//div[@id='question_34']/div/div/div[@data-answerid='0']"
q35_a_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, q35_a_button_xpath)))
q35_a_button.click()





#//div[@id='question_3']/div/div/div[@data_answerid='3']
#//div[@id='question_2']/div/div/div[@data-answerid='2']