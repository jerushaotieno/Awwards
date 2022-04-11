from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.projects_today,name='projectsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_projects,name = 'pastProjects')
]
