"""
------------------------------------------------------------------------
SwitchSnatcher.py settings
------------------------------------------------------------------------
Author: bb $kreetz
Email: bbskreets@protonmail.com
__updated__ = "2020-04-12"
------------------------------------------------------------------------
"""

OS = 'mac'  # Options: mac, win, linux | Type: str
REFRESH_PERIOD = 1.5  # How often to refresh websites (seconds) | Type: float
ALERT_SOUND = 'air_horn.wav'
BROWSER = 'chrome'  # Options: chrome (currently only chrome supported)| Type: str
BROWSER_VERSION = 81  # Options: 80, 81 | Type: int | Go to chrome://settings/help to see browser version
HEADLESS = False  # If you start getting 'Unable to locate element' errors, change headless to False


# Auto-purchase Settings
# Please read the README.md file for steps to set this up...
# Automatic purchasing does not work yet, will update soon!

# AMZN_AUTOMATION = (False, False, False) # (add to cart, proceed to checkout, pay)
