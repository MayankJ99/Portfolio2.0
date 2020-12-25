from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.index, name='personal-index'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='personal-login'),
    path('logout', auth_views.LogoutView.as_view(), name='personal-logout'),

    path('newProject', views.CreateProject.as_view(), name='create'),
    path('newWork', views.CreateWork.as_view(), name='work'),
    path('newQuote', views.CreateQuote.as_view(), name='quote'),

    re_path(r"deleteProject/(?P<pk>\d+)/$", views.DeleteProject.as_view(), name="deleteProject"),
    re_path(r"deleteWork/(?P<pk>\d+)/$", views.DeleteWork.as_view(), name="deleteWork"),

    re_path(r"updateProject/(?P<pk>\d+)/$", views.UpdateProject.as_view(), name="updateProject"),
    re_path(r"updateWork/(?P<pk>\d+)/$", views.UpdateWork.as_view(), name="updateWork"),
    path('edit', views.EditProfile, name='edit'),
    # path('blog', views.blogList, name='bloglist'),
    re_path(r"article/(?P<pk>\d+)/$", views.blogDetail.as_view(), name="blog-detail"),
    path('newArticle', views.CreateArticle.as_view(), name='new-blog'),
    re_path(r"deleteArticle/(?P<pk>\d+)/$", views.deleteArticle.as_view(), name="blog-delete"),
    re_path(r"updateArticle/(?P<pk>\d+)/$", views.updateArticle.as_view(), name="blog-update"),
    re_path(r'^tinymce/', include('tinymce.urls')),
]
# handler404 = views.handler404
# handler500 = views.handler500
