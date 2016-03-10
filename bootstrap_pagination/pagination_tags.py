import re
from django import template

register = template.Library()
regex_page = re.compile("page=[0-9]+")

@register.filter
def add_page_arg(url,page_index):
    
    if regex_page.search(url) != None:
        return regex_page.sub("page=%s"%page_index,url)
    else:
        url_base = "%s&&page=%s" if "?" in url else "%s?page=%s"
        return url_base%(url,page_index,)