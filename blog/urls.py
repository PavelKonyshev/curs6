from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView

app_name = BlogConfig.name

urlpatterns = [
    # Урлы для главной страницы
    path('blog/', BlogListView.as_view(), name='blog_list'),
]