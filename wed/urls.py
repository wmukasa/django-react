from django.urls import path
from .views import BlogPostListView,BlogPostDetailView,BlogPostFeacturedView,BlogPostcategoryView
urlpatterns =[
    path('',BlogPostListView.as_view()),
    path('featured',BlogPostFeacturedView.as_view()),
    path('category',BlogPostcategoryView.as_view()),
    path('<slug>',BlogPostDetailView.as_view()),
    
]