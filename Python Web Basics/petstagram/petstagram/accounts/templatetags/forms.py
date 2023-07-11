from django import template

register = template.Library()


@register.filter
def placeholder(input_field, text):
    input_field.field.widget.attrs['placeholder'] = text

    return input_field


@register.filter
def form_field_class(form_field, class_name):
    default_classname = form_field.field.widget.attrs.get('class', '')
    form_field.field.widget.attrs['class'] = default_classname + ' ' + class_name

    return form_field
