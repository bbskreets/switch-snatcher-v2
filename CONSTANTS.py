"""
------------------------------------------------------------------------
Constants
------------------------------------------------------------------------
Author: bb $kreetz
Email: bbskreets@protonmail.com
__updated__ = "2020-04-12"
------------------------------------------------------------------------
"""
from SETTINGS import *
import os


RESOURCES_PATH = 'resources'
WEBSITES_PATH = f'{RESOURCES_PATH}/websites'
URL_MAP_PATH = f'{WEBSITES_PATH}/map.json'
SOUNDS_PATH = f'{RESOURCES_PATH}/sounds/'
PROXIES_PATH = f'{RESOURCES_PATH}/proxies'
DRIVER_FOLDER = f'{RESOURCES_PATH}/drivers/{BROWSER}/version_{BROWSER_VERSION}'
DRIVER_PATH = f'{RESOURCES_PATH}/drivers/{BROWSER}/version_{BROWSER_VERSION}/{OS}'
CHROME_PROFILE_PATH = f'{RESOURCES_PATH}/drivers/{BROWSER}/profile'
SITE_TYPES = ('amazon')  # todo --> 'bestbuy','thesource','walmart','staples','ebgames'


DATETIME_STR = "%m/%d/%Y, %H:%M:%S"

INTRO = """
----------------------------------------------------------------------------------------------------
██████╗ ██████╗     ▄▄███▄▄·██╗  ██╗██████╗ ███████╗███████╗████████╗███████╗
██╔══██╗██╔══██╗    ██╔════╝██║ ██╔╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝╚══███╔╝
██████╔╝██████╔╝    ███████╗█████╔╝ ██████╔╝█████╗  █████╗     ██║     ███╔╝
██╔══██╗██╔══██╗    ╚════██║██╔═██╗ ██╔══██╗██╔══╝  ██╔══╝     ██║    ███╔╝
██████╔╝██████╔╝    ███████║██║  ██╗██║  ██║███████╗███████╗   ██║   ███████╗
╚═════╝ ╚═════╝     ╚═▀▀▀══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚══════╝
                                                         Switch Snatcher v2.0
----------------------------------------------------------------------------------------------------"""

if not os.path.exists(CHROME_PROFILE_PATH):
    os.makedirs(CHROME_PROFILE_PATH)
