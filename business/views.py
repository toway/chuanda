from calendar import month_name

from django.http import Http404
from django.shortcuts import get_object_or_404

from django.shortcuts import render
from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.blog.feeds import PostsRSS, PostsAtom
from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import render, paginate
from mezzanine.utils.models import get_user_model

cate_dics = {}
catedb = BlogCategory.objects.all()
for c in catedb:
    cate_dics[c.slug] = c

def blog_post_home(request, template="index.html"):
    settings.use_editable()
    templates = []

    news = BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['news'])

    acts = BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['activity'])

    briefs = BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['brief'])
    
    coms = BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['company'])

    clubs = BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['club'])

    jobs = BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['job'])

    context = {"news":news, "blog_posts": acts, "briefs":briefs, "coms":coms, "clubs":clubs,  "jobs":jobs}

    templates.append(template)
    return render(request, templates, context)

