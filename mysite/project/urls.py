from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article', views.article, name='article'),
    url(r'^reddit', views.reddit, name='reddit'),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
