from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from compromisso import views as compromisso_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', compromisso_views.compromisso_list, name="home"),
    path('accounts/', include('accounts.urls')),
    path('compromissos/', include('compromisso.urls')),
]

urlpatterns += staticfiles_urlpatterns()
