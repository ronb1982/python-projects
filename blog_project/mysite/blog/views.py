from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView)                                

# Helpers
def init_login_attributes():
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    
def init_model_attributes():
    form_class = PostForm
    model = Post

# VIEWS
class AboutView(TemplateView):
    template_name = 'about.html'
    
class PostListView(ListView):
    model = Post
    
    # This is like running a DB query on the Post object
    # __lte = less than or equal to
    # '-field_name' = descending order (minus in front)
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        
class PostDetailView(DetailView):
    model = Post
    
class CreatePostView(LoginRequiredMixin,CreateView):
    init_login_attributes()
    init_model_attributes()
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    init_login_attributes()
    init_model_attributes()
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
    models = Post
    success_url = reverse_lazy('post_list')
    
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
        
    ############################################
    ############################################
    
    @login_required
    def post_publish(request,pk):
        post = get_object_or_404(Post,pk=pk)
        post.publish()
        return redirect('post_detail',pk=pk)
    
    @login_required
    def add_comment_to_post(request,pk):
        post = get_object_or_404(Post,pk=pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form':form})    
        
    @login_required
    def comment_approve(request,pk):
        comment = get_object_or_404(Comment,pk=pk)
        comment.approve()
        return redirect('post_detail',pk=comment.post.pk)
        
    @login_required
    def comment_remove(request,pk):
        comment = get_object_or_404(Comment,pk=pk)
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post_detail',pk=comment.post.pk)
    