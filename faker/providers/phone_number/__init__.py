localized = True

from .. import BaseProvider


class Provider(BaseProvider):
    formats = ('###-###-###',)
    formats2 = ('135########',)

    def phone_number(self):
        return self.numerify(self.random_element(self.formats))

    def cell_phone(self):
        return self.numerify(self.random_element(self.formats2))
