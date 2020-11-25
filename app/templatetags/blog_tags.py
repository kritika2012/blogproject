from app.models import Post
from django import template
from django.db.models import Count

register=template.Library()

@register.simple_tag
def total_post():
    return Post.objects.count()

@register.inclusion_tag('app\\latest_post.html')
def show_latest_post(count=3):
    latest=Post.objects.order_by('-publish')[:count]
    return {'latest':latest}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('Comments')).order_by('-total_comments')[:count]
