from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.logout_user, name="log out user"),
    path('register/',views.register_user, name="register user"),
    path('record/<int:pk>',views.customer_record, name="customer record"),
    path('delete_record/<int:pk>', views.delete_record, name="delete record"),
    path('add_record/', views.add_record, name="add record"),
    path('update_record/<int:pk>', views.update_record, name="update record"),
]

