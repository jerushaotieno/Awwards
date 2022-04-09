from django.http  import HttpResponse,Http404
from django.shortcuts import render, redirect
import datetime as dt

# Create your views here.

# Welcome greeting
def welcome(request):
    return render(request, 'index.html')


# View Function to present projects from today

def projects_of_day(request):
    date = dt.date.today()
    return render(request, 'today-projects.html', {"date": date,})


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
        return redirect(projects_of_day)

    return render(request, 'past-projects.html', {"date": date})