from . import views
from django.urls import path
urlpatterns =[
    path("", views.index, name='home'),
    path('post/	online_class/', views.onlinelearning, name="post_onlinelearning"),
    path('post/', views.agriculture, name="post_agriculture"),
    path('post/mdf_projects/', views.mdfprojects, name="post_mdfprojects"),
    path('post', views.outreach, name="post_outreach"),
    path('post/', views.ramadan, name="post_ramadan"),
    path('post/', views.ramadan, name="post_ramadan"),

    path('gallery', views.gallery, name="gallery"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('team', views.team, name="team"),
    path('post/	online_class/<str:pk>/', views.singleBlog, name="online_post"),
    path('post/	mdf_projects/<str:pk>/', views.singleBlog, name="mdf_post"),

]
