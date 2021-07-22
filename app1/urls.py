from .views import(
    StudentList,
    StudentAPI, 
    LoginAPIView, 
    LogoutAPIView,
    RegisterAPIView,
    index

)
from django.urls import path


urlpatterns = [
    path("index/",index,name="index"),
    path("studentlist/<int:id>/", StudentList.as_view(), name="studentlist"),
    path("studentlist/", StudentList.as_view(), name='studentlist'),
    path("student/", StudentAPI.as_view(), name='student'),
    path("student/<int:id>/", StudentAPI.as_view(), name='student'),
    path('student/login/', LoginAPIView.as_view(), name='login'),
    path("student/logout/", LogoutAPIView.as_view(), name='logout'),
    path("student/register/", RegisterAPIView.as_view(), name='register')   

]
