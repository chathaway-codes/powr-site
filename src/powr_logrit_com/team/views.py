from django.views.generic.list import ListView

from team.models import Profile, File

class ProfileListView(ListView):
    model = Profile

class FileListView(ListView):
    model = File
