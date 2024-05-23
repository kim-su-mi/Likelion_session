from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.BlogListAPIView.as_view()),
    path('<int:blog_id>/',views.BlogDetailAPIView.as_view()),
]
