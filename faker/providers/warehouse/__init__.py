# coding=utf-8
localized = True

from .. import BaseProvider


class Provider(BaseProvider):

    warehouse_list = ['New Youk Warehouse' ]
    
    def warehouse_name(self):
        return self.random_element(self.warehouse_list)
	
