from calendar import month_name

from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.templatetags.static import static

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.blog.feeds import PostsRSS, PostsAtom
from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import render, paginate
from mezzanine.utils.models import get_user_model
from .models import ApplyLink

cate_dics = {}
catedb = BlogCategory.objects.all()
for c in catedb:
    cate_dics[c.slug] = c

static_images = []
for i in range(1,4,1):
    static_images.append(static('images/banner%d.jpg' %i ))

def blog_post_home(request, template="index.html"):
    settings.use_editable()
    templates = []

    cnt = 8
    news = BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['news'])[:cnt]

    acts = list(BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['activity'])[:cnt])

    briefs = BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['brief'])[:cnt]
    
    coms = BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['company'])[:cnt]

    clubs = BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['club'])[:cnt]

    jobs = BlogPost.objects.published(for_user=request.user).filter(categories=cate_dics['job'])[:cnt]

    ap_links = ApplyLink.objects.filter(permit=True)

    images = []
    for a in acts:
        if a.featured_image:
            images.append(a.featured_image.url)
    if len(images) < 6:
        images += static_images[:cnt-len(images)]
    #print images

    context = {"news":news, "blog_posts": acts, "briefs":briefs, "coms":coms, "clubs":clubs,  "jobs":jobs, 'imgs':images, 'ap_links':ap_links}

    templates.append(template)
    return render(request, templates, context)

