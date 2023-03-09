from . import views
from django.urls import path
urlpatterns =[
    path("", views.index, name='home'),
    path('post/	online_class/', views.onlinelearning, name="post_onlinelearning"),
    path('post/agriculture_livestock_&_farming', views.agriculture, name="post_agriculture"),
    path('post/mdf_projects/', views.mdfprojects, name="post_mdfprojects"),
    path('post/community_outreach_by_mdf/', views.outreach, name="post_outreach"),
    path('post/ramadan_program', views.ramadan, name="post_ramadan"),
    path('post/Hairdressing_&_barbing', views.hair, name="post_hair"),

    path('gallery', views.gallery, name="gallery"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('team', views.team, name="team"),
    path('post/	online_class/<str:pk>/', views.singleBlog, name="online_post"),
    path('post/	mdf_projects/<str:pk>/', views.singleBlog, name="mdf_post"),
    path('post/	ramadan/<str:pk>/', views.singleBlog, name="ramadan_post"),
    path('post/	agriculture/<str:pk>/', views.singleBlog, name="agriculture_post"),
    path('post/	hair/<str:pk>/', views.singleBlog, name="hair_post"),
    path('post/outreach/<str:pk>/', views.singleBlog, name="outreach_post"),

]
