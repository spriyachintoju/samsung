import yaml
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


with open('variables/details.yaml') as file:
    variables = yaml.load(file, Loader=yaml.FullLoader)

browser = webdriver.Chrome()

browser.get(f'https://www.samsung.com/us/search/searchMain/?listType=g&searchTerm={variables.get("phone")}&sort=most_popular&color={variables.get("mobile_phone_color")}')
select_item = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-result-react"]/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/a')))


select_item.click()
if not variables.get("tradein_option"):
    select_no_trade_in = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="tradeinOptionNo"]')))
    select_no_trade_in.click()

check_out_cart = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="homeCTA"]/div/div/div')))
check_out_cart.click()

add_on = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="add-ons-wrapper"]/div[5]/div/a')))
add_on.click()
proceed_check_page = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="promotionOffer"]/div[3]/div[1]/div/div/span')))
proceed_check_page.click()

print(f'Give phone {variables.get("phone")} added to cart and ready to checkout')
sleep(5)
browser.quit()

