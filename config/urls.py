from django.urls import path, include
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
]

# Django 2.0 이전 : URL 패턴을 지정하기 위해 정규표현식(RegEx)을 사용한 django.conf.urls.url()
# Django 2.0 이후, django.urls.path() 또는 django.urls.re_path() 함수를 사용.

# from django.conf.urls import include, url
# # 정규식 conf.urls
# from django.contrib import admin
# from django.contrib.auth import views
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^accounts/login/$', views.login, name='login'),
#     url(r'', include('blog.urls')),
# ]
