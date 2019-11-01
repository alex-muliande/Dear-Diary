from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views
urlpatterns = [
    path('',  views.index, name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),


]
