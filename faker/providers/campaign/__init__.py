# coding=utf-8
localized = True

from .. import BaseProvider


class Provider(BaseProvider):

    campaign_list = ['Black Friday' ]
    
    def cost(self):
        return self.random_int(300,100000)*10

    def campaign_name(self):
        return self.random_element(self.campaign_list)
	
