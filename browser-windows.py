"""
------------------------------------------------------------------------
Browser.py -- windows

selenium browser class
------------------------------------------------------------------------
Author: bb $kreetz
Email: bbskreets@protonmail.com
__updated__ = "2020-04-12"
------------------------------------------------------------------------
"""
from CONSTANTS import *
from SETTINGS import *
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import simpleaudio as sa
import os

CHROME_OPTIONS_WIN = ['--ignore-gpu-blacklist', '--no-default-browser-check', '--no-first-run', '--disable-default-apps',
                      '--disable-infobars', '--disable-extensions', '--test-type', '--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--window-size=1420,1080']


class Browser():
    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=resources/drivers/chrome/profile')

        if OS == 'win':
            for opt in CHROME_OPTIONS_WIN:
                options.add_argument(opt)

        if HEADLESS:
            options.add_argument("--headless")

            options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def check_website(self, website):
        valid = False
        if website.site_type == 'amazon':
            try:
                self.driver.get(website.url)

                name = self.driver.find_element_by_xpath('//*[@id="olpProductDetails"]/h1').text
                cur_price = min([float(re.search("\d+\.\d+", price.text).group(0)) for price in self.driver.find_elements_by_class_name('olpOfferPrice')])

                in_stock = True
            except Exception as e:
                print('Error:', e)
                name = website.name
                cur_price = website.cur_price
                in_stock = True

        elif website.site_type == 'bestbuy':
            self.driver.get(website.url)

        if in_stock and website.max_price >= cur_price:
            valid = True
            wave_obj = sa.WaveObject.from_wave_file(f'{SOUNDS_PATH}/{ALERT_SOUND}').play()
            self.driver.close()
            options = webdriver.ChromeOptions()
            if OS == 'win':
                for opt in CHROME_OPTIONS_WIN:
                    options.add_argument(opt)
            options.add_argument('user-data-dir=resources/drivers/chrome/profile')
            self.driver2 = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            self.driver2.get(website.url)
            self.driver2.maximize_window()

        return cur_price, in_stock, name, valid
