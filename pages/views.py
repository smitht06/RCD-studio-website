from django.views.generic import TemplateView, ListView, DetailView
from .models import Page, TeamMember, BlogPost, Project


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['team'] = TeamMember.objects.all()
        context['posts'] = BlogPost.objects.order_by('-publication_date').all()
        context['projects'] = Project.objects.all()
        return context

class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'team.html'
    
    ordering = ['name']
    
class TeamMemberDetailView(DetailView):
    model = TeamMember
    template_name = 'team_detail.html'
    
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog.html'
    
    ordering = ['-publication_date']
        
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
    
class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    
    ordering = ['-release_date']
        
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
