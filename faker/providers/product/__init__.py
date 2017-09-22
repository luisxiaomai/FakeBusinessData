# coding=utf-8
localized = True

from .. import BaseProvider


class Provider(BaseProvider):

    '''
    product_name
    '''
    products_name = ["Clarks Men Leather Casual Sneakers"]


    batchFormats = ('BN-10#######',)
    serialFormats = ('SN-10#######',)

    uomFormats = ["bundle", ]


    '''
    product_barcode
    '''
    def product_name(self):
        return self.random_element(self.products_name)

    def batch_number(self):
        return self.numerify(self.random_element(self.batchFormats))
        
    def serial_code(self):
        return self.numerify(self.random_element(self.serialFormats))

    def UoM(self):
        return self.numerify(self.random_element(self.uomFormats))

 