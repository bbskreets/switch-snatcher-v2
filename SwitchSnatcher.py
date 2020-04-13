"""
------------------------------------------------------------------------
SwitchSnatcher.py Functions
------------------------------------------------------------------------
Author: bb $kreetz
Email: bbskreets@protonmail.com
__updated__ = "2020-04-12"
------------------------------------------------------------------------
"""

from CONSTANTS import *

from Website import Website
from URLMap import urlmap
from Browser import Browser
from datetime import datetime
import time
import colorama





def clear():
    print("\x1b[2J")

def reposition(x, y):
    print("\x1b[{};{}H".format(x + 1, y + 1))

def reset_screen():
    clear()
    reposition(0,0)
    colorama.init()
    print(colorama.Fore.BLUE + INTRO + colorama.Fore.RESET)
    position = 12
    reposition(position,0)
    for _ in URL_MAP:
        reposition(position, 0)
        print(colorama.Fore.YELLOW + 'Loading...' + colorama.Fore.RESET)
        position += 1
    reposition(position + 2, 0)
    print(colorama.Fore.YELLOW + 'Press CTRL+C to go back to main menu.' + colorama.Fore.RESET)

def add_website(url, site_type, max_price):
    browser = Browser()
    if url not in URL_MAP.map.values():
        uuid = URL_MAP.add(url)
        website = Website(uuid, url=url, site_type=site_type, max_price=max_price)
        cur_price, in_stock, name, value = browser.check_website(website)
        website.update_website(cur_price, in_stock, name)
        created = True

    else:
        created = False

    browser.driver.close()

    return created

def remove_website(uuid):
    removed = False
    try:
        URL_MAP.remove_site(uuid)
        Website.remove_website(uuid)
        removed = True

    except Exception as e:
        print(f'{e}')
        time.sleep(5)

    return removed

def start_checking():
    browser = Browser()
    clear()
    count = 0
    reposition(0,0)
    colorama.init()
    print(colorama.Fore.BLUE + INTRO + colorama.Fore.RESET)
    valid = False

    reset_screen()

    try:
        count = 0
        while not valid:

            website, line = website_list.pop(0)
            website_list.append([website, line])
            curtime = datetime.now()
            seconds_passed = int((curtime-website.last_checked).total_seconds())
            if seconds_passed < REFRESH_PERIOD:
                time.sleep(REFRESH_PERIOD-seconds_passed)

            else:
                count += 1
                cur_price, in_stock, name, item_valid = browser.check_website(website)
                website.update_website(cur_price, in_stock, name)

                if item_valid:
                    print(colorama.Fore.GREEN + str(website) + colorama.Fore.RESET)
                    time.sleep(3)
                    valid = True

                else:
                    if count == len(website_list)*3:
                        reset_screen()
                        count = 0
                    reposition(line, 0)
                    print(colorama.Fore.RED + str(website) + colorama.Fore.RESET)

    except KeyboardInterrupt:
        try:
            browser.driver.close()
            time.sleep(1)
        except Exception as e:
            print(e)

URL_MAP = urlmap()

website_list = []

position = 12
for uuid in URL_MAP:
    site = Website(uuid)
    website_list.append([site, position])
    position += 1
