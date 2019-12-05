from django.shortcuts import render, redirect
from .models import Event, Enrolled


def events_view(request):
    events = Event.objects.all()
    enrolled = Enrolled.objects.all()

    context = {
        "events": events,
        "enrolled": enrolled,
        "title": "Events",
    }
    return render(request, "events/events.html", context)


def event_detail_view(request, event_id):
    event = Event.objects.get(id=event_id)
    join = True
    if request.method == "POST":
        if request.user.is_authenticated:
            if Enrolled.objects.filter(user=request.user, event=event).count() == 1:
                join = True
            else:
                join = False
            update = request.POST.get('update')
            if update == "join":
                instance = Enrolled.objects.create(user=request.user, event=event)
                instance.save()
                join = False
            elif update == "leave":
                Enrolled.objects.filter(user=request.user, event=event).delete()
                join = True
            else:
                print("Error")
        else:
            return redirect('/login/')

    members = Enrolled.objects.filter(event=event).count()

    context = {
        "title": event.title,
        "event": event,
        "join": join,
        "members": members,
    }
    return render(request, "events/detail.html", context)
