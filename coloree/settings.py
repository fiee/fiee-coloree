# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
# from django.utils.translation import ugettext_lazy as _
_ = lambda s: s  # don’t import settings!

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de'
LANGUAGES = (('de', _('German')),
             ('en', _('English')),
             )

USE_I18N = True
USE_L10N = True
