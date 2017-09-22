from __future__ import unicode_literals
from .. import Provider as EmailProvider


class Provider(EmailProvider):
    formats = ['{{last_name}}.{{first_name}}{{email_suffix}}', ]
    email_suffixes = ['@facebook.com', '@gamil.com','@outlook.com','@yahoo.com','@gmx.com','@inbox.com','@126.com', '@qq.com','@sina.com','@163.com','@sohu.com','@360.com',]
