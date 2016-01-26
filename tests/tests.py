# see https://docs.djangoproject.com/en/1.9/topics/testing/
from __future__ import unicode_literals
from django.test import TestCase
from django.core.urlresolvers import reverse

from . import *


class ColorConversionTests(TestCase):

    def test_htmlcolorcodetostrings(self):
        """
        check function `HtmlColorCode_to_strings`
        """
        self.assertEqual(HtmlColorCode_to_strings('FFCC00'), ['FF', 'CC', '00'])
        self.assertEqual(HtmlColorCode_to_strings('#FFCC00'), ['FF', 'CC', '00'])
        self.assertEqual(HtmlColorCode_to_strings('ffcc00'), ['ff', 'cc', '00'])
        self.assertEqual(HtmlColorCode_to_strings('#ffcc00'), ['ff', 'cc', '00'])
    
    def test_htmlcolorcodetoints(self):
        """
        check function `HtmlColorCode_to_ints`
        """
        self.assertEqual(HtmlColorCode_to_ints('FFCC00'), [255,204,0])
        self.assertEqual(HtmlColorCode_to_ints('#FFCC00'), [255,204,0])
        self.assertEqual(HtmlColorCode_to_ints('000000'), [0,0,0])
        self.assertEqual(HtmlColorCode_to_ints('FFFFFF'), [255,255,255])
        
    def test_htmlcolorcodetofloats(self):
        """
        check function `HtmlColorCode_to_floats`
        """
        self.assertEqual(HtmlColorCode_to_floats('FFCC00'), [1.0, 0.8, 0.0])
        self.assertEqual(HtmlColorCode_to_floats('#FFCC00'), [1.0, 0.8, 0.0])
        self.assertEqual(HtmlColorCode_to_floats('000000'), [0.0, 0.0, 0.0])
        self.assertEqual(HtmlColorCode_to_floats('FFFFFF'), [1.0, 1.0, 1.0])

    def test_rgbtocmyk(self):
        """
        check function `RGB_to_CMYK` with GCR (grey component replacement)
        """
        # white
        self.assertEqual(RGB_to_CMYK(1.0, 1.0, 1.0, 0.0), [0,0,0,0])
        # black
        self.assertEqual(RGB_to_CMYK(0.0, 0.0, 0.0, 0.0), [100,100,100,0])
        self.assertEqual(RGB_to_CMYK(0.0, 0.0, 0.0, 1.0), [0,0,0,100])
        # red
        self.assertEqual(RGB_to_CMYK(1.0, 0.0, 0.0, 0.0), [0,100,100,0])
        # green
        self.assertEqual(RGB_to_CMYK(0.0, 1.0, 0.0, 0.0), [100,0,100,0])
        # blue
        self.assertEqual(RGB_to_CMYK(0.0, 0.0, 1.0, 0.0), [100,100,0,0])
        
    def test_htmlcolorcodetocmyk(self):
        """
        check function `HtmlColorCode_to_CMYK`
        """
        self.assertEqual(HtmlColorCode_to_CMYK('FFFFFF', 1.0), [0,0,0,0])
        self.assertEqual(HtmlColorCode_to_CMYK('#FFFFFF', 1.0), [0,0,0,0])
        self.assertEqual(HtmlColorCode_to_CMYK('000000', 1.0), [0,0,0,100])
        self.assertEqual(HtmlColorCode_to_CMYK('000000', 0.0), [100,100,100,0])
        self.assertEqual(HtmlColorCode_to_CMYK('FFFFFF', 1.0), [0,0,0,0])
        
    def test_cmyktorgb(self):
        """
        check function `CMYK_to_RGB`
        """
        self.assertEqual(CMYK_to_RGB('0,0,0,100'), [0.0,0.0,0.0])
        self.assertEqual(CMYK_to_RGB('100,80,0,0'), [0.0,51.0,255.0])
        self.assertEqual(CMYK_to_RGB(''), None)
        
    def test_cmyktohtmlcolorcode(self):
        """
        check function `CMYK_to_HtmlColorCode`
        """
        self.assertEqual(CMYK_to_HtmlColorCode('100,80,0,0'), '#0032FF')
        self.assertEqual(CMYK_to_HtmlColorCode('0,0,0,0'), '#FFFFFF')

