from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('profile-page/', views.profile_page, name='profile'),
    path('user-data/', views.user_data, name='userdata'),
    path('to-do-list/add-page/', views.to_do_create_view, name='to_do_create'),
    path('to-do-list/update-page/<slug:slug>/', views.to_do_update_view, name='to_do_update'),
    path('to-do-list/delete-page/<slug:slug>/', views.to_do_delete_view, name='to_do_delete'),
]
