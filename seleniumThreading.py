from selenium import webdriver
import threading

def thread1():

    browser = webdriver.Chrome()

    rep = 0

    while rep < 10000:

        browser.get('https://docs.google.com/forms/d/e/1FAIpQLSfVNRudfbclxj09DsAOIawmmYmE4fNYPKwxKAds1TSTdtkfCw/viewform')

        browser.find_element_by_xpath('//*[@id="mG61Hd"]\
        /div/div/div[2]/div[8]/div/div[2]/div[1]/div/label\
        /div/div[1]').click()
    
        browser.find_element_by_xpath('//*[@id="mG61Hd"]\
        /div/div/div[3]/div/div/div/span/span').click()

        rep += 1

if __name__ == "__main__":

    threading.Thread(target = thread1).start()
    threading.Thread(target = thread1).start()
