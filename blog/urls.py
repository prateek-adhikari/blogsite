from django.urls import path
from  . import views
from .views import HomePageView, PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
