from django.urls import path,re_path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.index, name='personal-index'),
        path('login', auth_views.LoginView.as_view(template_name ='login.html'), name='personal-login'),
        path('logout', auth_views.LogoutView.as_view(), name = 'personal-logout'),

        path('newProject', views.CreateProject.as_view(), name='create'),
        path('newWork', views.CreateWork.as_view(), name='work'),
        path('newQuote', views.CreateQuote.as_view(), name='quote'),

        re_path(r"deleteProject/(?P<pk>\d+)/$",views.DeleteProject.as_view(),name="deleteProject"),
        re_path(r"deleteWork/(?P<pk>\d+)/$",views.DeleteWork.as_view(),name="deleteWork"),

        re_path(r"updateProject/(?P<pk>\d+)/$",views.UpdateProject.as_view(),name="updateProject"),
        re_path(r"updateWork/(?P<pk>\d+)/$",views.UpdateWork.as_view(),name="updateWork"),
        path('edit', views.EditProfile, name='edit'),
        path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]