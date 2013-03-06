from django import forms
from django.contrib.comments.models import Comment
from django.contrib.comments.forms import CommentForm

from captcha.fields import CaptchaField

class CaptchaCommentForm(CommentForm):
  captcha = CaptchaField()
