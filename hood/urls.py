from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns= [
    url(r'^$',views.homm, name="home"),
    url(r'register/', views.register, name="register"),
    url(r'accounts/', include('django.contrib.auth.urls')),
]
