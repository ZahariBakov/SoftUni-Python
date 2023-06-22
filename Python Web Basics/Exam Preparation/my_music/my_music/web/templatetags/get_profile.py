from django import template

from my_music.web.models import Profile

register = template.Library()


@register.simple_tag
def get_user_profile():
    return Profile.objects.first()
