from django import template

register = template.Library()

@register.filter(name='add_class_to_fields')
def add_class_to_fields(form, css_class):
    for field_name, field in form.fields.items():
        field.widget.attrs.update({'class': css_class})
    return form