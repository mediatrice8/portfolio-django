from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    # url('^$',views.index,name='index'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^category/(\w+)', views.categoryPage,name='categoryPage'),
    url(r'^location/(\w+)', views.locationPage,name='locationPage'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
