from django import template

register = template.Library()

# Option 1: register with Decorators
@register.filter(name='cutstring')

def cutstring(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# Option 2: Register template to library
#register.filter('cutstring', cutstring)