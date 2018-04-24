(r'^$', 'gsdjango.blog.views.index'),
url(
    r'^blog/view/(?P<slug>[^\.]+).html', 
    'gsdjango.blog.views.view_post', 
    name='view_blog_post'),
url(
    r'^blog/category/(?P<slug>[^\.]+).html', 
    'gsdjango.blog.views.view_category', 
    name='view_blog_category'),
