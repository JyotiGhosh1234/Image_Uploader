from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.upload, name="uploadpage"),
    path('delete_data/<int:id>/', views.delete_data , name='deletedata'),
    path('update_data/<int:id>/', views.update_data , name='updatedata'),
]
