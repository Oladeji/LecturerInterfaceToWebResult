from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
  
    path('', views.landing, name='landing'),
    path('login_view', views.login_view, name='login_view'),
    # path('logout_view', views.logout_view, name='logout_view'),
    path('logout_view', auth_views.LogoutView.as_view(template_name='GradeManager/landing.html'), name='logout_view'),
    path('register_view', views.register_view, name='register_view'),
    path('availableCourses_view', views.availableCourses_view, name='availableCourses_view'), 
    path('displayCourseview/<str:csrid>', views.displayCourse_view, name='displayCourse_view'), 
    # path('download', views.export_users_xls, name='export_users_xls'),
    # path('uploadscore', views.uploadscore, name='uploadscore'),
    # path('uploadscores', views.uploadexcelscores, name='uploadscores'),

]
