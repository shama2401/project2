from blog.models import Category
from django import template
from django.db.models import Count, F

register = template.Library()

@register.simple_tag(name='get_list_category')
def get_category():
    return Category.objects.all()


@register.inclusion_tag('blog/show_category.html')
def show_category():
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published')).filter(cnt__gt=0))
    return {'categories' : categories}