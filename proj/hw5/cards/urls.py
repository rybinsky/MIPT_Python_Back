from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('card_list/', views.card_list_view, name='card_list'),
    path('create/', views.card_create_view, name='card_create'),
    path('<int:pk>/', views.card_detail_view, name='card_detail'),
    path('<int:pk>/update/', views.card_update_view, name='card_update'),
    path('<int:card_id>/comment/create/', views.comment_create_view, name='comment_create'),
    path('comment/<int:pk>/delete/', views.comment_delete_view, name='comment_delete'),
    path('<int:pk>/like/', views.card_like_view, name='card_like'),
    path('<int:pk>/dislike/', views.card_dislike_view, name='card_dislike'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]