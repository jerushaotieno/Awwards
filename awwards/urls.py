# from django.conf.urls import url
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django_registration.backends.one_step.views import RegistrationView
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url(r'^$',views.projects_today,name='projectsToday'),
    url(r'^profile/$', views.profile, name='profile'),
    url('^search/', views.search, name='search'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/',
        RegistrationView.as_view(success_url=reverse_lazy('home')),
        name='django_registration_register'),

    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path(r'login/', LoginView.as_view(), {"next_page": '/'}),
]

urlpatterns += staticfiles_urlpatterns()

# urlpatterns=[
#     
#     url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_projects,name = 'pastProjects'),
#     url(r'^search/', views.search_results, name='search_results')
#     # url(r'^project/(\d+)',views.project,name ='project')
# ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

