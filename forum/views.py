from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from haystack.forms import ModelSearchForm, HighlightedSearchForm
from .models import Post, UserProfile, User
from .forms import UserForm, EditUserForm, UserProfileForm, LoginForm, ThreadForm, CommentForm
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=2)

# Create your views here.
def index(request):
	latest_post_list = Post.objects.filter(thread_post__isnull=True).order_by('-pub_date')[:]
	context = {
		'output': latest_post_list
	}
	return render_to_response('index.jinja', context, 
		context_instance=RequestContext(request))

def search(request):
	form = ModelSearchForm(request.GET)
	results = form.search()

	context = {
		'form':form,
	}
	return render_to_response('search/search.jinja', context, \
		context_instance=RequestContext(request))

def detail(request, id=None):
	post = get_object_or_404(Post, id=id)
	comments = Post.objects.filter(thread_post=id)
	context = {
		'post': post,
		'message': request.GET.get('message'),
		'comments': comments,
		'comment_form': CommentForm()
	}
	return render_to_response('detail.jinja', context,
		context_instance=RequestContext(request))

@login_required(login_url='/forum/login/')
def add_comment(request, id=None):
	if request.method == 'POST':
		add_comment_form = CommentForm(data=request.POST)
		if add_comment_form.is_valid():
			if request.user.is_authenticated:
				comment = add_comment_form.save(commit=False)
				comment.author_id = request.user.id
				comment.thread_post_id = id
				comment.save()

				return detail(request, id)
			else:
				context = {
					'login_Form': LoginForm(),
					'redirect_message': '发言前请登录'
				}
				return render_to_response('login.jinja', context,
			context_instance=RequestContext(request))
		else:
			return detail(request, id)
	else:
		pass

@login_required
def add_thread(request):
	if request.method == 'POST':
		add_thread_form = ThreadForm(data=request.POST)
		if add_thread_form.is_valid():
			if request.user.is_authenticated():
				thread = add_thread_form.save(commit=False)

				m_tags = add_thread_form.cleaned_data['tags']

				thread.author_id = request.user.id
				thread.save()
				for m_tag in m_tags:
					thread.tags.add(m_tag)
				return HttpResponseRedirect('/forum/')
		else:
			print (add_thread_form.errors)
	else:
		add_thread_form = ThreadForm()

	context = {
		'add_thread_form': add_thread_form
	}

	return render_to_response('add_thread.jinja', context,
		context_instance=RequestContext(request))

def user_detail(request, username=None):
	user = User.objects.get(username=username)

	#user_profile = UserProfile.objects.filter(id=user.id)
	context = {
		'user_detail': user
	}

	return render_to_response('user_detail.jinja', context,
		context_instance=RequestContext(request))

@login_required(login_url='/forum/login/')
def edit_profile(request, username=None):
	user = get_object_or_404(User, username=username)
	userprofile = user.userprofile
	if request.method == 'POST':
		user_form = EditUserForm(request.POST, instance=user)
		userprofile_form = UserProfileForm(request.POST, instance=userprofile)
		if userprofile_form.is_valid():
			user_form.save()
			userprofile_form.save()
			return index(request)
	else:
		user_form = EditUserForm(instance=user)
		userprofile_form = UserProfileForm(instance=userprofile)

	pp.pprint(userprofile_form.as_p())
	context = {
		'username':			username,
		'user_form': 		user_form,
		'userprofile_form': userprofile_form
	}
	return render_to_response('edit_profile.jinja', context,
		context_instance=RequestContext(request))

@login_required(login_url='/forum/login/')
def edit_post(request, id=None):
	# Handy method to show an error page if id is None
	post = get_object_or_404(Post, id=id) 
	if request.method == 'POST':
		edit_form = ThreadForm(request.POST, instance=post)
		if edit_form.is_valid():
			post = edit_form.save(commit=False)
			post.author_id = request.user.id
			m_tags = edit_form.cleaned_data['tags']
			print ('m_tags = ', m_tags)
			# Need to update the time
			if not post.pub_date:
				post.pub_date = timezone.now()
			post.last_edited_date = timezone.now()
			post.save()
			post.tags.clear()
			for m_tag in m_tags:
				print ('m_tag:', m_tag)
				post.tags.add(m_tag)
			
			return detail(request, id)
	else:
		edit_form = ThreadForm(instance=post)

	return render_to_response('edit_thread.jinja', \
		{'edit_form':edit_form},
		context_instance=RequestContext(request))

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'avator' in request.FILES:
				profile.avator = request.FILES['avator']

			profile.save()

			registered = True

		else:
			print (user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	context = {
		'user_form': user_form,
		'profile_form': profile_form,
		'registered': registered
	}

	return render_to_response('register.jinja', context,
		context_instance=RequestContext(request))

# We use a subclass of AuthenticationForm
def user_login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		login_form = LoginForm(data=request.POST)

		if login_form.is_valid():
			login(request, login_form.get_user())
			return HttpResponseRedirect('/forum/')
	else:
		login_form = LoginForm()

	context = {
		'login_form': login_form,
		'redirect_message': '发言前请登录'
	}
	
	return render_to_response('login.jinja', context,
			context_instance=RequestContext(request))

@login_required(login_url='/forum/login/')
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/forum/')