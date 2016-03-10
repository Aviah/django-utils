import re
from django import template
from django.conf import settings

register = template.Library()

@register.filter
def intmonth(value):
    """ returns a month label from an int number
    In template: Invoice Month - {{ invoice_month|intmonth }}
    Will show: Invoirce Month: Jan"""
    
    try:
        return ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][int(value)-1]
    except:
        return value
    
@register.filter
def currencyformat(value):
    """replaces the value with a currency formated number, 0 for non number"""
    try:
        float(value)
    except:
        value = 0
    return '{:0,}'.format(int(round(value)))


@register.filter
def abs_value(value):
    """replaces the value with a absolute value, 0 for non number"""
    try:
        float(value)
    except:
        value = 0 
    return abs(value)


@register.filter
def date_format(value):
    """replaces a python date with formatted date string"""
    return value.strftime("%Y-%m-%d %H") # or any other python strftime string

@register.filter
def striftrue(value,arg):
    """ replaces value with arg if True
    {{ is_approved|striftrue "Approved" }}
    only for strict boolean, will not convert a True/False typecast"""
    return arg if value is True else ""




