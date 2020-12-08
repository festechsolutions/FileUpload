from django.contrib import admin
from .models import jobType, userJobTp
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(jobType)


class userjobAdmin(admin.ModelAdmin):
	
	list_display=("fname","lname","dob","phonenumber","emai","workex","jobdes","resume")
	search_fields=('fname','emai','jobdes')
	list_per_page=10
	list_filter=('jobdes',)
	sortable_by='id'
admin.site.register(userJobTp,userjobAdmin)



admin.site.unregister(Group)

admin.site.site_header="Originalle Admin panel"
admin.site.site_title='Originalle admin'
admin.site.index_title='Originalle administration'


