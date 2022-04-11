from django.http  import HttpResponse,Http404, request
from django.shortcuts import render, redirect
import datetime as dt
from .models import Project, UserProfile, UserRating
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# Welcome greeting
def welcome(request):
    return render(request, 'index.html')


# View Function to present projects from today

def projects_today(request):
    date = dt.date.today()
    awwards = Project.objects.all()
    return render(request, 'all-projects/today-projects.html', {"date": date,"awwards":awwards})


# View Function to present projects from past days

def past_days_projects(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(projects_today)

    awwards = Project.days_projects(dt.date)
    return render(request, 'all-projects/past-projects.html',{"date": dt.date,"awwards":awwards})


# Search View

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-projects/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-projects/search.html',{"message":message})


# Individual Project View

def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except Project.DoesNotExist:
        raise Http404()
    return render(request,"all-projects/project.html", {"project":project})