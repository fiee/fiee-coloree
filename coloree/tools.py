#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assert_on_exception(fn):
    """
    This decorator cares that exceptions raised by the wrapped widget won’t get swallowed by Django.
    
    In custom Django widgets or admin list_display callable functions you have probably run into this: 
    Everything looks ok, except the place where your widget should be is just blank. 
    Nothing. No traceback or any clue as to what went wrong.

    It seems that Django suppresses all the exceptions sent by widgets rendering 
    except for AssertionError and TypeError. Debugging under those conditions is tricky, 
    so I wrote a function decorator to help. 
    Just import this and put @assert_on_exception before your render method or admin list_display callable function.
    
    by Ian Ward, http://excess.org/article/2010/12/django-hides-widget-exceptions/
    """
    import sys
    def wrap(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except (AssertionError, TypeError):
            raise
        except:
            assert 0, sys.exc_info()[0].__name__ + ": " + str(sys.exc_info()[1])
    wrap.__name__ = fn.__name__
    wrap.__dict__.update(fn.__dict__)
    wrap.__doc__ = fn.__doc__
    wrap.__module__ = fn.__module__
    return wrap