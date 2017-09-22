localized = True

from .. import BaseProvider


class Provider(BaseProvider):
    formats = ['{{first_name}}{{email_suffix}}', ]
    email_suffixes = ['@facebook.com', ]

    def email_address(self):
        pattern = self.random_element(self.formats)
        return self.generator.parse(pattern)

    def email_suffix(self):

        return self.random_element(self.email_suffixes)
