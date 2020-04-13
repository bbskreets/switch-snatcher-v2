"""
------------------------------------------------------------------------
URL Map
------------------------------------------------------------------------
Author: bb $kreetz
Email: bbskreets@protonmail.com
__updated__ = "2020-04-12"
------------------------------------------------------------------------
"""

from SETTINGS import *
from CONSTANTS import *
import json
from uuid import uuid4
import os

# if os.curdir == '.':
#     os.chdir('switch_snatcher')

class urlmap():
    def __init__(self):

        with open(URL_MAP_PATH, 'r') as fh:
            self.map = json.loads(fh.read())

        return

    def __iter__(self):
        for i in self.map:
            yield i

    def __getitem__(self, item):
        return self.map[item]

    def add(self, url):
        uuid = self._get_uuid()
        self.map[uuid] = str(url)
        self._save()

        return uuid

    def _save(self):
        with open(URL_MAP_PATH, 'w') as fh:
            json.dump(self.map, fh, indent=2)

        return

    def _get_uuid(self):
        uuid = uuid4()
        while uuid in self.map.values():
            uuid = uuid4()

        return str(uuid)

    def remove_site(self, uuid):
        self.map.pop(uuid)
        self._save()
