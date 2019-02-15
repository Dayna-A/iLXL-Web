from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
import datetime 
import pandas as pd

from backend.models import Member, Project, Publication, Grant, Event, News, Collaborator
import requests
import json

# Home base


def home(request):
    return render(request, 'news.html', {"newslist": News.objects.all()})

# projects content


def projects(request):
    # dictionary of things that should be included in render context
    base_context = {
        # list of projects
        "projects": Project.objects.all(),
        # list of members
        "members": Member.objects.all()
    }
    return render(request, 'projects.html', base_context)

# events content


def events(request):
    return render(request, 'events.html', {"events": Event.objects.all()})

# function for obtaining list of years between today and the start of iLXL
def year_list():
    start = "2018-01-01"
    end = (datetime.date.today()).__str__()
    between= datetime.datetime.strptime(end, '%Y-%m-%d') - datetime.datetime.strptime(start, '%Y-%m-%d')
    no_years=int(float(between.days)/364.0)+1
    start_year=2018
    years=[]
    for x in range(no_years):
        years.append(2018+x)
    return {'yearList': years, 'numYears': no_years}


# publications content
def publications(request):
    base_context = {
        # obtain list of publications by year.
        yearInfo=year_List();
        publications=[[] for _ in range(yearInfo.numYears)]
        for year in yearList:

        "publications": Publication.objects.all(),
        # list of grants
        "grants": Grant.objects.all()
    }
    return render(request, 'publications.html', base_context)


# people content
def people(request):
    base_context = {
        # list of publications
        "members": Member.objects.all(),
        # list of grants
        "collaborators": Collaborator.objects.all()
    }
    return render(request, 'people.html', base_context)

# Contact Us content


def contactus(request):
    return render(request, 'contactus.html', {})


# Contact Us request form handling. The below code is commented out
# due to the removal of the slack webhooks from the form.
def submitted(request):

    if request.method == 'POST':
        fullname = request.POST["fn"]+" "+request.POST["ln"]
        email = request.POST["email"]
        webhook_url = request.POST["recipChannel"]
        sub = request.POST["subj"]
        sub = request.POST["subj"]
        messagebody = request.POST["messageContent"]
        message = "%s has sent you a message from the iLXL team site!\nSubject: %s:\nMessage:\n%s\n\nRespond via email to %s!" % (
            fullname, sub, messagebody, email)
        slack_data = {'text': message}
        r = requests.post(webhook_url, data=json.dumps(
            slack_data), headers={'Content-type': 'application/json'})
        if r.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (r.status_code, r.text)
            )

    return render(request, 'submitted.html', {})

# Join Us content


def join(request):
    return render(request, 'join.html', {})

# Applied content


def applied(request):
    if request.method == 'POST':
        # obtain form results.
        fname = request.POST["fn"]
        lname = request.POST["ln"]
        email = request.POST["email"]
        highest = request.POST["highest"]
        status = request.POST["status"]
        grad = request.POST["grad"]
        if request.POST.get("epp") is not None:
            epp = request.POST["epp"]
        if("epp" == "1"):
            epp = "has"
        else:
            epp = "but has not"
        pprSubmission = request.POST["pprsub"]
        # composing email
        subject = "You've recieved a new application to join iLXL!"
        part1 = "%s student %s %s would like to join the iLXL Team.\n" % (
            status, fname, lname)
        part2 = ""
        if(grad == "Undergraduate"):
            part2 = "%s has completed %s, %s passed the epp exam and expects to graduate %s.\n" % (
                fname, highest, epp, grad)
        else:
            part2 = "%s has completed %s and expects to graduate %s.\n" % (
                fname, highest, grad)
        part3 = "%s can be reached at %s" % (fname, email)
        part4 = "and has submited the following programming problem prompts:\n%s" % (
            pprSubmission)
        message = "%s %s %s %s" % (part1, part2, part3, part4)
        email = EmailMessage(subject, message, to=["jtcshen@fullerton.edu"])
        email.send()
    return render(request, 'applied.html', {})
