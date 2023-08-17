from django import template
from django.utils.safestring import mark_safe

from django.utils import timezone

register = template.Library()

@register.filter(name="bool_icon", is_safe=True)
def bool_icon(value, arg):
    if value == True:
        return mark_safe('<i class="fa-solid {0}"></i>'.format(arg))
    else:
        return mark_safe('<i class="relative fa-solid {0}"><i class="absolute left-0 fa-solid fa-slash text-danger"></i></i>'.format(arg))
    
@register.filter(name="slide_range")
def slide_range(value):
    return range(0, value - 1)


@register.filter(name="age")
def age(value):

    now = timezone.now().date()
    # Calculate Years, return years if 1 or older.
    years = int(now.year) - int(value.year) - ((int(now.month), int(now.day)) < (int(value.month), int(value.day)))
    if years > 1:
        return str(years) + " Years"
    elif years == 1:
        return str(years) + " Year"
    else:
        # Calculate months, if less than a month, return message
        months = int(now.month) - int(value.month)
        if months > 1:
            return str(months) + " Months"
        elif months == 1:
            return str(months) + " Month"
        else:
            return "Less than a month"
    