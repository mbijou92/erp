from django import template

register = template.Library()


@register.filter
def getattr_(obj, k):
    return getattr(obj, k)


@register.filter
def get_dict(obj, k):
    if not obj:
        print(obj)
        return ""
    print(obj[k])
    if k in obj:
        return obj[k]
    else:
        return ""

@register.filter
def get_image_path_from_object(obj, k):
    return getattr(obj, k).url