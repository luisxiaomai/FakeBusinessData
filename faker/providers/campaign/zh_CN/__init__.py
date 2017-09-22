# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .. import Provider as CampaignProvider

class Provider(CampaignProvider):
    
    name_list = ["双十一","618","年初大促","年终大促","年底大促","周年庆","元旦","春节","元宵节","中秋","七夕节","情人节","端午节","五一","国庆","妇女节",
    			 "母婴","青年节","儿童节","双十二"]

    campaign_list = ['{} 活动'.format(a) for a in name_list]
