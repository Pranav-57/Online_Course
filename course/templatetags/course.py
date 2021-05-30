from django import template

register = template.Library()


@register.filter(name='duration')
def duration(duration):
    return int(duration/60)

@register.filter(name='check')
def check(name, incoming_name):
    if name == incoming_name:
        return True
    else:
        return False