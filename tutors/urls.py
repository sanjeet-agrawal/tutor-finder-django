from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutor_list, name='tutor_list'),
    path('edit-profile/', views.edit_tutor_profile, name='edit_tutor_profile'),
    path('<int:tutor_id>/', views.tutor_detail, name='tutor_detail'),
    
]