"""
------------------------------------------------------------------------
File to launch Switch Snatcher
------------------------------------------------------------------------
File: run.py
Author: bb $kreetz
Email: bbskreets@protonmail.com
__updated__ = "2020-04-12"
------------------------------------------------------------------------
"""

from CONSTANTS import *
from SETTINGS import *
from SwitchSnatcher import *
import colorama
import time

running = True

colorama.init()


def clear():
    print("\x1b[2J")


def reposition(x, y):
    print("\x1b[{};{}H".format(x + 1, y + 1))


def reset_screen():
    clear()
    reposition(0, 0)
    print(colorama.Fore.YELLOW + INTRO + colorama.Fore.RESET)


while running:
    reset_screen()

    print('1) Start Checking Websites')
    print('2) Add New Websites')
    print('3) Remove Websites')
    print('4) Exit Program')
    x = input('--> ')

    if x == '1':
        x = None
        try:
            start_checking()

        except Exception as e:
            print(f'Error: {e}')
            time.sleep(5)

    elif x == '2':
        x = None
        adding_site = True
        site_type = None
        while adding_site:
            reset_screen()
#             print('Supported Websites:', ', '.join(map(str, SITE_TYPES)))
            print('Supported Websites: amazon')
            url = input('URL: ')

            if 'amazon.ca' in url.lower():
                site_type = 'amazon'

            elif 'bestbuy.ca' in url.lower():
                site_type = 'bestbuy'

            elif 'thesource.ca' in url.lower():
                site_type = 'thesource'

            elif 'walmart.ca' in url.lower():
                site_type = 'walmart'

            elif 'staples.ca' in url.lower():
                site_type = 'staples'

            elif 'ebgames.ca' in url.lower():
                site_type = 'ebgames'

            if site_type is not None:
                max_price = None
                while type(max_price) is not float:
                    reset_screen()
                    max_price = input('Maximum price to pay: ')
                    try:
                        max_price = float(max_price)
                        reset_screen()
                        print('Adding website...')
                        added = add_website(url, site_type, max_price)
                        if added:
                            print('Done!')

                        else:
                            print('Website already exists.')
                        adding_site = False
                        time.sleep(2)

                    except Exception as e:
                        print(e)
                        print('Please enter a valid price.')
                        time.sleep(2)

            else:
                reset_screen()
                print('Please check the URL and make sure it is valid.')
                time.sleep(2)

    elif x == '3':
        x = None
        removing = True
        while removing:
            items = {}
            count = 0
            reset_screen()

            for i in URL_MAP:
                count += 1
                items[count] = i
                print(f'{count}) {URL_MAP[i]}')

            try:
                print("\nenter 'x' to go back.")
                to_remove = input('Website to remove: ')
                reset_screen()

                if to_remove.lower() == 'x':
                    removing = False

                elif int(to_remove) in items:
                    if remove_website(items[int(to_remove)]):
                        print('Successfully removed.')
                        removing = False

                    else:
                        print('Error, please try again.')

                    time.sleep(2)

                else:
                    print('Please enter a valid number.')
                    time.sleep(2)

            except ValueError:
                print('Please enter a valid number.')
                time.sleep(2)

    elif x == '4':
        clear()
        running = False

    else:
        reset_screen()
        print('Invalid selection...')
        time.sleep(2)
