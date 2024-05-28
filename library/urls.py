from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('submit-item/', views.submit_item, name='submit_item'),
    path('get-form-fields/<str:item_type>/', views.get_form_fields, name='get_form_fields'),
    path('library/<int:pk>/', views.library_detail, name='library_detail'),
    path('genre/<str:genre>/', views.genre_detail, name='genre_detail'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),

]