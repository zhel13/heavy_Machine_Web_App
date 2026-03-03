from django import template

register = template.Library()
@register.inclusion_tag('user_info.html', takes_context=True)
def show_user_info(context):
    if context['user'].is_authenticated:
        return {'username': context['user'].username,}

    return {'username': "Stranger",}