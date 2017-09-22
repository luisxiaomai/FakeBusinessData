# coding=utf-8

from __future__ import unicode_literals
from .. import BaseProvider


class Provider(BaseProvider):

    def unit_price(self):
        return self.random_int(300,2000)

    def quantity(self):
        return self.random_int(1,50)*10