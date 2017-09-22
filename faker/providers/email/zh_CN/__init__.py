# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as EmailProvider


class Provider(EmailProvider):
    formats = ['{{last_name}}.{{first_name}}{{email_suffix}}', ]
    email_suffixes = ['@126.com', '@qq.com','@sina.com','@163.com','@sohu.com','@360.com',]
