# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.template import Library, Node

DUOSHUO_SHORT_NAME = getattr(settings, "DUOSHUO_SHORT_NAME", None)

register = Library()

class DuoshuoCommentsNode(Node):
    def __init__(self, short_name=DUOSHUO_SHORT_NAME):
        self.short_name = short_name

    def render(self, context):
        code = '''<!-- Duoshuo Comment BEGIN -->
        <div class="ds-thread"></div>
        <script type="text/javascript">
        var duoshuoQuery = {short_name:"%s"};
        (function() {
            var ds = document.createElement('script');
            ds.type = 'text/javascript';ds.async = true;
            ds.src = 'http://static.duoshuo.com/embed.js';
            ds.charset = 'UTF-8';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ds);
        })();
        </script>
        <!-- Duoshuo Comment END -->''' % self.short_name
        return code
    
def duoshuo_comments(parser, token):
    short_name = token.contents.split()   
    if DUOSHUO_SHORT_NAME:
        return DuoshuoCommentsNode(DUOSHUO_SHORT_NAME)
    elif len(short_name) == 2:
        return DuoshuoCommentsNode(short_name[1])
    else:
        raise template.TemplateSyntaxError, "duoshuo_comments tag takes SHORT_NAME as exactly one argument"
duoshuo_comments = register.tag(duoshuo_comments)

@register.simple_tag
def duoshuo_id_for(obj):
    """
    Returns a unique identifier for the object to be used in
    DISQUS JavaScript.
    """
    return "%s-%s" % (obj._meta.object_name, obj.id)

@register.simple_tag
def duoshuo_shortname():
    return DUOSHUO_SHORT_NAME

# 生成remote_auth，使用JWT后弃用
# @register.filter
# def remote_auth(value):
#     user = value
#     duoshuo_query = ds_remote_auth(user.id, user.username, user.email)
#     code = '''
#     <script>
#     duoshuoQuery['remote_auth'] = '%s';
#     </script>
#     ''' % duoshuo_query
#     return code
# remote_auth.is_safe = True
