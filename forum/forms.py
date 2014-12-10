from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField
from ckeditor.widgets import CKEditorWidget
from taggit.forms import *
from .models import UserProfile, Post

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'col-lg-10 form-control'}))
	captcha = CaptchaField()

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {
			'username': forms.TextInput(attrs={'class': 'col-lg-10 form-control'}),
			'email': forms.TextInput(attrs={'class': 'col-lg-10 form-control'})
		}
		help_texts = {
			'username': _('You can\'t change your username'),
		}
		error_message = {
			'username': {
				'max_length' : _("This username is too long."),
				'required': _("请填写用户名")
			},
		}

class EditUserForm(forms.ModelForm):
	class Meta(UserForm):
		model = User
		fields = ('email', )
		widgets = {
			'email': forms.TextInput(attrs={'class': 'col-lg-10 form-control'}),
		}
		error_message = {
			'username': {
				'max_length' : _("This username is too long."),
				'required': _("请填写用户名")
			},
		}

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avator',)

class LoginForm(AuthenticationForm):
	captcha = CaptchaField()

	class Meta:
		model = User
		fields = ('username', 'password')
		widgets = {
            'username': forms.TextInput(attrs={'class': 'col-lg-10 form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'col-lg-10 form-control'}),
        }

	def clean(self): # Raise a customized error here
		#self.error_messages['invalid_login'] = 'Invalid username or password.'
		return super(LoginForm, self).clean()

class ThreadForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content', 'tags')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'col-lg-10 form-control', 'title':'标题'}, ),
			'content': forms.Textarea(attrs={'class': 'col-lg-10 form-control', 'title':'内容'}, ),
			'tags': TagWidget(attrs={'class': 'col-lg-10 form-control', }),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('content',)
		widgets = {
			'content': CKEditorWidget(attrs={'label':'Reply'}),
		}
			