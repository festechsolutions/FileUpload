from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    # path('signup',views.signup,name='signup'),
    # path('login',views.login,name='login'),
    # path('logout',views.logout,name='logout'),
    path('userJobForm',views.userJobForm,name='userJobForm'),
    path('userdata',views.userdata,name='userdata')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
