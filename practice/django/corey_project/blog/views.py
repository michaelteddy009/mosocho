from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
# Create your views here.


'''
#this is a function based view which we replace with a class based view below

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)'''

class PostListView(ListView):
	model = Post  #the model to query inorder to create our view.
	template_name = 'blog/home.html' #<app>/<model>_<Viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']   #to enable the latest post being displayed first.
	paginate_by = 3

#query posts specific to a user.
class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	#ordering = ['-date_posted']
	paginate_by = 3

	#when a person is clicked we get specific query relating to the person
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	#give the form a condition that the person should login first before creating a form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	#give the form a condition that the person should login first before creating a form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#run the test for current author is the user to enable deleting
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return false

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return false



def about(request):
	return render(request, 'blog/about.html', {'title':'about'})
