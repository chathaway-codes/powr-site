from django.contrib import admin

from team.models import Profile, Comment, File

class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name",)}

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment)
admin.site.register(File)
