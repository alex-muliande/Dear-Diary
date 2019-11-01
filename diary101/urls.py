from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url,include
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,ReviewCreateView
from . import views
urlpatterns = [
    path('',  PostListView.as_view(), name='projects-index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    path('profile/details/<str:username>/',views.display_profile, name = 'profile-detail'),


]
