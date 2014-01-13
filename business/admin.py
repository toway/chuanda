from copy import deepcopy
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost
from .models import ApplyLink
from mezzanine.pages.admin import PageAdmin

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-1, "recommand")

class ChuandaBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets

link_extra_fieldsets = ((None, {"fields": ("url","name","permit")}),)
class ApplyLinkAdmin(PageAdmin):
    fieldsets = link_extra_fieldsets
admin.site.register(ApplyLink, ApplyLinkAdmin)

admin.site.unregister(BlogPost)
admin.site.register(BlogPost, ChuandaBlogPostAdmin)

