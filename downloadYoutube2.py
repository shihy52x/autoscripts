import datetime
import sys
import urllib
from selenium import webdriver
import time
import pdb

def get_url_list(url):
    driver = webdriver.Chrome("/Users/hongboshi/Project/camping/driver/chromedriver")
    driver.get(url)
    #select logdging properties
    time.sleep(5)
    elems = driver.find_elements_by_id("playlist-items")
    res = []
    for elem in elems:
        href = elem.find_element_by_id("thumbnail").get_attribute("href")
        res.append(href)
        print(href)
    return res

def download(url):
    driver = webdriver.Chrome("/Users/hongboshi/Project/camping/driver/chromedriver")
    driver.get("https://ssyoutube.com/en1/youtube-video-downloader")
    time.sleep(5)
    pdb.set_trace()
    search_elem = driver.find_element_by_id("main-form")
    elem = search_elem.find_element_by_id("id_url")
    elem.send_keys(url)
    search_elem.submit()
    time.sleep(5)
    table_elem = driver.find_element_by_id("download-mp4-720-audio")
    table_elem.click()
    driver.close()
    return




redownload_list = []
url="https://www.youtube.com/watch?v=D9M-raooB9k&list=PLxU36BrYn1dY55YLAZDkeqnzmzr6olM4W"
url="https://www.youtube.com/watch?v=rqsJnjYm4KI&list=PLMX26aiIvX5rcYjAW7p_bguZDB-imN_4u"
url_list = get_url_list(url)
if redownload_list:
    url_list = [url_list[i] for i in redownload_list]
for i, url in enumerate(url_list):
    try:
        download(url)
        time.sleep(60)
    except:
        print("did not download " + url)
