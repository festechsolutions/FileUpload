from django.contrib import admin
from .models import Vacancie, Candidate
from django.contrib.auth.models import Group

# Register your models here.
class vacancieAdmin(admin.ModelAdmin):
	list_display = ("position","description","salary","experience","location")
admin.site.register(Vacancie,vacancieAdmin)


class userjobAdmin(admin.ModelAdmin):
	
	list_display=("First_name","Last_name","DOB","phonenumber","mail_ID","experience","Position","resume")
	search_fields=('First_name','mail_ID','Position')
	list_per_page=10
	list_filter=('Position',)
	sortable_by='id'
admin.site.register(Candidate,userjobAdmin)



admin.site.unregister(Group)

admin.site.site_header="Originalle Admin panel"
admin.site.site_title='Originalle admin'
admin.site.index_title='Originalle administration'


