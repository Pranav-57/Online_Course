from django import template

register = template.Library()

@register.simple_tag
def selling_price(price, discount):
    if discount != 0:
        a = price * discount
        b = a/100
        c = price - b
        return int(c)
    else:
        return price

@register.filter(name='rupee')
def rupee(price):
    return f'₹ {price}'