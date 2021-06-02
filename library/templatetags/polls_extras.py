from django import template

register = template.Library()

def find(value,args):
    for a in args:
        if value == a:
            return True
    return False

register.filter("find", find)
