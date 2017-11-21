from django.conf.urls import url
from core.views import index, article_detail

urlpatterns = [
    url(r'^$', index, name = 'core_index'),
    url(r'^detail/(?P<pk>\d+)/$', article_detail, name = 'core_article_detail'),

]
