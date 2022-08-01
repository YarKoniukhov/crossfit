from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileUser(admin.ModelAdmin):

    list_display = ['fio', 'age', 'kind_of_sport']


admin.site.register(Profile, ProfileUser)
