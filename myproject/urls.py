# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('handle-get/', views.handle_get, name='handle_get'),
    path('handle-post', views.handle_post, name='handle_post'),
]