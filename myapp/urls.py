from django.urls import path
from . import views

urlpatterns = [
	path('',views.login, name="login"),
    path('user-dashboard/<str:user_id>',views.UserDashBoard, name="user-dashboard"),
    path('delete-records/<int:id>',views.DeleteUserRecords, name="delete-record"),
]
