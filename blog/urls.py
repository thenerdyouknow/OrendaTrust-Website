# from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/', views.allblogs, name='allblogs'),
    path('blog/<int:blog_id>/', views.detail, name="detail"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
