from django.urls import path
from . import views

urlpatterns =[ 
    path("", views.home, name='home'),
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("papers/", views.papers, name='papers'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("admin_dash/", views.admin_dash, name='admin_dash'),
    path("api/search/", views.search_subjects, name="search_subjects"),
    path("api/subjects/<int:id>/",views.subject_detail, name="subject_detail"),
    path("api/branch/<str:branch>/", views.branch_detail, name="branch_detail"),
    path("api/papers/", views.filter_paper, name="filter_paper"),
    path("api/bookmark/<int:paper_id>/", views.toggle_bookmark, name='toggle_bookmark'),
    path("edit_profile/", views.edit_profile, name="edit_profile")
]