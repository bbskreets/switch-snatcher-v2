"""
------------------------------------------------------------------------
Website.py

Where website info is stored
------------------------------------------------------------------------
Author: bb $kreetz
Email: bbskreets@protonmail.com
__updated__ = "2020-04-12"
------------------------------------------------------------------------
"""

#internal imports
from CONSTANTS import *
from SETTINGS import *

#imports
from datetime import datetime
import os
import json


class Website():
    def __init__(self, uuid, url=None, site_type=None, max_price=None):
        """
        :param url: url for link to check
        :param max_price: maximum price willing to pay
        """
        self.uuid = uuid

        if os.path.exists(f'{WEBSITES_PATH}/{self.uuid}.json'):

            with open(f'{WEBSITES_PATH}/{self.uuid}.json', 'r') as fh:
                file_data = json.loads(fh.read())

                self.url = file_data['url']
                self.site_type = file_data['site_type']
                self.max_price = float(file_data['max_price'])
                self.name = file_data['name']
                self.cur_price = float(file_data['cur_price'])
                self.in_stock = file_data['in_stock']
                self.last_checked = datetime.strptime(file_data['last_checked'], DATETIME_STR)

        else:
            self.url = url
            self.site_type = site_type
            self.max_price = max_price
            self.name = None
            self.cur_price = None
            self.in_stock = None
            self.last_checked = None

    def __str__(self):
        return '{:^9}|{:^10}|{:^55}|{:^8}|{:^6}|'.format(
            self.last_checked.strftime("%H:%M:%S"),self.site_type.upper(),self.name,self.cur_price, str(self.in_stock)
        )

    def _save(self):
        file_data = {
            "url":self.url,
            'site_type':self.site_type,
            "max_price":self.max_price,
            "name":self.name,
            "cur_price":self.cur_price,
            "in_stock":self.in_stock,
            "last_checked":self.last_checked.strftime(DATETIME_STR)
        }

        with open(f'{WEBSITES_PATH}/{self.uuid}.json', 'w') as fh:
            json.dump(file_data, fh, indent=2)

        return

    def update_website(self, cur_price, in_stock, name):

        self.name = name
        self.cur_price = cur_price
        self.in_stock = in_stock
        self.last_checked = datetime.now()
        self._save()


    @staticmethod
    def remove_website(uuid):
        os.remove(f'{WEBSITES_PATH}/{uuid}.json')
