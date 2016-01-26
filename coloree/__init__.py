#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from validators import is_cmyk_color_code

verbose_name = _('fiëé colorée')
verbose_name_plural = _('fiëé colorée')


def HtmlColorCode_to_strings(value):
    """
    Convert a HTML color code
    like '#FFCC00' or 'FFCC00'
    to a list of strings ['FF', 'CC', '00']
    """
    x = 1 * value.startswith('#')
    return [value[x:x+2], value[x+2:x+4], value[x+4:x+6]]


def HtmlColorCode_to_ints(value):
    """
    Convert a HTML color code
    like '#FFCC00' or 'FFCC00'
    to a list of integers [255, 204, 0]
    """
    return [int(x, 16) for x in HtmlColorCode_to_strings(value)]


def HtmlColorCode_to_floats(value):
    """
    Convert a HTML color code
    like '#FFCC00' or 'FFCC00'
    to a list of floats [1.0, 0.8, 0.0]
    """
    # return (float.fromhex('0x'+x)/255 for x in HtmlColorCode_to_strings(value))  # fromhex is python 2.6!
    return [float(int(x, 16))/255 for x in HtmlColorCode_to_strings(value)]


def RGB_to_CMYK(r, g, b, gcr=1.0):
    """
    take r,g,b float values (0.0 to 1.0),
    invert to get c,m,y,
    apply GCR (0.0 to 1.0, 0 means no GCR = CMY separation),
    return c,m,y,k as integers (percent values)

    GCR see http://en.wikipedia.org/wiki/Grey_component_replacement
    """
    c, m, y = (1.0 - (float(x)/2) for x in (g+b, r+b, r+g))
    k = min(c, m, y) * gcr
    c, m, y = c-k, m-k, y-k
    return [int(round(x*100)) for x in (c, m, y, k)]


def HtmlColorCode_to_CMYK(value, gcr=1.0):
    """
    Convert from a HTML color code to CMYK values,
    see `RGB_to_CMYK`.
    """
    (r, g, b) = HtmlColorCode_to_floats(value)
    return RGB_to_CMYK(r, g, b, gcr)


def CMYK_to_RGB(cmyk):
    """
    Convert a comma separated integer list into RGB float values, i.e.
    '100,80,0,0' to (0.0, 51.0, 255.0)
    Returns None for invalid input.

    This is a simple number conversion
    that ignores the basics of color management (no profiles involved)!
    """
    if not is_cmyk_color_code(cmyk):
        return None
    c, m, y, k = (float(x) for x in cmyk.split(','))

    if max(c+k, m+k, y+k) > 100:
        k = 100 - max(c, m, y)
    return [(1 - (x+k)/100)*255 for x in (c, m, y)]


def CMYK_to_HtmlColorCode(cmyk):
    """
    Convert a comma separated integer list into a HTML hex color code, i.e.
    '100,80,0,0' to '#0032FF'
    Returns empty string for invalid input.

    This is a simple number conversion
    that ignores the basics of color management (no profiles involved)!
    """
    t = CMYK_to_RGB(cmyk)
    if t: return '#%02X%02X%02X' % (t[0], t[1], t[2])
    return ''


def color_spot(htmlcolorcode, text=None):
    """
    HTML snippet: span with class 'colorspot' and `htmlcolorcode`
    as background color
    """
    if text is None:
        text = htmlcolorcode
    return u'<span class="colorspot" style="background-color:%s;">&nbsp;&nbsp;&nbsp;</span>&nbsp;%s' % (htmlcolorcode, text)
