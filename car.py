import datetime
import sys
import urllib
from selenium import webdriver
import time
url="https://automobiles.honda.com/tools/inventory-results/?vehiclemodelseries=pilot&modelYear=2021&exteriorColor=NH-883P"
import pdb


#https://automobiles.honda.com/tools/inventory-results/?vehiclemodelseries=pilot&modelYear=2021&trim=EX-L&exteriorColor=NH-883P&interiorColor=5473037EFA8245B6B1D020B6D12639C9&zipcode=94706


def get_available_prices(url):
    pdb.set_trace()
    driver = webdriver.Chrome("/Users/hongboshi/Project/camping/driver/chromedriver")
    driver.get(url)
#    driver.find_elements_by_xpath("//*[@id='book-drop']")[0].click()
    
    #select logdging properties
    driver.find_element_by_id('box-widget_InitialProductSelection').find_elements_by_tag_name('option')[1].click()
    #select number of rooms
    driver.find_element_by_id('box-widget_UnitCount').find_elements_by_tag_name('option')[0].click()

    # select number of adults
    driver.find_element_by_id('box-widget_Adults').find_elements_by_tag_name('option')[1]

    #select arrival date
    driver.find_element_by_id('box-widget_ArrivalDate').send_keys(arrival_day)

    #select arrival date
    driver.find_element_by_id('box-widget_DepartureDate').send_keys(departure_day)

    #submit
    #driver.find_elements_by_xpath("/html/body/div[7]/div/div/div[2]/div/div/form/div[12]")[0].click()
    driver.find_elements_by_xpath("/html/body/div[5]/div[2]/div/div[3]/div/div[2]/nav/div[1]/ul/li/div/div/form/div[12]/input")[0].click()

    time.sleep(15)
    texts = driver.find_elements_by_id("tblDataTableResults")[0].text
    res = []
    for text in texts.split("Best Available Rate")[1:]:
        res.append(text.split("AVERAGE")[0])
    driver.quit()
    return res

current_day = datetime.date(2021, 7, 1)
date_delta = datetime.timedelta(days=1)
import pdb
for i in [94706, 94504]:
    try:
        url_new  = url[:-1] + "&zipcode=" + str(i) + '"'
        res = get_available_prices(url_new)
        print(res)
    except:
        print("did not find available hotels for " + i)
