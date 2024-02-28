from django.urls import path

from .views import HomePageView, TeamMemberListView, TeamMemberDetailView, BlogPostListView, BlogPostDetailView, ProjectListView, ProjectDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('team/', TeamMemberListView.as_view(), name='team'),
    path('team/<int:pk>/', TeamMemberDetailView.as_view(), name='team_detail'),
    path('blog/', BlogPostListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]
