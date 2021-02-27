from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search-index', views.search_results, name='search-results'),
    path('project-list', views.project_list, name='project-list'),
    path('project-contents', views.project_contents, name='project-contents'),
    path('folder-contents', views.folder_contents, name='folder-contents'),
    path('file-contents', views.file_contents, name='file-contents'),
    path('issue-create', views.issue_create, name='issue-create'),
    path('issue-read', views.issue_read, name='issue-read'),
    path('issue-update', views.issue_update, name='issue-update'),
    path('issue-delete', views.issue_delete, name='issue-delete'),
    path('issue-list', views.issue_list, name='issue-list'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]