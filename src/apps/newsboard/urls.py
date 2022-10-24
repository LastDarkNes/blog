from django.urls import path, re_path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.return_to_home_page, name='return_to_home_page'),
    path('home/<int:page>', views.news_render, name='newsboard'),
    path('home/', views.news_render, name='newsboard'),
    path('post/<int:pk>', views.single_post, name='single_post')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
