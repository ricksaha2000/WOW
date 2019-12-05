from django.shortcuts import render
from events.models import Event
from jobs.models import Job
from communities.models import Community


def home_view(request):
    events = Event.objects.all()
    jobs = Job.objects.all()
    communities = Community.objects.all()
    context = {
        'events': events,
        'jobs': jobs,
        'communities': communities,
        'title': 'Home',
    }
    return render(request, 'home/home.html', context)


def about_view(request):
    context = {
        'title': 'About Us',
    }
    return render(request, 'home/about.html', context)


def contact_view(request):
    context = {
        'title': 'Contact',
    }
    return render(request, 'home/contact.html', context)
