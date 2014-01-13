from __future__ import unicode_literals
from django.contrib.contenttypes.models import ContentType

import re

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine import template
from hitcount.models import HitCount

register = template.Library()


@register.as_tag
def sc_recent_notice(limit=8):
    category = BlogCategory.objects.get(slug='notice')
    blog_posts = BlogPost.objects.published().filter(categories=category)
    return list(blog_posts[:limit])

@register.as_tag
def sc_hottest(limit=8):
    '''
    posts = BlogPost.objects.all().extra(
            select={
                'hit_count':'select hits from hitcount_hit_count as t where t.content_type_id=18 and t.object_pk = blog_blogpost.id',},).order_by("hit_count")[:10]
    return posts
    '''
    ct = ContentType.objects.get_for_model(BlogPost)
    post_ids = HitCount.objects.values_list("object_pk", flat=True).filter(content_type=ct).order_by("-hits")
    posts = BlogPost.objects.filter(pk__in=post_ids)
    return list(posts[:limit])

@register.as_tag
def sc_recommand(limit=5):
    blog_posts = BlogPost.objects.published().filter(recommand=True)
    return list(blog_posts[:limit])

html_remove = re.compile(r'\s*<.*?>\s*',re.I|re.U|re.S)
@register.filter("limit_chars")
def limit_chars(value, max_length):
    value = html_remove.sub('', value)
    if len(value) > max_length:
        truncd_val = value[:max_length]
        if not len(value) == max_length+1 and value[max_length+1] != " ":
            truncd_val = truncd_val[:truncd_val.rfind(" ")]
        return  truncd_val + "..."
    return value
