# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .. import Provider as WareHouseProvider


class Provider(WareHouseProvider):
    
    state_list = ["上海","北京","广东","武汉","西安","沈阳","云南","成都","长沙","山东"]

    warehouse_list = ['{}仓库'.format(a) for a in state_list]
